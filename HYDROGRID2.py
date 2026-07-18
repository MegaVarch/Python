import streamlit as st
import time
import random

st.set_page_config(page_title="HydroGrid", layout="centered")

st.title("💧 HydroGrid")
st.subheader("Smart Community Water Management")

rain = st.empty()
humidity = st.empty()
solar = st.empty()
tank = st.empty()
flow = st.empty()
progress = st.progress(0)

for i in range(101):

    rain.markdown("### 🌧️ Rainwater Harvesting")
    humidity.metric("🌫️ Humidity", f"{random.randint(60,90)} %")
    solar.metric("☀️ Solar Efficiency", f"{random.randint(85,100)} %")
    tank.metric("🛢️ Tank Level", f"{i}%")

    progress.progress(i)

    if i < 30:
        flow.markdown("""
☁️ Clouds

⬇️⬇️⬇️

🌧️ Rain

⬇️

🛢️ Tank
""")

    elif i < 70:
        flow.markdown("""
☁️ Clouds

⬇️

🌧️ Rain

⬇️

🛢️ Tank

⬇️

🚿 Filter
""")

    else:
        flow.markdown("""
☁️ Clouds

⬇️

🌧️ Rain

⬇️

🛢️ Tank

⬇️

🚿 Filter

⬇️

🏠🏠🏠 Houses

🚰 Water Supplied
""")

    time.sleep(0.08)

st.success("✅ HydroGrid Successfully Distributed Water!")