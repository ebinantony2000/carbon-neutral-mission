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
    st.info("Carbon calculator will be added in the next step.")

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

  
