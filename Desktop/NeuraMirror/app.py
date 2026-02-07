import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NeuraMirror",
    page_icon="🧠",
    layout="centered"
)
# ---------------- SIDEBAR AUTHOR ----------------
st.sidebar.markdown("## 👨‍💻 Author")
st.sidebar.markdown("**Suranjan Chaudhari**")
st.sidebar.markdown("AIML Student · India 🇮🇳")
st.sidebar.markdown("[GitHub Profile](https://github.com/suranjan2006)")
# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
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

# ---------------- INPUT ----------------
st.subheader("Tell Neura about your daily habits")

screen_time = st.slider("📱 Screen Time (hours/day)", 0, 15, 5)
social_time = st.slider("📲 Social Media Time (hours)", 0, 10, 3)
study_time = st.slider("📚 Study / Work Hours", 0, 12, 4)
sleep_time = st.slider("😴 Sleep Hours", 0, 12, 7)
stress = st.slider("😰 Stress Level (1–10)", 1, 10, 5)

# ---------------- LOTTIE LOADER ----------------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

LOTTIE = {
    "healthy": "https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json",
    "warning": "https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json",
    "danger": "https://assets9.lottiefiles.com/packages/lf20_tutvdkg0.json"
}

# ---------------- ANALYSIS ----------------
if st.button("🔍 Analyze Me"):
    with st.spinner("Neura is thinking..."):
        time.sleep(2)

    score = screen_time + social_time + stress - sleep_time

    st.markdown("---")
    st.subheader("🧠 AI Reflection")

    # ---------- HEALTHY ----------
    if score < 10:
        st_lottie(load_lottie_url(LOTTIE["healthy"]), height=260)
        st.success("Your digital balance looks healthy 🌱")

        st.markdown("""
        **What you're doing right:**
        - Balanced screen usage  
        - Good sleep routine  
        - Stress under control  

        **Suggestions to maintain this:**
        - Keep sleep ≥ 7 hours  
        - Take screen breaks every 60–90 minutes  
        """)

    # ---------- WARNING ----------
    elif score < 18:
        st_lottie(load_lottie_url(LOTTIE["warning"]), height=260)
        st.warning("You’re drifting toward overload ⚠️")

        st.markdown("""
        **What needs attention:**
        - Screen or social media time is increasing  
        - Stress is slowly building  

        **Suggested improvements:**
        - Reduce social media by 30–45 minutes  
        - Add one offline activity daily  
        - Sleep at consistent time  
        """)

    # ---------- DANGER ----------
    else:
        st_lottie(load_lottie_url(LOTTIE["danger"]), height=260)
        st.error("High digital strain detected 🚨")

        st.markdown("""
        **Critical habits to change:**
        - Excessive screen & social media usage  
        - Poor sleep  
        - High stress levels  

        **Immediate actions:**
        - Digital detox before sleep  
        - Limit social media strictly  
        - Add physical movement  
        - Consider mindfulness / breathing  
        """)

    st.markdown("""
    <p style="text-align:center; opacity:0.7;">
    Neura doesn’t judge you. It reflects you.
    </p>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; opacity:0.7; font-size:14px;">
        <p>🧠 Built with ❤️ by <b>Suranjan Chaudhari</b></p>
        <p>AIML Student · India 🇮🇳</p>
        <p>
            <a href="https://github.com/suranjan2006" target="_blank"
               style="color:#58a6ff; text-decoration:none;">
               GitHub
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
