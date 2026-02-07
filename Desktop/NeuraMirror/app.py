from streamlit_lottie import st_lottie
import json
import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NeuraMirror",
    page_icon="🧠",
    layout="centered"
)

# ---------------- ANIMATED BACKGROUND ----------------
def animated_background():
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

    button {
        transition: transform 0.2s ease;
    }

    button:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

animated_background()

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center;'>🧠 Neura Mirror</h1>
<h4 style='text-align:center; opacity:0.8;'>
Your digital habits. Reflected by AI.
</h4>
<hr>
""", unsafe_allow_html=True)

# ---------------- USER INPUT ----------------
st.subheader("Tell Neura about your daily habits")

screen_time = st.slider("📱 Screen Time (hours/day)", 0, 15, 5)
social_media = st.slider("📲 Social Media Time (hours)", 0, 10, 3)
study_hours = st.slider("📚 Study / Work Hours", 0, 12, 4)
sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 7)
stress_level = st.slider("😰 Stress Level (1–10)", 1, 10, 5)

# ---------------- AI CHARACTER ----------------
def load_lottie(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Animation file not found: {path}")
        return None
def ai_character(state):
    if state == "healthy":
        anim = load_lottie("assets/ai_calm.json")
        msg = "Your digital balance looks healthy. Keep it up 🌱"
    elif state == "warning":
        anim = load_lottie("assets/ai_warning.json")
        msg = "You’re drifting toward overload. Small changes help ⚠️"
    else:
        anim = load_lottie("assets/ai_danger.json")
        msg = "High digital strain detected. Pause. Breathe. Reset 🚨"

    if anim:
    st_lottie(anim, height=260, key=state)
    st.markdown(f"<h3 style='text-align:center'>{msg}</h3>", unsafe_allow_html=True)


# ---------------- ANALYSIS ----------------
st.markdown("<br>", unsafe_allow_html=True)

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