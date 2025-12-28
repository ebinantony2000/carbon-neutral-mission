import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import datetime
import matplotlib.pyplot as plt
import io

# ================== WEBSITE HEADER ==================
st.set_page_config(page_title="Carbon Neutral Mission", page_icon="🌱", layout="wide")
st.title("🌱 Carbon Neutral Mission")
st.subheader("Towards a Carbon Neutral Community")
st.sidebar.header("Project Team")
st.sidebar.write("*TKM College of Engineering - Civil Engineering*")
st.sidebar.write("Athullya PR") 
st.sidebar.write("Ebin Antony")
st.sidebar.write("Prathul K")
st.sidebar.write("Anupama Raj")
st.sidebar.write("Jareesh IS")
st.sidebar.write("Shamil AN")

# ================== NAVIGATION ==================
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Carbon Calculator", "Why Carbon Neutral?", "Solutions", "Our Team"]
)

# ================== HOME PAGE ==================
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>🌱 Carbon Neutral Mission</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Towards a Sustainable & Low-Carbon Future</h4>", unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
        use_column_width=True,
        caption="Protecting the planet starts at home"
    )

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌍 About the Project")
        st.write("""
        The *Carbon Neutral Mission* is a socially relevant initiative aimed at
        measuring and reducing *household carbon emissions*.
        This platform helps families understand their *carbon footprint*
        and encourages sustainable living practices.
        """)
    with col2:
        st.subheader("🎯 Project Objectives")
        st.markdown("""
        - Assess household carbon emissions  
        - Promote awareness on climate change  
        - Encourage eco-friendly lifestyle choices  
        - Support carbon-neutral community initiatives  
        """)
    st.divider()
    st.subheader("💡 Why Carbon Neutrality Matters?")
    st.write("""
    Carbon emissions from households contribute significantly to climate change.
    By adopting *energy-efficient, water-conserving, and low-carbon practices*,
    communities can reduce environmental impact and move towards a *sustainable future*.
    """)
    st.info("🌿 Small changes at home can create a big impact on the planet.")

# ================== CALCULATOR PAGE ==================
elif page == "Carbon Calculator":
    st.title("🧮 Household Carbon Calculator")
    st.info("Estimate your annual household carbon footprint below.")

    # Inputs with icons
    house_name = st.text_input("🏠 House Name")
    owner_name = st.text_input("👤 Owner Name")
    house_no = st.text_input("🏷 House Number")
    family_members = st.number_input("👨‍👩‍👧‍👦 Number of Family Members", min_value=1, value=1)

    st.subheader("⚡ Electricity & Cooking")
    electricity_units = st.number_input("💡 Monthly Grid Electricity Units", min_value=0, value=150)
    solar_units = st.number_input("☀ Monthly Solar Units (if any)", min_value=0, value=0)
    lpg_cylinders = st.number_input("🔥 LPG Cylinders per Month", min_value=0, value=1)

    st.subheader("💧 Water & Transport")
    water_day = st.number_input("💧 Water Usage per Day (litres)", min_value=0, value=100)
    bus = st.number_input("🚌 Monthly Bus Travel per Person (km)", min_value=0, value=0)
    train = st.number_input("🚆 Monthly Train Travel per Person (km)", min_value=0, value=0)
    tw = st.number_input("🏍/🚗 Two-wheeler/Car Travel per Person (km)", min_value=0, value=0)
    flight = st.number_input("✈ Monthly Flight Travel per Person (km)", min_value=0, value=0)

    st.subheader("🗑 Waste & Digital")
    bio_waste = st.number_input("🌿 Biodegradable Waste kg/day", min_value=0, value=1)
    nonbio_waste = st.number_input("🗑 Non-biodegradable Waste kg/day", min_value=0, value=1)
    mobiles = st.number_input("📱 Number of Mobile Phones", min_value=0, value=1)
    ewaste = st.number_input("💻 E-Waste Items per Year", min_value=0, value=1)

    st.subheader("🌳 Green Actions")
    trees = st.number_input("🌳 Trees Maintained / Planted", min_value=0, value=0)

    # ---------------- CALCULATION & CHART ----------------
    if st.button("Calculate Carbon Footprint"):
        net_units = max(electricity_units - solar_units, 0)
        electricity_CO2 = net_units * 0.82 * 12
        cooking_CO2 = lpg_cylinders * 42 * 12
        water_CO2 = water_day * 0.0003 * 365
        transport_CO2 = (bus*0.05 + train*0.04 + tw*0.12 + flight*0.15) * 12 * family_members
        waste_CO2 = (bio_waste*0.18 + nonbio_waste*0.35) * 365
        digital_CO2 = mobiles*25 + ewaste*15
        offset = trees * 21
        gross_CO2 = electricity_CO2 + cooking_CO2 + water_CO2 + transport_CO2 + waste_CO2 + digital_CO2
        net_CO2 = gross_CO2 - offset
        per_capita = net_CO2 / family_members

        labels = ["Electricity", "Cooking", "Water", "Transport", "Waste", "Digital"]
        values = [electricity_CO2, cooking_CO2, water_CO2, transport_CO2, waste_CO2, digital_CO2]

        # Rating
        if net_CO2 < 3000:
            rating = "LOW CARBON HOUSEHOLD"
            color = "green"
        elif net_CO2 < 6000:
            rating = "MODERATE CARBON HOUSEHOLD"
            color = "orange"
        else:
            rating = "HIGH CARBON HOUSEHOLD"
            color = "red"

        st.metric("🌱 Net CO₂ Emission (kg/year)", f"{net_CO2:.1f}")
        st.metric("👤 Per Capita CO₂", f"{per_capita:.1f}")
        st.metric("🏆 Overall Rating", rating)

        # Bar chart
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=['green','orange','blue','red','brown','purple'])
        ax.set_ylabel("CO₂ Emission (kg/year)")
        ax.set_title("Household Carbon Emission Breakdown")
        st.pyplot(fig)

        # ---------------- PDF REPORT ----------------
       # ---------------- PDF REPORT ----------------
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import green, orange, red, black
import io

buffer = io.BytesIO()
doc = SimpleDocTemplate(buffer, pagesize=A4)
story = []
styles = getSampleStyleSheet()

# Custom style for colored rating
def get_rating_style(rating_text):
    if rating_text.startswith("LOW"):
        return ParagraphStyle('rating', parent=styles['Heading2'], textColor=green)
    elif rating_text.startswith("MODERATE"):
        return ParagraphStyle('rating', parent=styles['Heading2'], textColor=orange)
    else:
        return ParagraphStyle('rating', parent=styles['Heading2'], textColor=red)

# ----------------- CONTENT -----------------

# Heading
story.append(Paragraph("<b>HOUSEHOLD CARBON EMISSION REPORT</b>", styles["Title"]))
story.append(Spacer(1,12))

# Section 1: House Information
story.append(Paragraph("<b>HOUSE INFORMATION</b>", styles["Heading2"]))
story.append(Paragraph(f"House Name: {house_name}", styles["Normal"]))
story.append(Paragraph(f"Owner Name: {owner_name}", styles["Normal"]))
story.append(Paragraph(f"House Number: {house_no}", styles["Normal"]))
story.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y')}", styles["Normal"]))
story.append(Spacer(1,12))

# Section 2: Annual Carbon Emissions
story.append(Paragraph("<b>ANNUAL CARBON EMISSIONS (kg/year)</b>", styles["Heading2"]))
for i, label in enumerate(labels):
    story.append(Paragraph(f"{label}: {values[i]:.1f}", styles["Normal"]))
story.append(Spacer(1,6))
story.append(Paragraph(f"Net CO₂ Emissions: {net_CO2:.1f} kg/year", styles["Normal"]))
story.append(Spacer(1,12))

# Section 3: Emission Contribution (%)
story.append(Paragraph("<b>EMISSIONS CONTRIBUTION (%)</b>", styles["Heading2"]))
total = sum(values)
for i, label in enumerate(labels):
    story.append(Paragraph(f"{label}: {values[i]/total*100:.1f} %", styles["Normal"]))
story.append(Spacer(1,12))

# Overall Rating in color
story.append(Paragraph(f"Overall Rating: {rating}", get_rating_style(rating)))
story.append(Spacer(1,12))

# Section 4: Key Suggestion
story.append(Paragraph("<b>KEY SUGGESTION</b>", styles["Heading2"]))
suggestions = {
    "Electricity": "Adopt LED lighting and solar energy.",
    "Cooking": "Reduce LPG usage and switch to induction/biogas.",
    "Water": "Install rainwater harvesting systems.",
    "Transport": "Prefer public transport, cycling, or carpooling.",
    "Waste": "Compost bio-waste and recycle non-biodegradable waste.",
    "Digital": "Reduce frequent device replacement and recycle e-waste."
}
highest_source = labels[values.index(max(values))]
story.append(Paragraph(f"{highest_source}: {suggestions[highest_source]}", styles["Normal"]))
story.append(Spacer(1,12))

# Section 5: Conclusion
story.append(Paragraph("<b>CONCLUSION</b>", styles["Heading2"]))
story.append(Paragraph(
    "Measuring and reducing household carbon emissions is essential for "
    "a sustainable future. Following suggested actions can significantly "
    "reduce the carbon footprint of your home.", styles["Normal"]))

doc.build(story)
buffer.seek(0)

st.download_button(
    label="📥 Download PDF Report",
    data=buffer,
    file_name=f"Household_Carbon_Report_{house_name}.pdf",
    mime="application/pdf"
)
# ================== WHY CARBON NEUTRAL? ==================
elif page == "Why Carbon Neutral?":
    st.title("🌿 Why Carbon Neutral?")
    st.subheader("Understanding Carbon Footprint and Its Impact")
    st.image(
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
        use_column_width=True,
        caption="Every action at home counts towards the planet"
    )
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏠 Household Impact")
        st.write("""
        - Residential electricity & cooking fuels are major contributors  
        - Transportation adds significant emissions  
        - Waste management and e-waste affect carbon footprint  
        """)
    with col2:
        st.subheader("🌎 Global Context")
        st.write("""
        - Climate change is accelerated by CO₂ emissions  
        - Reducing household carbon footprint contributes to sustainability  
        - Small steps at home lead to measurable environmental benefits  
        """)
    st.divider()
    st.subheader("💡 Takeaway")
    st.info("Reducing household carbon emissions is a contribution to a sustainable future!")

# ================== SOLUTIONS ==================
elif page == "Solutions":
    st.title("🌿 Carbon Reduction Solutions")
    st.markdown("""
    ### Simple Actions for a Low-Carbon Lifestyle
    - 💡 Use LED bulbs and energy-efficient appliances  
    - 🔥 Reduce LPG usage and adopt induction/biogas  
    - 🚴‍♂ Use public transport, cycling, or carpooling  
    - 💧 Practice rainwater harvesting  
    - 🌿 Compost biodegradable waste  
    - 🌳 Plant and maintain trees  
    """)

# ================== TEAM ==================
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
    st.divider()
    st.caption("© 2025 Carbon Neutral Mission | Civil Engineering | TKMCE")
