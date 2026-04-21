import streamlit as st
import pandas as pd

# 1. SETUP & STANDARDS
st.set_page_config(page_title="Green Building Scorer", page_icon="🌿")

# Mapping choices to scores based on International Standards (LEED-inspired)
STANDARDS = {
    "Materials (30%)": {
        "♻️ Recycled & Low-Carbon (Bio-based)": 100,
        "🚛 Locally Sourced Materials": 75,
        "🏗️ Standard Industrial Materials": 50,
        "🧱 High-Carbon / Imported Materials": 20
    },
    "Ecology (20%)": {
        "🌳 Urban Forest & High Biodiversity": 100,
        "🪴 Rooftop Garden & Vertical Greenery": 80,
        "🌿 Basic Landscaping (Grass/Trees)": 50,
        "🏢 No Greenery / Fully Paved": 10
    },
    "Energy (35%)": {
        "☀️ Net Zero (Solar + High Insulation)": 100,
        "💡 Energy Star Certified / LED / Inverters": 80,
        "🔌 Standard Grid Power": 50,
        "🥵 Poor Insulation / Old Appliances": 20
    },
    "Water (15%)": {
        "💧 Full Greywater Recycling System": 100,
        "🌧️ Rainwater Harvesting Tanks": 80,
        "🚿 Water-Saving Fixtures (Low-flow)": 60,
        "🚰 Standard Water System": 40
    }
}

WEIGHTS = {"Materials": 0.30, "Ecology": 0.20, "Energy": 0.35, "Water": 0.15}

# 2. APP UI
st.title("🌿 Green Building Sustainability Scorer")
st.markdown("Assess your building's environmental impact based on global standards.")

# Building Name
building_name = st.text_input("Project Name", value="Eco-Tower Bangkok")

st.divider()

# Creating two columns for the dropdowns
col1, col2 = st.columns(2)

with col1:
    m_choice = st.selectbox("Select Materials Standard", options=list(STANDARDS["Materials (30%)"].keys()))
    g_choice = st.selectbox("Select Ecology Standard", options=list(STANDARDS["Ecology (20%)"].keys()))

with col2:
    e_choice = st.selectbox("Select Energy Standard", options=list(STANDARDS["Energy (35%)"].keys()))
    w_choice = st.selectbox("Select Water Standard", options=list(STANDARDS["Water (15%)"].keys()))

# 3. CALCULATIONS
m_score = STANDARDS["Materials (30%)"][m_choice]
g_score = STANDARDS["Ecology (20%)"][g_choice]
e_score = STANDARDS["Energy (35%)"][e_choice]
w_score = STANDARDS["Water (15%)"][w_choice]

final_score = (m_score * WEIGHTS["Materials"]) + \
              (g_score * WEIGHTS["Ecology"]) + \
              (e_score * WEIGHTS["Energy"]) + \
              (w_score * WEIGHTS["Water"])

# 4. DISPLAY RESULTS
st.divider()
st.subheader(f"Results for: {building_name}")

# Metrics
c1, c2 = st.columns(2)
c1.metric("Final Sustainability Score", f"{final_score:.2f} / 100")

if final_score >= 80:
    level, color, icon = "PLATINUM (Global Leader)", "green", "🏆"
elif final_score >= 60:
    level, color, icon = "GOLD (Innovator)", "orange", "🥇"
elif final_score >= 40:
    level, color, icon = "SILVER (Standard)", "blue", "🥈"
else:
    level, color, icon = "CERTIFIED (Baseline)", "gray", "🥉"

c2.markdown(f"### Rating: {icon} :{color}[{level}]")

# Visual Chart (Comparison)
st.write("### Category Breakdown")
chart_data = pd.DataFrame({
    'Category': ['Materials', 'Ecology', 'Energy', 'Water'],
    'Score': [m_score, g_score, e_score, w_score]
})
st.bar_chart(chart_data.set_index('Category'))

# Sidebar Info
st.sidebar.header("How it's calculated")
st.sidebar.info(f"""
The score is a weighted average:
- **Energy:** {WEIGHTS['Energy']*100}%
- **Materials:** {WEIGHTS['Materials']*100}%
- **Ecology:** {WEIGHTS['Ecology']*100}%
- **Water:** {WEIGHTS['Water']*100}%
""")
