import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(
    page_title="HydroGrid Dashboard",
    page_icon="💧",
    layout="wide"
)

st.title("💧 HydroGrid Smart Water Management System")
st.subheader("Community Water Monitoring Dashboard")

placeholder = st.empty()

while True:

    humidity = random.randint(45,95)
    rain_tank = random.randint(30,100)
    grey_tank = random.randint(20,90)
    solar = random.choice(["ON ☀️","OFF 🌙"])
    awg = random.choice(["ACTIVE","STANDBY"])
    quality = random.choice(["GOOD","VERY GOOD","EXCELLENT"])
    water_today = random.randint(120,450)

    if rain_tank < 30:
        pump = "OFF"
        status = "⚠ Low Water Level"
    else:
        pump = "ON"
        status = "✅ System Normal"

    with placeholder.container():

        st.header("Live Sensor Data")

        c1,c2,c3,c4 = st.columns(4)

        c1.metric("Humidity",f"{humidity}%")
        c2.metric("Rainwater Tank",f"{rain_tank}%")
        c3.metric("Greywater Tank",f"{grey_tank}%")
        c4.metric("Water Produced",f"{water_today} L")

        st.divider()

        c5,c6,c7,c8 = st.columns(4)

        c5.metric("Solar Power",solar)
        c6.metric("AWG Unit",awg)
        c7.metric("Pump",pump)
        c8.metric("Water Quality",quality)

        st.divider()

        st.subheader("Tank Levels")

        st.write("Rainwater Tank")
        st.progress(rain_tank)

        st.write("Greywater Tank")
        st.progress(grey_tank)

        st.write("Humidity")
        st.progress(humidity)

        st.divider()

        st.success(status)

        st.caption("Last Updated : " + datetime.now().strftime("%H:%M:%S"))

    time.sleep(2)