import streamlit as st
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

st.set_page_config(page_title="Carbon Neutral Mission", layout="wide")

st.sidebar.title("🌱 Carbon Neutral Mission")
page = st.sidebar.radio("Navigation", ["Home", "Carbon Calculator"])


# ---------------- HOME PAGE ----------------
if page == "Home":
    st.title("🌍 Carbon Neutral Mission")

    st.markdown("""
    ### A Socially Relevant Engineering Project

    *TKM College of Engineering – Civil Engineering*

    *Team Members*
    - Athullya PR  
    - Ebin Antony  
    - Prathul K  
    - Anupama Raj  
    - Jareesh IS  
    - Shamil AN  
    """)


# ---------------- CALCULATOR PAGE ----------------
if page == "Carbon Calculator":

    st.title("🏠 Household Carbon Footprint Calculator")

    house_name = st.text_input("House Name")
    owner_name = st.text_input("Owner Name")
    house_number = st.text_input("House Number")
    members = st.number_input("Family Members", min_value=1, step=1)

    electricity = st.number_input("Monthly Electricity (kWh)", min_value=0.0)
    cooking_gas = st.number_input("Monthly Cooking Gas (kg)", min_value=0.0)
    water = st.number_input("Monthly Water Usage (litres)", min_value=0.0)
    transport = st.number_input("Monthly Transport Distance (km)", min_value=0.0)

    if st.button("Calculate Carbon Footprint"):

        electricity_co2 = electricity * 12 * 0.82
        cooking_co2 = cooking_gas * 12 * 3.0
        water_co2 = water * 12 * 0.0003
        transport_co2 = transport * 12 * 0.21

        total_co2 = electricity_co2 + cooking_co2 + water_co2 + transport_co2
        per_capita = total_co2 / members

        st.success(f"Total CO₂ Emission: {total_co2:.2f} kg/year")
        st.info(f"Per Capita CO₂: {per_capita:.2f} kg/year")

        categories = ["Electricity", "Cooking", "Water", "Transport"]
        values = [electricity_co2, cooking_co2, water_co2, transport_co2]

        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_ylabel("kg CO₂ / year")
        ax.set_title("Carbon Emission Breakdown")

        st.pyplot(fig)

        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)

        pdf.drawString(50, 800, "HOUSEHOLD CARBON EMISSION REPORT")
        pdf.drawString(50, 760, f"House Name: {house_name}")
        pdf.drawString(50, 740, f"Owner Name: {owner_name}")
        pdf.drawString(50, 720, f"House Number: {house_number}")
        pdf.drawString(50, 700, f"Total CO₂: {total_co2:.2f} kg/year")

        pdf.save()
        buffer.seek(0)

        st.download_button(
            "Download PDF Report",
            buffer,
            "Carbon_Report.pdf",
            "application/pdf"
        )
