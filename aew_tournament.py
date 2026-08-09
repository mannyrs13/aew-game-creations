import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium AEW Theme CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&display=swap');

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 99% !important;
    }

    .stApp {
        background: radial-gradient(circle at center, #181d28 0%, #080a0e 100%) !important;
    }

    .aew-main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        color: #ffd700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-top: 0px;
        margin-bottom: 0.6rem;
        font-family: 'Impact', 'Montserrat', sans-serif, Arial;
        text-shadow: 0 0 16px rgba(255, 215, 0, 0.5), 0 0 30px rgba(255, 215, 0, 0.2);
    }

    .finals-title {
        text-align: center;
        font-size: 1.3rem;
        font-weight: 900;
        color: #ffd700;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 0.5rem;
        font-family: 'Impact', 'Montserrat', sans-serif;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
    }

    div.stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%) !important;
        color: #000000 !important;
        border: 1px solid #ffe566 !important;
        border-radius: 5px !important;
        padding: 0.5rem 0.2rem !important;
        font-weight: 900 !important;
        font-size: 0.82rem !important;
        font-family: 'Montserrat', -apple-system, sans-serif !important;
        letter-spacing: 0.03em !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 2px 0 !important;
        box-shadow: 0 4px 12px rgba(255, 215, 0, 0.25) !important;
        transition: all 0.15s ease-in-out !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
        color: #ffffff !important;
        border-color: #f87171 !important;
        box-shadow: 0 0 15px rgba(239, 68, 68, 0.5) !important;
        transform: scale(1.02);
    }

    div.stButton > button:disabled {
        background: linear-gradient(180deg, #1e2430 0%, #121620 100%) !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #ffd700 !important;
        border-radius: 5px !important;
        opacity: 0.95 !important;
        font-weight: 800 !important;
        font-size: 0.82rem !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5) !important;
    }

    .champ-container div.stButton > button:disabled {
        background: radial-gradient(circle, #2a220a 0%, #0d1117 100%) !important;
        border: 2px solid #ffd700 !important;
        color: #ffd700 !important;
        font-size: 0.95rem !important;
        font-family: 'Impact', 'Montserrat', sans-serif !important;
        letter-spacing: 0.05em !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.4) !important;
    }

    .qf-spacer { height: 35px; }
    .qf-gap { height: 62px; }
    .sf-spacer { height: 95px; }
    .sf-gap { height: 140px; }
    .finals-spacer { height: 60px; }
    </style>
""", unsafe_allow_html=True)

# 3. Ratings Database
RATINGS = {
    "Will Ospreay": 97.5, "Christian Cage": 88.0, "Orange Cassidy": 86.5, "Bandido": 85.8,
    "Hologram": 80.0, "Claudio Castagnoli": 88.7, "Wheeler Yuta": 82.3, "Roderick Strong": 84.1,
    "Darby Allin": 89.0, "Hangman Adam Page": 91.2, "Kyle Fletcher": 86.4, "Kyle O'Reilly": 83.5,
    "Katsuyori Shibata": 85.0, "Jon Moxley": 92.3, "Daniel Garcia": 81.5, "Ricochet": 87.8
}

def get_shuffled_roster():
    keys = list(RATINGS.keys())
    random.shuffle(keys)
    return keys

# Initialize Session State
if "slots" not in st.session_state:
    st.session_state.slots = {}
if "scores" not in st.session_state:
    st.session_state.scores = {}
if "pb_score" not in st.session_state:
    st.session_state.pb_score = 87.8
if "roster" not in st.session_state:
    st.session_state.roster = get_shuffled_roster()

drafted_count = sum(1 for k in st.session_state.slots.keys() if k.startswith("r16_"))
draft_complete = (drafted_count >= 16)
current_wrestler = st.session_state.roster[drafted_count] if not draft_complete else None

# Match Grade Calculator
def calc_match_score(p1, p2, round_mult=1.0):
    if p1 in RATINGS and p2 in RATINGS:
        base = (RATINGS[p1] + RATINGS[p2]) / 2.0
        penalty = abs(RATINGS[p1] - RATINGS[p2]) * 0.25
        return round(min((base - penalty) * round_mult, 100.0), 1)
    return 84.0

all_scores = list(st.session_state.scores.values())
if all_scores:
    current_avg = round(sum(all_scores) / len(all_scores), 1)
    if current_avg > st.session_state.pb_score:
        st.session_state.pb_score = current_avg
else:
    current_avg = "--"

# --- TOP HEADER SECTION ---
st.markdown('<div class="aew-main-title">AEW TOURNAMENT GM</div>', unsafe_allow_html=True)

nav_c1, nav_c2, nav_c3 = st.columns([1.5, 2.2, 3])
with nav_c1:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.slots = {}
        st.session_state.scores = {}
        st.session_state.roster = get_shuffled_roster()
        st.rerun()

with nav_c2:
    st.markdown(f"<p style='color: #e2e8f0; margin-top: 8px; font-weight: 700; font-size: 0.9rem;'>🏆 Personal Best: <span style='color:#ffd700;'>{st.session_state.pb_score}/100</span> | Grade: <span style='color:#10b981;'>{current_avg}</span></p>", unsafe_allow_html=True)

with nav_c3:
    if not draft_complete:
        st.markdown(f"<p style='color: #ffd700; margin-top: 8px; font-weight: 900; font-size: 0.95rem; text-transform: uppercase;'>ON THE CLOCK: <span style='color:#ffffff; text-decoration: underline;'>{current_wrestler.upper()}</span> <span style='color: #ef4444;'>(Click empty slot)</span></p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #10b981; margin-top: 8px; font-weight: 900; font-size: 0.95rem;'>DRAFT COMPLETE! Click participants to advance winners.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

def handle_r16_draft(key):
    if key not in st.session_state.slots and not draft_complete:
        st.session_state.slots[key] = current_wrestler
        st.rerun()

# --- BRACKET GRID (7 COLUMNS) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.2, 1.1, 1.1, 1.4, 1.1, 1.1, 1.2])

# Helper to format button label with score if available
def get_label(slot_key, default_name):
    name = st.session_state.slots.get(slot_key, default_name)
    score = st.session_state.scores.get(slot_key)
    if score and name != default_name:
        return f"{name} ⭐ {score}"
    return name

# 1. LEFT - ROUND OF 16
with c1:
    for i in range(8):
        slot_key = f"r16_l_{i}"
        label = st.session_state.slots.get(slot_key, "Place Here")
        if st.button(label, key=f"btn_{slot_key}", disabled=(draft_complete and label == "Place Here")):
            if not draft_complete:
                handle_r16_draft(slot_key)
            else:
                target_qf = f"qf_l_{i//2}"
                st.session_state.slots[target_qf] = label
                p_opp = st.session_state.slots.get(f"r16_l_{i^1}", "")
                st.session_state.scores[target_qf] = calc_match_score(label, p_opp, round_mult=0.95)
                st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

# 2. LEFT - QUARTERFINALS
with c2:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    for i in range(4):
        qf_key = f"qf_l_{i}"
        qf_label = get_label(qf_key, "QF Slot")
        is_empty = ("QF Slot" in qf_label)
        if st.button(qf_label, key=f"btn_{qf_key}", disabled=is_empty):
            target_sf = f"sf_l_{i//2}"
            raw_name = st.session_state.slots.get(qf_key, "")
            st.session_state.slots[target_sf] = raw_name
            opp_key = f"qf_l_{i^1}"
            p_opp = st.session_state.slots.get(opp_key, "")
            st.session_state.scores[target_sf] = calc_match_score(raw_name, p_opp, round_mult=1.0)
            st.rerun()
        if i < 3:
            st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)

# 3. LEFT - SEMIFINALS
with c3:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    for i in range(2):
        sf_key = f"sf_l_{i}"
        sf_label = get_label(sf_key, "Semi Final")
        is_empty = ("Semi Final" in sf_label)
        if st.button(sf_label, key=f"btn_{sf_key}", disabled=is_empty):
            raw_name = st.session_state.slots.get(sf_key, "")
            st.session_state.slots["finalist_1"] = raw_name
            p_opp = st.session_state.slots.get(f"sf_l_{i^1}", "")
            st.session_state.scores["finalist_1"] = calc_match_score(raw_name, p_opp, round_mult=1.05)
            st.rerun()
        if i == 0:
            st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)

# 4. CENTER - FINALS & CHAMPION
with c4:
    st.markdown('<div class="finals-title">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div class="finals-spacer"></div>', unsafe_allow_html=True)
    
    f1_label = get_label("finalist_1", "Finalist 1")
    if st.button(f1_label, key="btn_f1", disabled=("Finalist 1" in f1_label)):
        raw_name = st.session_state.slots.get("finalist_1", "")
        st.session_state.slots["champion"] = raw_name
        f2_raw = st.session_state.slots.get("finalist_2", "")
        st.session_state.scores["champion"] = calc_match_score(raw_name, f2_raw, round_mult=1.1)
        st.rerun()

    st.markdown("<p style='text-align: center; color: #ef4444; font-weight: 900; margin: 6px 0; letter-spacing: 0.15em; font-family: Montserrat;'>VS</p>", unsafe_allow_html=True)
    
    f2_label = get_label("finalist_2", "Finalist 2")
    if st.button(f2_label, key="btn_f2", disabled=("Finalist 2" in f2_label)):
        raw_name = st.session_state.slots.get("finalist_2", "")
        st.session_state.slots["champion"] = raw_name
        f1_raw = st.session_state.slots.get("finalist_1", "")
        st.session_state.scores["champion"] = calc_match_score(raw_name, f1_raw, round_mult=1.1)
        st.rerun()

    st.markdown('<div style="height: 35px;"></div>', unsafe_allow_html=True)
    champ_label = get_label("champion", "???")
    st.markdown('<div class="champ-container">', unsafe_allow_html=True)
    st.button(f"🏆 CHAMPION: {champ_label}", key="btn_champ", disabled=("???" in champ_label))
    st.markdown('</div>', unsafe_allow_html=True)

# 5. RIGHT - SEMIFINALS
with c5:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    for i in range(2):
        sf_key = f"sf_r_{i}"
        sf_label = get_label(sf_key, "Semi Final")
        is_empty = ("Semi Final" in sf_label)
        if st.button(sf_label, key=f"btn_{sf_key}", disabled=is_empty):
            raw_name = st.session_state.slots.get(sf_key, "")
            st.session_state.slots["finalist_2"] = raw_name
            p_opp = st.session_state.slots.get(f"sf_r_{i^1}", "")
            st.session_state.scores["finalist_2"] = calc_match_score(raw_name, p_opp, round_mult=1.05)
            st.rerun()
        if i == 0:
            st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)

# 6. RIGHT - QUARTERFINALS
with c6:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    for i in range(4):
        qf_key = f"qf_r_{i}"
        qf_label = get_label(qf_key, "QF Slot")
        is_empty = ("QF Slot" in qf_label)
        if st.button(qf_label, key=f"btn_{qf_key}", disabled=is_empty):
            target_sf = f"sf_r_{i//2}"
            raw_name = st.session_state.slots.get(qf_key, "")
            st.session_state.slots[target_sf] = raw_name
            opp_key = f"qf_r_{i^1}"
            p_opp = st.session_state.slots.get(opp_key, "")
            st.session_state.scores[target_sf] = calc_match_score(raw_name, p_opp, round_mult=1.0)
            st.rerun()
        if i < 3:
            st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)

# 7. RIGHT - ROUND OF 16
with c7:
    for i in range(8):
        slot_key = f"r16_r_{i}"
        label = st.session_state.slots.get(slot_key, "Place Here")
        if st.button(label, key=f"btn_{slot_key}", disabled=(draft_complete and label == "Place Here")):
            if not draft_complete:
                handle_r16_draft(slot_key)
            else:
                target_qf = f"qf_r_{i//2}"
                st.session_state.slots[target_qf] = label
                p_opp = st.session_state.slots.get(f"r16_r_{i^1}", "")
                st.session_state.scores[target_qf] = calc_match_score(label, p_opp, round_mult=0.95)
                st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
