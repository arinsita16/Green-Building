This Streamlit application is a professional-grade calculator designed to evaluate the sustainability of a building project based on LEED-inspired criteria. 

Here is a step-by-step breakdown of how the code functions:

---

### 1. Setup & Standards
The first section defines the logic and the "brain" of the application.

* **`st.set_page_config`**: Sets the browser tab title and the emoji icon you see in the browser tab.
* **The `STANDARDS` Dictionary**: This is a nested data structure. Each category (Materials, Ecology, etc.) contains specific "levels" and their corresponding numeric scores (0–100). This acts as your database.
* **The `WEIGHTS` Dictionary**: Not all categories are equal. Energy (35%) has a bigger impact on the final score than Water (15%). These decimals represent the multipliers used in the final math.

### 2. User Interface (UI)
This section handles everything the user sees and interacts with.

* **`st.title` & `st.markdown`**: These create the header and the descriptive text at the top of the page.
* **`st.text_input`**: Allows the user to type in their project name. It defaults to "Eco-Tower Bangkok".
* **`st.columns(2)`**: This splits the screen into two vertical panes (`col1` and `col2`) so the dropdown menus don't take up too much vertical space.
* **`st.selectbox`**: These create the dropdown menus. 
    * `options=list(STANDARDS["..." ].keys())` tells Streamlit to look at the keys (the text descriptions) in your standards dictionary and show them as choices.

---

### 3. Calculations
Once the user makes a selection, the app needs to turn those words back into numbers.

* **Mapping**: `m_score = STANDARDS["Materials (30%)"][m_choice]` looks up the score associated with the user’s choice. For example, if the user picks "Locally Sourced," it finds the number **75**.
* **Weighted Average Formula**:
    $$Final\ Score = \sum (Category\ Score \times Category\ Weight)$$
    The code multiplies each score by its weight (e.g., $75 \times 0.30$) and adds them together to get a final value out of 100.

---

### 4. Results & Logic
This part interprets the data and makes it "pretty" for the user.

* **`st.metric`**: Displays the final score in a large, easy-to-read font.
* **Conditional Logic (`if/elif/else`)**: This determines the "medal" status.
    * **Platinum**: $\geq 80$
    * **Gold**: $\geq 60$
    * **Silver**: $\geq 40$
    * **Certified**: $< 40$
* **`st.bar_chart`**: Streamlit takes the `chart_data` (a Pandas DataFrame) and automatically generates an interactive bar graph showing how each category performed.

---

### 5. Sidebar
* **`st.sidebar`**: This moves content to the left-hand panel of the screen. It’s used here for "instructional" content so it doesn't clutter the main results area. It uses an **f-string** (the `f"""..."""` part) to inject the weight values directly into the text.

### Summary of Data Flow
1.  **Input:** User selects options in the UI.
2.  **Processing:** App retrieves values from the `STANDARDS` dictionary and applies `WEIGHTS`.
3.  **Output:** App displays a metric, a color-coded rating, and a bar chart.
