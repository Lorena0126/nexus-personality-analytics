
import streamlit as st
import time
import random

st.set_page_config(
    page_title="NEXUS // Personality Analytics",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #05070a;
    color: #e8edf2;
}
.block-container {
    max-width: 850px;
    padding-top: 3rem;
}
h1, h2, h3 {
    font-family: monospace;
    letter-spacing: 1px;
}
.system {
    font-family: monospace;
    color: #7df9ff;
    border: 1px solid #24444a;
    padding: 18px;
    border-radius: 8px;
    background: #071015;
}
.result {
    font-family: monospace;
    border: 1px solid #24444a;
    padding: 20px;
    border-radius: 8px;
    background: #071015;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="system">NEXUS // PERSONALITY ANALYTICS<br>'
    'CONFIDENTIAL BEHAVIORAL INTELLIGENCE SYSTEM<br>'
    'STATUS: ONLINE</div>',
    unsafe_allow_html=True
)

st.title("🧠 Personality Intelligence Dashboard")
st.caption("Behavioral pattern assessment — demonstration system")

name = st.text_input("SUBJECT IDENTIFICATION", placeholder="Enter your name")

questions = [
    ("When entering a new environment, how quickly do you adapt?", "adaptability"),
    ("How strongly do you enjoy learning completely new things?", "curiosity"),
    ("How comfortable are you making decisions under uncertainty?", "risk"),
    ("How easily can you understand another person's feelings?", "emotional"),
    ("How comfortable are you starting conversations with strangers?", "social"),
    ("How likely are you to change your plans when circumstances change?", "adaptability"),
    ("How often do you question information instead of accepting it immediately?", "curiosity"),
    ("How well do you stay calm when things go wrong?", "emotional"),
    ("How willing are you to try something unfamiliar?", "risk"),
    ("How easily can you work with people who have very different personalities?", "social"),
]

labels = [
    "1 — Very low",
    "2 — Low",
    "3 — Neutral",
    "4 — High",
    "5 — Very high"
]

if name:
    st.markdown("---")
    answers = []

    for i, (question, category) in enumerate(questions):
        answer = st.radio(
            f"{i+1:02d} // {question}",
            labels,
            horizontal=True,
            key=f"q{i}"
        )
        answers.append((category, labels.index(answer) + 1))

    if st.button("▶ RUN DEEP ANALYSIS", use_container_width=True):
        with st.spinner("INITIALIZING BEHAVIORAL MODEL..."):
            time.sleep(0.8)
            with st.spinner("PROCESSING RESPONSE MATRIX..."):
                time.sleep(0.8)

        scores = {
            "Emotional Intelligence": [],
            "Social Adaptability": [],
            "Risk Tolerance": [],
            "Curiosity": []
        }

        mapping = {
            "emotional": "Emotional Intelligence",
            "social": "Social Adaptability",
            "risk": "Risk Tolerance",
            "curiosity": "Curiosity",
            "adaptability": "Social Adaptability",
        }

        for category, value in answers:
            scores[mapping[category]].append(value)

        final = {}
        for key, values in scores.items():
            raw = sum(values) / len(values)
            final[key] = round(raw / 5 * 100)

        st.markdown("---")
        st.markdown("### ANALYSIS COMPLETE")

        cols = st.columns(4)
        for col, (key, value) in zip(cols, final.items()):
            col.metric(key, f"{value}%")

        avg = sum(final.values()) / len(final)

        if avg >= 85:
            classification = "HIGHLY ADAPTIVE PROFILE"
            text = "Your behavioral pattern indicates strong curiosity, flexibility, and environmental adaptability."
        elif avg >= 70:
            classification = "ADAPTIVE PROFILE"
            text = "Your responses indicate a balanced and generally flexible behavioral pattern."
        elif avg >= 55:
            classification = "MODERATELY ADAPTIVE PROFILE"
            text = "Your profile shows a mixture of stable preferences and situational flexibility."
        else:
            classification = "STABLE PROFILE"
            text = "Your responses suggest stronger preference for familiar environments and predictable situations."

        st.markdown(
            f'<div class="result"><b>CLASSIFICATION</b><br><br>'
            f'<span style="font-size:1.35rem;">{classification}</span><br><br>'
            f'"{text}"</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "NEXUS is a fictional demonstration system. "
            "This assessment is for entertainment and does not constitute a psychological diagnosis."
        )
