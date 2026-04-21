This User Manual provides instructions on how to use the **Green Building Sustainability Scorer**, an interactive tool designed to evaluate the environmental impact of building projects based on global green standards (inspired by LEED).

---

# 🌿 Green Building Scorer: User Manual

## 1. Overview
The Green Building Scorer is a web-based application that allows architects, developers, and sustainability consultants to estimate a building's sustainability rating. By selecting specific standards for materials, energy, water, and ecology, the app calculates a weighted score and assigns a certification level.

## 2. Key Features
* **Real-time Scoring:** Instant calculation as you change your project parameters.
* **Weighted Assessment:** Factors in the relative importance of different environmental categories.
* **Visual Analytics:** A bar chart breakdown to identify areas for improvement.
* **Standardized Ratings:** Grading tiers from "Certified" to "Platinum."

---

## 3. How to Use the App

<img src="Screenshot 2026-04-21 201403.png" alt="App Screenshot 1" width="100%">

### Step 1: Project Identification
Enter the name of your project in the **Project Name** text field at the top of the page. This name will appear in the results summary.

### Step 2: Input Sustainability Data
The app is divided into four main categories. Use the dropdown menus to select the option that best describes your project:

| Category | Weight | Options Include |
| :--- | :--- | :--- |
| **Materials** | 30% | Recycled, Locally Sourced, Industrial, or High-Carbon. |
| **Energy** | 35% | Net Zero, Energy Star, Standard Grid, or Poor Insulation. |
| **Ecology** | 20% | Urban Forest, Rooftop Gardens, Basic Landscaping, or Paved. |
| **Water** | 15% | Greywater Recycling, Rainwater Tanks, Low-flow, or Standard. |

### Step 3: Review the Results
Once selections are made, scroll down to the **Results** section:
1.  **Final Sustainability Score:** A numeric value out of 100.
2.  **Rating Tier:** * 🏆 **PLATINUM (80+):** Global Leader in sustainability.
    * 🥇 **GOLD (60-79):** High-level innovator.
    * 🥈 **SILVER (40-59):** Meets baseline green standards.
    * 🥉 **CERTIFIED (<40):** Basic environmental compliance.

<img src="Screenshot 2026-04-21 201425.png" alt="App Screenshot 2" width="100%">

### Step 4: Analyze Category Breakdown
Review the **Category Breakdown** bar chart. This visual shows the raw score for each individual category, helping you see which area (e.g., Water or Energy) is the weakest link in your sustainability profile.

---

## 4. Technical Calculations
The app uses a weighted average formula to ensure that high-impact areas like **Energy** and **Materials** carry more weight than others.

**The Formula:**
$$Score = (Materials \times 0.30) + (Ecology \times 0.20) + (Energy \times 0.35) + (Water \times 0.15)$$

---

## 5. Troubleshooting & FAQ
* **The app isn't updating:** Streamlit apps update automatically. If it feels stuck, try refreshing your browser page.
* **Where is the data saved?** This is a calculator tool; data is processed in real-time and is not saved to a permanent database once the browser session is closed.
* **Can I change the weights?** The current version uses fixed weights based on international standards. Custom weight adjustments require a code-level update.

---
*Environmentally conscious building starts with better data. Use this tool to iterate on your design and reach for Platinum!*
