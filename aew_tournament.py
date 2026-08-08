import streamlit as st
import random

# 1. Page Config
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Enhanced AEW PPV Dark Gold Theme CSS
st.markdown("""
    <style>
    /* Remove padding and add authentic AEW dark obsidian textured gradient background */
    .block-container {
        padding-top: 1.8rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 99% !important;
    }

    .stApp {
        background: radial-gradient(circle at center, #151922 0%, #0b0e14 100%) !important;
    }

    /* Main Big AEW Gold Header */
    .aew-main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 900;
        color: #ffd700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0px;
        margin-bottom: 0.8rem;
        font-family: 'Impact', sans-serif, Arial;
        text-shadow: 0 0 12px rgba(255, 215, 0, 0.4);
    }

    .finals-title {
        text-align: center;
        font-size: 1.25rem;
        font-weight: 900;
        color: #ffd700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }

    /* Primary Draft Buttons (Neon Green During Draft, Gold Accents) */
    div.stButton > button {
        width: 100% !important;
        background-color: #00ff66 !important;
        color: #000000 !important;
        border: 1px solid #00cc52 !important;
        border-radius: 4px !important;
        padding: 0.45rem 0.2rem !important;
        font-weight: 800 !important;
        font-size: 0.82rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 2px 0 !important;
    }

    div.stButton > button:hover {
        background-color: #00cc52 !important;
        color: #000000 !important;
    }

    /* Disabled/Empty Dark Slots with Subtle Gold/Slate Border */
    div.stButton > button:disabled {
        background-color: #161b22 !important;
        color: #8b949e !important;
        border: 1px solid #30363d !important;
        border-left: 3px solid #d4af37 !important;
        opacity: 0.85 !important;
    }

    /* Center Champion Box Highlight */
    .champ-container div.stButton > button:disabled {
        background: radial-gradient(circle, #21262d 0%, #0d1117 100%) !important;
        border: 2px solid #ffd700 !important;
        color: #ffd700 !important;
        font-size: 0.95rem !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.25) !important;
    }

    /* Vertical Alignment Spacers */
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
if "match_scores" not in st.session_state:
    st.session_state.match_scores = []
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
    return 82.0

if st.session_state.match_scores:
    current_avg = round(sum(st.session_state.match_scores) / len(st.session_state.match_scores), 1)
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
        st.session_state.match_scores = []
        st.session_state.roster = get_shuffled_roster()
        st.rerun()

with nav_c2:
    st.markdown(f"<p style='color: #cccccc; margin-top: 8px; font-weight: 600; font-size: 0.9rem;'>🏆 Personal Best: {st.session_state.pb_score}/100 | Current Grade: <span style='color:#00ff66;'>{current_avg}</span></p>", unsafe_allow_html=True)

with nav_c3:
    if not draft_complete:
        st.markdown(f"<p style='color: #ffd700; margin-top: 8px; font-weight: 800; font-size: 0.95rem;'>ON THE CLOCK: {current_wrestler.upper()} <span style='color: #ff4444;'>(Click an empty slot)</span></p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #00ff66; margin-top: 8px; font-weight: 800; font-size: 0.95rem;'>DRAFT COMPLETE! Click participants to advance winners.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Helper function for slot placement
def handle_r16_draft(key):
    if key not in st.session_state.slots and not draft_complete:
        st.session_state.slots[key] = current_wrestler
        st.rerun()

# --- BRACKET GRID (7 COLUMNS) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.2, 1.1, 1.1, 1.4, 1.1, 1.1, 1.2])

# 1. LEFT - ROUND OF 16
with c1:
    for i in range(8):
        slot_key = f"r16_l_{i}"
        label = st.session_state.slots.get(slot_key, "Place Here")
        if st.button(label, key=f"btn_{slot_key}", disabled=(draft_complete and label == "Place Here")):
            if not draft_complete:
                handle_r16_draft(slot_key)
            else:
                st.session_state.slots[f"qf_l_{i//2}"] = label
                p_opp = st.session_state.slots.get(f"r16_l_{i^1}", "")
                if p_opp:
                    st.session_state.match_scores.append(calc_match_score(label, p_opp, 0.95))
                st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

# 2. LEFT - QUARTERFINALS
with c2:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    for i in range(4):
        qf_key = f"qf_l_{i}"
        qf_label = st.session_state.slots.get(qf_key, "QF Slot")
        is_empty = (qf_label == "QF Slot")
        if st.button(qf_label, key=f"btn_{qf_key}", disabled=is_empty):
            st.session_state.slots[f"sf_l_{i//2}"] = qf_label
            st.rerun()
        if i < 3:
            st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)

# 3. LEFT - SEMIFINALS
with c3:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    for i in range(2):
        sf_key = f"sf_l_{i}"
        sf_label = st.session_state.slots.get(sf_key, "Semi Final")
        is_empty = (sf_label == "Semi Final")
        if st.button(sf_label, key=f"btn_{sf_key}", disabled=is_empty):
            st.session_state.slots["finalist_1"] = sf_label
            st.rerun()
        if i == 0:
            st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)

# 4. CENTER - FINALS & CHAMPION (Stacked Vertically & Centered)
with c4:
    st.markdown('<div class="finals-title">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div class="finals-spacer"></div>', unsafe_allow_html=True)
    
    # Finalist 1 (Top)
    f1_label = st.session_state.slots.get("finalist_1", "Finalist 1")
    if st.button(f1_label, key="btn_f1", disabled=(f1_label == "Finalist 1")):
        st.session_state.slots["champion"] = f1_label
        f2_label = st.session_state.slots.get("finalist_2", "")
        if f2_label:
            st.session_state.match_scores.append(calc_match_score(f1_label, f2_label, 1.1))
        st.rerun()

    # VS Badge
    st.markdown("<p style='text-align: center; color: #ef4444; font-weight: 900; margin: 6px 0; letter-spacing: 0.1em;'>VS</p>", unsafe_allow_html=True)
    
    # Finalist 2 (Bottom)
    f2_label = st.session_state.slots.get("finalist_2", "Finalist 2")
    if st.button(f2_label, key="btn_f2", disabled=(f2_label == "Finalist 2")):
        st.session_state.slots["champion"] = f2_label
        if f1_label:
            st.session_state.match_scores.append(calc_match_score(f2_label, f1_label, 1.1))
        st.rerun()

    # Centered Champion Slot
    st.markdown('<div style="height: 35px;"></div>', unsafe_allow_html=True)
    champ_label = st.session_state.slots.get("champion", "???")
    st.markdown('<div class="champ-container">', unsafe_allow_html=True)
    st.button(f"🏆 CHAMPION: {champ_label} 🏆", key="btn_champ", disabled=(champ_label == "???"))
    st.markdown('</div>', unsafe_allow_html=True)

# 5. RIGHT - SEMIFINALS
with c5:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    for i in range(2):
        sf_key = f"sf_r_{i}"
        sf_label = st.session_state.slots.get(sf_key, "Semi Final")
        is_empty = (sf_label == "Semi Final")
        if st.button(sf_label, key=f"btn_{sf_key}", disabled=is_empty):
            st.session_state.slots["finalist_2"] = sf_label
            st.rerun()
        if i == 0:
            st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)

# 6. RIGHT - QUARTERFINALS
with c6:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    for i in range(4):
        qf_key = f"qf_r_{i}"
        qf_label = st.session_state.slots.get(qf_key, "QF Slot")
        is_empty = (qf_label == "QF Slot")
        if st.button(qf_label, key=f"btn_{qf_key}", disabled=is_empty):
            st.session_state.slots[f"sf_r_{i//2}"] = qf_label
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
                st.session_state.slots[f"qf_r_{i//2}"] = label
                p_opp = st.session_state.slots.get(f"r16_r_{i^1}", "")
                if p_opp:
                    st.session_state.match_scores.append(calc_match_score(label, p_opp, 0.95))
                st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
