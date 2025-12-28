import streamlit as st

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
elif page == "Carbon Calculator":
    st.title("🧮 Carbon Calculator")

    st.subheader("House Details")
    house_name = st.text_input("House Name")
    owner_name = st.text_input("Owner Name")
    house_number = st.text_input("House Number")
    members = st.number_input("Number of Family Members", min_value=1, step=1)

    st.subheader("Monthly Consumption")
    electricity = st.number_input("Electricity (kWh)", min_value=0.0)
    cooking_gas = st.number_input("Cooking Gas (kg)", min_value=0.0)
    water = st.number_input("Water Usage (litres)", min_value=0.0)
    transport = st.number_input("Transport Distance (km)", min_value=0.0)

    if st.button("Calculate Carbon Footprint"):

        electricity_co2 = electricity * 12 * 0.82
        cooking_co2 = cooking_gas * 12 * 3.0
        water_co2 = water * 12 * 0.0003
        transport_co2 = transport * 12 * 0.21

        total_co2 = electricity_co2 + cooking_co2 + water_co2 + transport_co2
        per_capita = total_co2 / members

        st.success(f"🌍 Total Annual CO₂ Emission: {total_co2:.2f} kg/year")
        st.info(f"👤 Per Capita CO₂ Emission: {per_capita:.2f} kg/year")

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
