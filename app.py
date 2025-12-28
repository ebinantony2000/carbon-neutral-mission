import streamlit as st
import matplotlib.pyplot as plt
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Carbon Neutral Mission",
    page_icon="🌱",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.title("🌱 Carbon Neutral Mission")
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Carbon Calculator", "Solutions", "Our Team"]
)

# ================= HOME =================
if page == "Home":
    st.title("🌍 Carbon Neutral Mission")
    st.subheader("Towards a Carbon Neutral Community")

    st.markdown("""
    The *Carbon Neutral Mission* aims to assess and reduce household
    carbon emissions by promoting sustainable practices.

    This platform helps citizens understand their *carbon footprint*
    and take informed climate-friendly actions.
    """)

# ================= CALCULATOR =================
elif page == "Carbon Calculator":

    st.title("🏠 Household Carbon Footprint Calculator")

    # ---------- HOUSE DETAILS ----------
    st.subheader("House Details")
    house_name = st.text_input("House Name")
    owner_name = st.text_input("Owner Name")
    house_no = st.text_input("House Number")
    family_members = st.number_input("Family Members", min_value=1, value=1)

    # ---------- ELECTRICITY & COOKING ----------
    st.subheader("Electricity & Cooking")
    electricity_units = st.number_input("Monthly Grid Electricity Units", min_value=0, value=150)
    solar_units = st.number_input("Monthly Solar Units", min_value=0, value=0)
    lpg_cylinders = st.number_input("LPG Cylinders per Month", min_value=0, value=1)

    # ---------- WATER & TRANSPORT ----------
    st.subheader("Water & Transport")
    water_day = st.number_input("Water Usage per Day (litres)", min_value=0, value=100)

    bus = st.number_input("Monthly Bus Travel per Person (km)", min_value=0, value=0)
    train = st.number_input("Monthly Train Travel per Person (km)", min_value=0, value=0)
    tw = st.number_input("Monthly Two-wheeler / Car Travel per Person (km)", min_value=0, value=0)
    flight = st.number_input("Monthly Flight Travel per Person (km)", min_value=0, value=0)

    # ---------- WASTE & DIGITAL ----------
    st.subheader("Waste & Digital Usage")
    bio_waste = st.number_input("Biodegradable Waste (kg/day)", min_value=0, value=1)
    nonbio_waste = st.number_input("Non-biodegradable Waste (kg/day)", min_value=0, value=1)
    mobiles = st.number_input("Number of Mobile Phones", min_value=0, value=1)
    ewaste = st.number_input("E-waste Items per Year", min_value=0, value=1)

    # ---------- GREEN OFFSET ----------
    st.subheader("Green Actions")
    trees = st.number_input("Trees Maintained / Planted", min_value=0, value=0)

    # ---------- CALCULATION ----------
    if st.button("Calculate Carbon Footprint"):

        net_units = max(electricity_units - solar_units, 0)
        electricity_CO2 = net_units * 0.82 * 12
        cooking_CO2 = lpg_cylinders * 42 * 12
        water_CO2 = water_day * 0.0003 * 365
        transport_CO2 = (bus*0.05 + train*0.04 + tw*0.12 + flight*0.15) * 12 * family_members
        waste_CO2 = (bio_waste*0.18 + nonbio_waste*0.35) * 365
        digital_CO2 = mobiles*25 + ewaste*15
        offset = trees * 21

        gross_CO2 = (
            electricity_CO2 + cooking_CO2 + water_CO2 +
            transport_CO2 + waste_CO2 + digital_CO2
        )

        net_CO2 = gross_CO2 - offset
        per_capita = net_CO2 / family_members

        labels = ["Electricity", "Cooking", "Water", "Transport", "Waste", "Digital"]
        values = [electricity_CO2, cooking_CO2, water_CO2, transport_CO2, waste_CO2, digital_CO2]

        highest_source = labels[values.index(max(values))]

        suggestions = {
            "Electricity": "Use LED bulbs and adopt solar power.",
            "Cooking": "Reduce LPG usage and switch to induction cooking.",
            "Water": "Install rainwater harvesting systems.",
            "Transport": "Use public transport or car pooling.",
            "Waste": "Compost biodegradable waste and recycle plastics.",
            "Digital": "Reduce device replacement and recycle e-waste."
        }

        # ---------- RESULTS ----------
        st.subheader("📊 Carbon Footprint Results")
        st.write(f"*Gross CO₂ Emission:* {gross_CO2:.1f} kg/year")
        st.write(f"*Green Offset:* {offset:.1f} kg/year")
        st.write(f"*Net CO₂ Emission:* {net_CO2:.1f} kg/year")
        st.write(f"*Per Capita CO₂:* {per_capita:.1f} kg/year")
        st.write(f"*Highest Emission Source:* {highest_source}")
        st.write(f"*Suggested Action:* {suggestions[highest_source]}")

        # ---------- BAR CHART ----------
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_ylabel("CO₂ Emission (kg/year)")
        ax.set_title("Household Carbon Emission Breakdown")
        st.pyplot(fig)

        # ---------- PDF REPORT ----------
       # ---------- PERCENTAGE CONTRIBUTION ----------
        percent = {
            "Electricity": (electricity_CO2 / gross_CO2) * 100,
            "Cooking": (cooking_CO2 / gross_CO2) * 100,
            "Water": (water_CO2 / gross_CO2) * 100,
            "Transport": (transport_CO2 / gross_CO2) * 100,
            "Waste": (waste_CO2 / gross_CO2) * 100,
            "Digital": (digital_CO2 / gross_CO2) * 100,
        }

        # ---------- RATING ----------
        if net_CO2 < 3000:
            rating = "LOW CARBON HOUSEHOLD"
            rating_color = "green"
        elif net_CO2 < 6000:
            rating = "MODERATE CARBON HOUSEHOLD"
            rating_color = "orange"
        else:
            rating = "HIGH CARBON HOUSEHOLD"
            rating_color = "red"

        # ---------- PDF REPORT ----------
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Title
        story.append(Paragraph("<b>HOUSEHOLD CARBON EMISSION REPORT</b>", styles["Title"]))
        story.append(Spacer(1, 12))

        # Section 1: House Information
        story.append(Paragraph("<b>1. House Information</b>", styles["Heading2"]))
        story.append(Paragraph(f"House Name: {house_name}", styles["Normal"]))
        story.append(Paragraph(f"Owner Name: {owner_name}", styles["Normal"]))
        story.append(Paragraph(f"House Number: {house_no}", styles["Normal"]))
        story.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y')}", styles["Normal"]))
        story.append(Spacer(1, 10))

        # Section 2: Annual Carbon Emissions
        story.append(Paragraph("<b>2. Annual Carbon Emissions (kg/year)</b>", styles["Heading2"]))
        story.append(Paragraph(f"Electricity: {electricity_CO2:.2f}", styles["Normal"]))
        story.append(Paragraph(f"Cooking: {cooking_CO2:.2f}", styles["Normal"]))
        story.append(Paragraph(f"Water: {water_CO2:.2f}", styles["Normal"]))
        story.append(Paragraph(f"Transport: {transport_CO2:.2f}", styles["Normal"]))
        story.append(Paragraph(f"Waste: {waste_CO2:.2f}", styles["Normal"]))
        story.append(Paragraph(f"Digital: {digital_CO2:.2f}", styles["Normal"]))
        story.append(Spacer(1, 10))

        # Section 3: Emission Contribution
        story.append(Paragraph("<b>3. Emission Contribution (%)</b>", styles["Heading2"]))
        for key, value in percent.items():
            story.append(Paragraph(f"{key}: {value:.2f} %", styles["Normal"]))

        story.append(Spacer(1, 10))
        story.append(Paragraph(f"<b>Net CO₂ Emissions:</b> {net_CO2:.2f} kg/year", styles["Normal"]))
        story.append(Spacer(1, 6))

        # Colored rating line
        story.append(
            Paragraph(
                f'<font color="{rating_color}"><b>Overall Rating: {rating}</b></font>',
                styles["Normal"]
            )
        )
        story.append(Spacer(1, 10))

        # Section 4: Key Suggestion
        story.append(Paragraph("<b>4. Key Suggestion</b>", styles["Heading2"]))
        story.append(Paragraph(suggestions[highest_source], styles["Normal"]))
        story.append(Spacer(1, 10))

        # Section 5: Conclusion
        story.append(Paragraph("<b>5. Conclusion</b>", styles["Heading2"]))
        story.append(
            Paragraph(
                "This assessment highlights the household’s carbon emission pattern. "
                "By adopting sustainable practices and reducing high-emission activities, "
                "the household can significantly contribute towards achieving carbon neutrality "
                "and combating climate change.",
                styles["Normal"]
            )
        )

        doc.build(story)
        buffer.seek(0)

        st.download_button(
            "📥 Download PDF Report",
            buffer,
            "Household_Carbon_Report.pdf",
            "application/pdf"
        )

# ================= SOLUTIONS =================
elif page == "Solutions":
    st.title("🌿 Carbon Reduction Solutions")
    st.markdown("""
    - Use energy-efficient appliances  
    - Adopt renewable energy  
    - Reduce water wastage  
    - Use sustainable transport  
    - Practice waste segregation  
    - Plant trees regularly  
    """)

# ================= TEAM =================
elif page == "Our Team":
    st.title("👥 Project Team")
    st.markdown("""
    *TKM College of Engineering – Civil Engineering*

    - Athullya PR  
    - Ebin Antony  
    - Prathul K  
    - Anupama Raj  
    - Jareesh IS  
    - Shamil AN  
    """)
