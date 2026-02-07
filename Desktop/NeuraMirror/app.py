import time
import streamlit as st
from streamlit_lottie import st_lottie_url

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NeuraMirror",
    page_icon="🧠",
    layout="centered"
)

# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
    background-size: 400% 400%;
    animation: bgMove 20s ease infinite;
    color: white;
}
@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style="text-align:center;">🧠 NeuraMirror</h1>
<h4 style="text-align:center; opacity:0.8;">
Your digital habits. Reflected by AI.
</h4>
<hr>
""", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
st.subheader("Tell Neura about your daily habits")

screen_time = st.slider("📱 Screen Time (hours/day)", 0, 15, 5)
social_media = st.slider("📲 Social Media Time (hours)", 0, 10, 3)
study_hours = st.slider("📚 Study / Work Hours", 0, 12, 4)
sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 7)
stress_level = st.slider("😰 Stress Level (1–10)", 1, 10, 5)

# ---------------- AI CHARACTER ----------------
def ai_character(state):
    if state == "healthy":
        url = "https://assets9.lottiefiles.com/packages/lf20_jbrw3hcz.json"
        msg = "Your digital balance looks healthy. Keep it up 🌱"
    elif state == "warning":
        url = "https://assets9.lottiefiles.com/packages/lf20_touohxv0.json"
        msg = "You’re drifting toward overload. Small changes help ⚠️"
    else:
        url = "https://assets9.lottiefiles.com/packages/lf20_gz3t8c.json"
        msg = "High digital strain detected. Pause. Breathe. Reset 🚨"

    st_lottie_url(url, height=260)
    st.markdown(f"<h3 style='text-align:center'>{msg}</h3>", unsafe_allow_html=True)

# ---------------- ANALYSIS ----------------
if st.button("🔍 Analyze Me"):
    with st.spinner("Neura is thinking..."):
        time.sleep(2)

    score = screen_time + social_media + stress_level - sleep_hours

    st.markdown("---")
    st.subheader("🧠 AI Reflection")

    if score < 10:
        ai_character("healthy")
    elif score < 18:
        ai_character("warning")
    else:
        ai_character("danger")

    st.markdown("""
    <p style="text-align:center; opacity:0.7;">
    Neura doesn’t judge you. It reflects you.
    </p>
    """, unsafe_allow_html=True)
