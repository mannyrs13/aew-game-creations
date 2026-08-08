import streamlit as st

# 1. Wide mode & Page Configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Exact Custom CSS to match the original local VS Code layout
st.markdown("""
    <style>
    /* Remove padding and force dark background */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 99% !important;
    }

    .stApp {
        background-color: #0d0d0d !important;
    }

    /* Main Big Yellow Header */
    .aew-main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 900;
        color: #ffcc00;
        text-transform: uppercase;
        letter-spacing: 0.05em;
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

    /* Bright Neon Green Draft Buttons ("Place Here") */
    div.stButton > button {
        width: 100% !important;
        background-color: #00ff66 !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.5rem 0.2rem !important;
        font-weight: 800 !important;
        font-size: 0.85rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 2px 0 !important;
    }

    div.stButton > button:hover {
        background-color: #00cc52 !important;
        color: #000000 !important;
    }

    /* Dark Slate Cards for QF, SF, and Finals slots */
    .dark-slot-card {
        background-color: #1e1e1e;
        border: 1px solid #2d2d2d;
        border-radius: 6px;
        padding: 0.6rem 0.4rem;
        text-align: center;
        color: #737373;
        font-weight: 700;
        font-size: 0.85rem;
        white-space: nowrap;
        margin-bottom: 8px;
    }

    .champ-card {
        background-color: #1a1a1a;
        border: 1px solid #333333;
        border-radius: 6px;
        padding: 0.8rem 0.4rem;
        text-align: center;
        color: #a3a3a3;
        font-weight: 700;
        font-size: 0.85rem;
    }

    /* Offsets to align inner bracket rounds */
    .qf-spacer { height: 42px; }
    .qf-gap { height: 72px; }
    .sf-spacer { height: 110px; }
    .sf-gap { height: 155px; }
    .finals-spacer { height: 85px; }
    </style>
""", unsafe_allow_html=True)

# Session State for Draft Logic
if "draft_slots" not in st.session_state:
    st.session_state.draft_slots = {}

# --- TOP HEADER SECTION ---
st.markdown('<div class="aew-main-title">AEW TOURNAMENT GM</div>', unsafe_allow_html=True)

nav_c1, nav_c2, nav_c3 = st.columns([1.5, 2, 3])
with nav_c1:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.draft_slots = {}
        st.rerun()

with nav_c2:
    st.markdown("<p style='color: #cccccc; margin-top: 8px; font-weight: 600; font-size: 0.9rem;'>🏆 Personal Best: 87.8/100</p>", unsafe_allow_html=True)

with nav_c3:
    st.markdown("<p style='color: #ffcc00; margin-top: 8px; font-weight: 800; font-size: 0.95rem;'>ON THE CLOCK: BANDIDO <span style='color: #ff4444;'>(Click an empty slot)</span></p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- BRACKET GRID (7 COLUMNS MATCHING YOUR SCREENSHOT) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.2, 1.1, 1.1, 1.3, 1.1, 1.1, 1.2])

# 1. LEFT - ROUND OF 16 (Green Buttons)
with c1:
    for i in range(8):
        slot_label = st.session_state.draft_slots.get(f"r16_l_{i}", "Place Here")
        if st.button(slot_label, key=f"r16_l_btn_{i}"):
            st.session_state.draft_slots[f"r16_l_{i}"] = "Bandido"
            st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 18px;"></div>', unsafe_allow_html=True)

# 2. LEFT - QUARTERFINALS
with c2:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)

# 3. LEFT - SEMIFINALS
with c3:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">Semi Final</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">Semi Final</div>', unsafe_allow_html=True)

# 4. CENTER - FINALS & CHAMPION
with c4:
    st.markdown('<div class="finals-title">🏆 FINALS 🏆</div>', unsafe_allow_html=True)
    st.markdown('<div class="finals-spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">Finalist 1</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888; font-weight: 900; margin: 4px 0; font-style: italic;'>VS</p>", unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">Finalist 2</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 35px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="champ-card">🍵 TOURNAMENT CHAMPION 🍵<br><span style="color: #666666;">???</span></div>', unsafe_allow_html=True)

# 5. RIGHT - SEMIFINALS
with c5:
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">Semi Final</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">Semi Final</div>', unsafe_allow_html=True)

# 6. RIGHT - QUARTERFINALS
with c6:
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-gap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="dark-slot-card">QF Slot</div>', unsafe_allow_html=True)

# 7. RIGHT - ROUND OF 16 (Green Buttons)
with c7:
    for i in range(8):
        slot_label = st.session_state.draft_slots.get(f"r16_r_{i}", "Place Here")
        if st.button(slot_label, key=f"r16_r_btn_{i}"):
            st.session_state.draft_slots[f"r16_r_{i}"] = "Bandido"
            st.rerun()
        if i % 2 == 1 and i < 7:
            st.markdown('<div style="height: 18px;"></div>', unsafe_allow_html=True)
