
import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Ayurvedic Diet & Nutrition System",
    page_icon="🌿",
    layout="wide"
)

# Load images
example_img = Image.open("example.png")
arch_img = Image.open("architecture.png")

# Create two columns: left for navigation, right for content
col1, col2 = st.columns([1, 4])  # adjust width ratio as needed

# ---------------- Navigation Menu ----------------
with col1:
    st.markdown("## 🌿 Navigation")
    pages = ["Home", "Architecture", "Workflow Demo", "Research & References"]
    selection = st.radio("", pages)

# ---------------- Main Content ----------------
with col2:
    if selection == "Home":
        st.title("🌿 Ayurvedic Diet & Nutrition System")
        st.write("""
        This project combines **Ayurvedic principles** with **modern nutrient science** 
        to generate **personalized diet charts** for patients.  
        Doctors can review AI-generated recommendations before sharing with patients.  
        """)
        st.image(example_img, caption="Ayurvedic Nutrition Concept", width=350)

    elif selection == "Architecture":
        st.title("📊 System Architecture")
        st.image(arch_img, caption="Architecture Diagram", width=800)
        st.write("""
        The architecture integrates **Ayurvedic knowledge** with **nutritional databases** 
        and a **rule-based engine** for generating personalized diet recommendations.
        """)

    elif selection == "Workflow Demo":
        st.title("⚙️ Workflow Demo - Generate Your Diet Chart")

        # Collect user inputs
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=5, max_value=100, step=1)
        gender = st.radio("Select gender", ["Male", "Female", "Other"])
        dosha = st.selectbox("Select your dominant Dosha", ["Vata", "Pitta", "Kapha"])
        activity = st.selectbox("Activity level", ["Sedentary", "Moderate", "Active"])
        health_goal = st.selectbox("Health goal", ["Weight Loss", "Muscle Gain", "General Wellness", "Diabetes Management"])
        diet_pref = st.selectbox("Dietary preference", ["Vegetarian", "Vegan", "Non-Vegetarian"])
        allergies = st.text_area("Any allergies? (comma separated, e.g., milk, nuts)")

        if st.button("Generate Diet Chart"):
            st.subheader(f"🍽️ Personalized Diet Plan for {name}")

            # Example output diet chart (static rules for demo)
            diet_chart = {
                "Breakfast": "Oats with almonds, fruits, and herbal tea",
                "Mid-Morning": "Fresh fruit bowl with seasonal options",
                "Lunch": "Steamed rice, dal, mixed vegetable curry, and salad",
                "Evening": "Herbal tea with roasted chickpeas",
                "Dinner": "Millet roti, light soup, and stir-fried greens"
            }

            # Modify based on dosha
            if dosha == "Vata":
                diet_chart["Dinner"] = "Warm soups with ghee and soft-cooked grains"
            elif dosha == "Pitta":
                diet_chart["Lunch"] = "Cooling foods: cucumber raita, coconut water, and leafy greens"
            elif dosha == "Kapha":
                diet_chart["Breakfast"] = "Warm herbal tea, fruits, avoid oily foods"

            # Modify based on goal
            if health_goal == "Weight Loss":
                diet_chart["Evening"] = "Green tea with sprouts"
            elif health_goal == "Muscle Gain":
                diet_chart["Breakfast"] = "Protein-rich upma with sprouts"
            elif health_goal == "Diabetes Management":
                diet_chart["Lunch"] = "Millet khichdi with bitter gourd curry"

            # Show results
            for meal, items in diet_chart.items():
                st.markdown(f"**{meal}:** {items}")

            st.success("✅ This is a demo diet chart generated using Ayurvedic + Nutrient rules.")

    elif selection == "Research & References":
        st.title("📚 Research and References")
        st.write("""
        1. Problem & Opportunity  
        2. Core Ayurvedic Knowledge  
        3. Rath, S. K. et al., *The scientific basis of rasa (taste) as a tool in Ayurveda*  
        4. National Institute of Nutrition (ICMR), *Indian Food Composition Tables (IFCT), 2017*  
        5. Payyappallimana, U., *Exploring Ayurvedic knowledge on food and health — parallels with biomedicine*  
        6. Patwardhan, B., *Ayurveda and Systems Biology — A New Vision of Personalized Nutrition*  
        7. WHO Traditional Medicine Strategy (2025) — Encouraging integrative healthcare models  
        """)
