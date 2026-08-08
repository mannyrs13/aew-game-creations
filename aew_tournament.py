import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS: Added top margin & button styling for all rounds
st.markdown("""
    <style>
    /* Add top spacing so the title isn't cut off at the top */
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 99% !important;
    }

    .stApp {
        background-color: #0d0d0d !important;
    }

    /* Main Title with Top Margin Space */
    .aew-main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 900;
        color: #ffcc00;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 10px;
        margin-bottom: 0.8rem;
        font-family: 'Impact', sans-serif, Arial;
    }

    .finals-title {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 800;
        color: #ffcc00;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    /* Interactive Buttons for R16, QF, SF, and Finals */
    div.stButton > button {
        width: 100% !important;
        background-color: #00ff66 !important;
        color: #000000 !important;
        border: none !important;
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

    /* Style for dark unfilled bracket slots */
    .slot-btn-empty div.stButton > button {
        background-color: #1e1e1e !important;
        color: #737373 !important;
        border: 1px solid #2d2d2d !important;
    }

    /* Spacers for vertical alignment */
    .qf-spacer { height: 35px; }
    .qf-gap { height: 62px; }
    .sf-spacer { height: 95px; }
    .sf-gap { height: 140px; }
    .finals-spacer { height: 70px; }
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Tournament State & Roster
if "slots" not in st.session_state:
    st.session_state.slots = {}

# Roster pool for drafting
roster = [
    "Will Ospreay", "Christian Cage", "Orange Cassidy", "Bandido",
    "Hologram", "Claudio Castagnoli", "Wheeler Yuta", "Roderick Strong",
    "Darby Allin", "Hangman Adam Page", "Kyle Fletcher", "Kyle O'Reilly",
    "Katsuyori Shibata", "Jon Moxley", "Daniel Garcia", "Ricochet"
]

# Track current draft pick index
drafted_count = sum(1 for k in st.session_state.slots.keys() if k.startswith("r16_"))
current_wrestler = roster[drafted_count] if drafted_count < len(roster) else "DRAFT COMPLETE"

# --- TOP HEADER SECTION ---
st.markdown('<div class="aew-main-title">AEW TOURNAMENT GM</div>', unsafe_allow_html=True)

nav_c1, nav_c2, nav_c3 = st.columns([1.5, 2, 3])
with nav_c1:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.slots = {}
        st.rerun()

with nav_c2:
    st.markdown("<p style='color: #cccccc; margin-top: 8px; font-weight: 600; font-size: 0.9rem;'>🏆 Personal Best: 87.8/100</p>", unsafe_allow_html=True)

with nav_c3:
    if current_wrestler != "DRAFT COMPLETE":
        st.markdown(f"<p style='color: #ffcc00; margin-top: 8px; font-weight: 800; font-size: 0.95rem;'>ON THE CLOCK: {current_wrestler.upper()} <span style='color: #ff4444;'>(Click an empty slot)</span></p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #00ff66; margin-top: 8px; font-weight: 800; font-size: 0.95rem;'>DRAFT COMPLETE! Click winners to advance them.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- BRACKET GRID (7 COLUMNS) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.2, 1.1, 1.1, 1.3, 1.1, 1.1, 1.2])

# Helper function to handle slot clicks
def handle_r16_click(key):
    if key not in st.session_state.slots and current_wrestler != "DRAFT COMPLETE":
        st.session_state.slots[key] = current_wrestler
        st.rerun()

# 1. LEFT - ROUND OF 16
with c1:
    for i in range(8):
        slot_key = f"r16_l_{i}"
        label = st.session_state.slots.get(slot_key, "Place Here")
        if st.button(label, key=f"btn_{slot_key}"):
            handle_r16_click(slot_key)
            # Auto-advance winner if clicked after draft
            if current_wrestler == "DRAFT COMPLETE" and label != "Place Here":
                st.session_state.slots[f"qf_l_{i//2}"] = label
                st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

# 2. LEFT - QUARTERFINALS
with c2:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    for i in range(4):
        qf_key = f"qf_l_{i}"
        qf_label = st.session_state.slots.get(qf_key, "QF Slot")
        if st.button(qf_label, key=f"btn_{qf_key}"):
            if qf_label != "QF Slot":
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
        if st.button(sf_label, key=f"btn_{sf_key}"):
            if sf_label != "Semi Final":
                st.session_state.slots["finalist_1"] = sf_label
                st.rerun()
        if i == 0:
            st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)

# 4. CENTER - FINALS & CHAMPION
with c4:
    st.markdown('<div class="finals-title">🏆 FINALS 🏆</div>', unsafe_allow_html=True)
    st.markdown('<div class="finals-spacer"></div>', unsafe_allow_html=True)
    
    f1_label = st.session_state.slots.get("finalist_1", "Finalist 1")
    if st.button(f1_label, key="btn_f1"):
        if f1_label != "Finalist 1":
            st.session_state.slots["champion"] = f1_label
            st.rerun()

    st.markdown("<p style='text-align: center; color: #888888; font-weight: 900; margin: 4px 0;'>VS</p>", unsafe_allow_html=True)
    
    f2_label = st.session_state.slots.get("finalist_2", "Finalist 2")
    if st.button(f2_label, key="btn_f2"):
        if f2_label != "Finalist 2":
            st.session_state.slots["champion"] = f2_label
            st.rerun()

    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
    champ_label = st.session_state.slots.get("champion", "???")
    st.button(f"🍵 CHAMPION: {champ_label} 🍵", key="btn_champ")

# 5. RIGHT - SEMIFINALS
with c5:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    for i in range(2):
        sf_key = f"sf_r_{i}"
        sf_label = st.session_state.slots.get(sf_key, "Semi Final")
        if st.button(sf_label, key=f"btn_{sf_key}"):
            if sf_label != "Semi Final":
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
        if st.button(qf_label, key=f"btn_{qf_key}"):
            if qf_label != "QF Slot":
                st.session_state.slots[f"sf_r_{i//2}"] = qf_label
                st.rerun()
        if i < 3:
            st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)

# 7. RIGHT - ROUND OF 16
with c7:
    for i in range(8):
        slot_key = f"r16_r_{i}"
        label = st.session_state.slots.get(slot_key, "Place Here")
        if st.button(label, key=f"btn_{slot_key}"):
            handle_r16_click(slot_key)
            if current_wrestler == "DRAFT COMPLETE" and label != "Place Here":
                st.session_state.slots[f"qf_r_{i//2}"] = label
                st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
