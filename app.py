
import streamlit as st
import time

st.set_page_config(
    page_title="NEXUS — Personality Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.stApp {
    background: #fcf8fa;
    color: #30272c;
}

.block-container {
    max-width: 1160px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}

/* Luxury header */
.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #fff 0%, #fff5f8 55%, #fce8ef 100%);
    border: 1px solid #ead3dc;
    border-radius: 28px;
    padding: 42px 46px;
    box-shadow: 0 18px 50px rgba(115, 55, 77, .08);
}

.hero:after {
    content: "N";
    position: absolute;
    right: 35px;
    top: -35px;
    font-family: 'Playfair Display', serif;
    font-size: 190px;
    color: rgba(213, 116, 147, .055);
    font-weight: 700;
}

.eyebrow {
    color: #b35a78;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.4px;
    text-transform: uppercase;
}

.logo {
    font-family: 'Playfair Display', Georgia, serif;
    color: #392b31;
    font-size: 43px;
    line-height: 1.1;
    margin-top: 10px;
    letter-spacing: .2px;
}

.tagline {
    color: #806b73;
    margin-top: 12px;
    font-size: 14px;
    max-width: 650px;
    line-height: 1.7;
}

.online {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    margin-top: 20px;
    color: #7c5363;
    font-size: 11px;
    letter-spacing: 1px;
    font-weight: 600;
}

.dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #c95d83;
    display: inline-block;
}

/* Sections */
.card {
    background: rgba(255,255,255,.96);
    border: 1px solid #ead7df;
    border-radius: 20px;
    padding: 26px;
    margin-top: 20px;
    box-shadow: 0 10px 30px rgba(115,55,77,.045);
}

.kicker {
    color: #ad5977;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
}

.heading {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 25px;
    color: #3c2c33;
    margin-top: 6px;
}

.muted {
    color: #89737c;
    font-size: 12px;
    line-height: 1.7;
    margin-top: 5px;
}

/* Score cards */
.score {
    background: linear-gradient(145deg, #fff 0%, #fff8fa 100%);
    border: 1px solid #efd5df;
    border-radius: 18px;
    padding: 19px;
    min-height: 118px;
}

.score-label {
    color: #967783;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.1px;
}

.score-number {
    color: #bf5278;
    font-size: 34px;
    font-weight: 700;
    margin-top: 8px;
}

/* Result */
.result {
    background: linear-gradient(135deg, #fff7fa, #fff);
    border: 1px solid #e6cbd6;
    border-radius: 22px;
    padding: 30px;
    margin-top: 20px;
}

.result-title {
    font-family: 'Playfair Display', Georgia, serif;
    color: #a7466c;
    font-size: 30px;
    margin-top: 7px;
}

.quote {
    color: #68535d;
    line-height: 1.8;
    font-size: 14px;
    margin-top: 12px;
}

/* Streamlit widgets */
div[data-baseweb="input"] > div {
    background: #fff !important;
    border: 1px solid #e6cbd5 !important;
    border-radius: 12px !important;
}

div[data-baseweb="input"] input {
    color: #332a2f !important;
    font-size: 14px !important;
}

.stTextInput label, .stSlider label {
    color: #58434c !important;
    font-weight: 600 !important;
}

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #c65b80;
}

.stButton > button {
    background: #bd5579;
    color: #fff;
    border: 1px solid #bd5579;
    border-radius: 12px;
    padding: 12px 18px;
    font-weight: 700;
    letter-spacing: .3px;
    box-shadow: 0 8px 20px rgba(189,85,121,.18);
}

.stButton > button:hover {
    background: #a94568;
    border-color: #a94568;
    color: #fff;
}

div[data-testid="stProgressBar"] > div > div {
    background: #c65b80;
}

.footer {
    text-align: center;
    color: #ae969f;
    font-size: 10px;
    margin-top: 32px;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="eyebrow">Nexus Intelligence · Behavioral Series 07</div>
    <div class="logo">Personality Intelligence</div>
    <div class="tagline">
        A refined behavioral-pattern experience designed to transform
        simple responses into a distinctive personality profile.
    </div>
    <div class="online"><span class="dot"></span> SYSTEM ONLINE · PRIVATE DEMO</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="kicker">01 · Subject</div>
    <div class="heading">Who are we analyzing?</div>
    <div class="muted">Enter a name to begin your private assessment.</div>
</div>
""", unsafe_allow_html=True)

name = st.text_input("SUBJECT NAME", placeholder="Your name", label_visibility="visible")

questions = [
    ("A new environment feels exciting rather than intimidating.", "adaptability"),
    ("You actively seek unfamiliar ideas, cultures, or subjects.", "curiosity"),
    ("You can make decisions even when you do not have all the information.", "risk"),
    ("You notice subtle changes in other people's moods.", "emotional"),
    ("You can comfortably start a conversation with a stranger.", "social"),
    ("When plans suddenly change, you adapt quickly.", "adaptability"),
    ("You question information instead of accepting it immediately.", "curiosity"),
    ("You remain relatively calm when something goes wrong.", "emotional"),
    ("You are willing to try something even when the outcome is uncertain.", "risk"),
    ("You can cooperate with people whose personalities differ greatly from yours.", "social"),
]

if name:
    st.markdown("""
    <div class="card">
        <div class="kicker">02 · Assessment</div>
        <div class="heading">Behavioral profile</div>
        <div class="muted">Move each scale from 1 — strongly disagree to 5 — strongly agree.</div>
    </div>
    """, unsafe_allow_html=True)

    answers = []
    for i, (question, category) in enumerate(questions):
        value = st.slider(
            f"{i+1:02d}  {question}",
            1, 5, 3,
            key=f"q{i}"
        )
        answers.append((category, value))

    if st.button("✦  Generate my personality report", use_container_width=True):
        progress = st.progress(0)
        status = st.empty()

        for message, pct in [
            ("Preparing your profile…", 25),
            ("Reading behavioral patterns…", 50),
            ("Comparing personality dimensions…", 75),
            ("Finishing your report…", 100),
        ]:
            status.markdown(
                f"<div style='color:#b14f73;font-weight:600;font-size:13px'>{message}</div>",
                unsafe_allow_html=True
            )
            progress.progress(pct)
            time.sleep(.35)

        buckets = {k: [] for k in ["emotional","social","risk","curiosity","adaptability"]}
        for category, value in answers:
            buckets[category].append(value)

        def score(category):
            return round(sum(buckets[category]) / len(buckets[category]) / 5 * 100)

        emotional = score("emotional")
        adaptability = score("adaptability")
        social = score("social")
        social_adaptability = round((social + adaptability) / 2)
        risk = score("risk")
        curiosity = score("curiosity")
        overall = round((emotional + social_adaptability + risk + curiosity) / 4)

        if overall >= 88:
            classification = "The Explorer"
            summary = "You show a striking combination of curiosity, flexibility and confidence when stepping into unfamiliar situations."
        elif overall >= 75:
            classification = "The Adaptable"
            summary = "Your responses suggest a balanced personality with a natural ability to adjust while keeping your own preferences."
        elif overall >= 60:
            classification = "The Balanced"
            summary = "You appear comfortable balancing familiar routines with selective curiosity and situational flexibility."
        else:
            classification = "The Grounded"
            summary = "You show a stronger preference for stability and predictability, while still retaining room for exploration."

        st.markdown(f"""
        <div class="card">
            <div class="kicker">03 · Results</div>
            <div class="heading">{name.title()} · Personal Profile</div>
            <div class="muted">Your behavioral pattern has been processed.</div>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(4)
        for col, (label, value) in zip(cols, [
            ("EMOTIONAL INTELLIGENCE", emotional),
            ("SOCIAL ADAPTABILITY", social_adaptability),
            ("RISK TOLERANCE", risk),
            ("CURIOSITY INDEX", curiosity),
        ]):
            with col:
                st.markdown(f"""
                <div class="score">
                    <div class="score-label">{label}</div>
                    <div class="score-number">{value}%</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result">
            <div class="kicker">Personality classification</div>
            <div class="result-title">{classification}</div>
            <div class="quote">“{summary}”</div>
        </div>
        """, unsafe_allow_html=True)

        spread = max(emotional, social_adaptability, risk, curiosity) - min(
            emotional, social_adaptability, risk, curiosity
        )

        if spread >= 45:
            notice = "Your profile contains one or more unusually strong behavioral dimensions."
        else:
            notice = "Your four major dimensions form a relatively harmonious profile."

        st.markdown(f"""
        <div class="card">
            <div class="kicker">Profile note</div>
            <div class="muted" style="font-size:13px;color:#6f5962;">
                {notice}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="footer">
            NEXUS is a fictional entertainment experience and is not a psychological or medical diagnostic tool.
        </div>
        """, unsafe_allow_html=True)
