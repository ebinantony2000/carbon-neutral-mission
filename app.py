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
elif page == "Carbon Calculator":
    st.title("🧮 Household Carbon Calculator")

    st.markdown("### Basic Household Details")

    members = st.number_input("Number of family members", min_value=1, step=1)

    st.markdown("### ⚡ Electricity Usage")
    electricity = st.selectbox(
        "Monthly electricity consumption (units)",
        ["<100", "100–200", "200–300", "300–500", ">500"]
    )

    elec_units = {
        "<100": 75,
        "100–200": 150,
        "200–300": 250,
        "300–500": 400,
        ">500": 600
    }[electricity]

    electricity_co2 = elec_units * 0.82 * 12

    st.markdown("### 🍳 Cooking (LPG)")
    lpg = st.number_input("LPG cylinders per month", min_value=0.0, step=0.1)
    cooking_co2 = lpg * 42 * 12

    st.markdown("### 💧 Water Usage")
    water = st.number_input("Water usage per day (litres)", min_value=0.0)
    water_co2 = water * 0.0003 * 365

    st.markdown("### 🚗 Transport (per person per month)")
    bus = st.number_input("Bus travel (km)", min_value=0.0)
    tw = st.number_input("Two-wheeler / Car travel (km)", min_value=0.0)

    transport_co2 = (bus * 0.05 + tw * 0.12) * 12 * members

    # ---------- TOTAL ----------
    total_co2 = electricity_co2 + cooking_co2 + water_co2 + transport_co2

    st.markdown("---")
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

    # ---------- BAR CHART ----------
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

  
