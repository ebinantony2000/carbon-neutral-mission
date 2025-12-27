import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Carbon Neutral Mission",
    layout="wide"
)

# ---------- SIDEBAR NAVIGATION ----------
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Carbon Calculator", "Solutions", "Our Team"]
)

# ---------- HOME PAGE ----------
if page == "Home":
    st.title("🌱 Carbon Neutral Mission")
    st.subheader("A Socially Relevant Project")

    st.markdown("""
    ### 🌍 About the Project
    The *Carbon Neutral Mission* aims to assess and reduce
    household carbon emissions by promoting sustainable practices.

    This web platform helps users understand their *carbon footprint*
    and encourages eco-friendly lifestyle choices.
    """)

    st.markdown("""
    ### 🎯 Objectives
    - Measure household carbon emissions  
    - Create awareness about sustainability  
    - Promote carbon-neutral living  
    - Support climate action initiatives  
    """)

# ---------- CALCULATOR PAGE ----------
if page == "Calculator":

    st.header("🏠 Household Carbon Footprint Calculator")

    house_name = st.text_input("House Name")
    owner_name = st.text_input("Owner Name")
    house_number = st.text_input("House Number")
    members = st.number_input("Number of family members", min_value=1, step=1)

    electricity = st.number_input("Monthly electricity consumption (kWh)", min_value=0.0)
    cooking_gas = st.number_input("Monthly cooking gas usage (kg)", min_value=0.0)
    water = st.number_input("Monthly water usage (litres)", min_value=0.0)
    transport = st.number_input("Monthly transport distance (km)", min_value=0.0)

    electricity_co2 = electricity * 12 * 0.82
    cooking_co2 = cooking_gas * 12 * 3.0
    water_co2 = water * 12 * 0.0003
    transport_co2 = transport * 12 * 0.21

    total_co2 = electricity_co2 + cooking_co2 + water_co2 + transport_co2

    if st.button("Calculate Carbon Footprint"):

        st.success(f"🌍 Total Annual Carbon Emission: *{total_co2:.2f} kg CO₂/year*")

        per_capita = total_co2 / members
        st.info(f"👤 Per Capita Emission: *{per_capita:.2f} kg CO₂/year*")

        if total_co2 < 2000:
            st.success("🌱 LOW CARBON HOUSEHOLD")
        elif total_co2 < 5000:
            st.warning("🟡 MODERATE CARBON HOUSEHOLD")
        else:
            st.error("🔴 HIGH CARBON HOUSEHOLD")

        st.markdown("### 📊 Category-wise CO₂ Emissions")

        categories = ["Electricity", "Cooking", "Water", "Transport"]
        values = [electricity_co2, cooking_co2, water_co2, transport_co2]

        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_ylabel("CO₂ Emission (kg/year)")
        ax.set_title("Household Carbon Emission Breakdown")

        st.pyplot(fig)
# ---------- SOLUTIONS PAGE ----------
elif page == "Solutions":
    st.title("🌿 Carbon Reduction Solutions")

    st.markdown("""
    ### Simple Actions for a Low-Carbon Lifestyle
    - Use LED bulbs and energy-efficient appliances  
    - Reduce LPG usage and adopt induction cooking  
    - Use public transport, cycling, or carpooling  
    - Practice rainwater harvesting  
    - Compost biodegradable waste  
    - Plant and maintain trees  
    """)

# ---------- TEAM PAGE ----------
elif page == "Our Team":
    st.title("👥 Project Team")

    st.markdown("""
    *TKM College of Engineering*  
    Department of Civil Engineering  

    *Team Members*
    - Athullya PR  
    - Ebin Antony  
    - Prathul K  
    - Anupama Raj  
    - Jareesh IS  
    - Shamil AN  
    """)

    st.markdown("---")
    st.caption("© 2025 Carbon Neutral Mission | Civil Engineering | TKMCE")

  
