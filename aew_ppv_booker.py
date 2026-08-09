import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(
    page_title="AEW PPV GM Booker",
    page_icon="🎟️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Enhanced CSS Styling with Clean Spacing & Slot Rules
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&display=swap');

    /* Added clean top padding so headers never get cut off */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 98% !important;
    }

    .stApp {
        background: radial-gradient(circle at center, #181d28 0%, #080a0e 100%) !important;
    }

    /* AEW Main Header */
    .aew-main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        color: #ffd700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-top: 10px !important;
        margin-bottom: 0.8rem;
        font-family: 'Impact', 'Montserrat', sans-serif;
        text-shadow: 0 0 16px rgba(255, 215, 0, 0.5), 0 0 30px rgba(255, 215, 0, 0.2);
    }

    /* On The Clock Banner */
    .clock-banner {
        background: linear-gradient(90deg, #161b22 0%, #21262d 50%, #161b22 100%);
        border: 2px solid #ffd700;
        border-radius: 8px;
        padding: 10px 18px;
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.2);
        margin-bottom: 15px;
    }

    .clock-text {
        color: #ffd700;
        font-size: 1.1rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .clock-sub {
        color: #ef4444;
        font-weight: 800;
        font-size: 0.88rem;
        margin-left: 10px;
    }

    /* Active Valid Buttons (Red to Gold Hover) */
    div.stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
        color: #ffffff !important;
        border: 1px solid #f87171 !important;
        border-radius: 5px !important;
        padding: 0.5rem 0.2rem !important;
        font-weight: 900 !important;
        font-size: 0.82rem !important;
        font-family: 'Montserrat', sans-serif !important;
        letter-spacing: 0.04em !important;
        text-transform: uppercase !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3) !important;
        transition: all 0.15s ease-in-out !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%) !important;
        color: #000000 !important;
        border-color: #ffe566 !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.5) !important;
        transform: scale(1.02);
    }

    /* Disabled / Invalid Division Buttons */
    div.stButton > button:disabled {
        background: #1e2430 !important;
        color: #64748b !important;
        border: 1px solid #334155 !important;
        opacity: 0.6 !important;
        font-weight: 800 !important;
    }

    /* Filled Match Slot Card */
    .placed-slot {
        background: linear-gradient(180deg, #1e2430 0%, #121620 100%);
        border: 1px solid #334155;
        border-left: 4px solid #10b981;
        border-radius: 5px;
        padding: 8px 12px;
        color: #f1f5f9;
        font-weight: 800;
        font-size: 0.88rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }

    /* Match Container Boxes */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #11161d !important;
        border: 1px solid #21262d !important;
        border-left: 3px solid #ffd700 !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        margin-bottom: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Roster Database with Division Categories
ROSTER = [
    {"name": "Penelope Ford", "type": "Womens Singles"},
    {"name": "Red Velvet", "type": "Womens Singles"},
    {"name": "Hikaru Shida", "type": "Womens Singles"},
    {"name": "Willow Nightingale", "type": "Womens Singles"},
    {"name": "Will Ospreay", "type": "Mens Singles"},
    {"name": "Jon Moxley", "type": "Mens Singles"},
    {"name": "Hangman Adam Page", "type": "Mens Singles"},
    {"name": "Orange Cassidy", "type": "Mens Singles"},
    {"name": "Claudio Castagnoli", "type": "Mens Singles"},
    {"name": "Darby Allin", "type": "Mens Singles"},
    {"name": "Wheeler Yuta", "type": "Mens Singles"},
]

# Initialize Session State
if "placed_slots" not in st.session_state:
    st.session_state.placed_slots = {}

if "pool" not in st.session_state or not st.session_state.pool:
    st.session_state.pool = list(ROSTER)
    random.shuffle(st.session_state.pool)

if "current_talent" not in st.session_state or st.session_state.current_talent is None:
    if st.session_state.pool:
        st.session_state.current_talent = st.session_state.pool.pop(0)

# Auto-Draw & Placement Logic
def place_talent_and_autodraw(slot_key):
    if st.session_state.current_talent:
        st.session_state.placed_slots[slot_key] = st.session_state.current_talent["name"]
        
        if st.session_state.pool:
            st.session_state.current_talent = st.session_state.pool.pop(0)
        else:
            st.session_state.current_talent = None
            
        st.rerun()

# --- HEADER SECTION ---
st.markdown('<div class="aew-main-title">🏟️ AEW WRESTLEDREAM GM BOOKER</div>', unsafe_allow_html=True)

col_top1, col_top2 = st.columns([1.5, 4])
with col_top1:
    if st.button("🚨 NEW CARD", type="primary"):
        st.session_state.placed_slots = {}
        st.session_state.pool = list(ROSTER)
        random.shuffle(st.session_state.pool)
        st.session_state.current_talent = st.session_state.pool.pop(0)
        st.rerun()

with col_top2:
    if st.session_state.current_talent:
        talent_name = st.session_state.current_talent["name"]
        talent_type = st.session_state.current_talent["type"]
        st.markdown(f"""
            <div class="clock-banner">
                <span class="clock-text">ON THE CLOCK: <span style="color:#ffffff;">{talent_name}</span></span>
                <span class="clock-sub">| DIVISION: <span style="color:#ffd700;">{talent_type.upper()}</span></span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="clock-banner" style="border-color: #10b981;">
                <span class="clock-text" style="color: #10b981;">✅ DRAFT COMPLETE! CARD FULLY BOOKED.</span>
            </div>
        """, unsafe_allow_html=True)

# --- MATCH CARD WITH DIVISION VALIDATION ---
matches = [
    ("Match 1: AEW Continental Championship", ["m1_s1", "m1_s2"], "Mens Singles"),
    ("Match 2: AEW World Trios Championship", ["m2_s1", "m2_s2"], "Mens Singles"),
    ("Match 3: AEW TBS Championship", ["m3_s1", "m3_s2"], "Womens Singles"),
    ("Match 4: AEW Women's World Championship (Triple Threat)", ["m4_s1", "m4_s2", "m4_s3"], "Womens Singles"),
    ("Match 5: AEW World Championship", ["m5_s1", "m5_s2"], "Mens Singles"),
]

curr_talent = st.session_state.current_talent

for match_title, slots, match_type in matches:
    with st.container(border=True):
        st.markdown(f"<h4 style='color: #ffd700; margin-bottom: 6px; font-size: 1.1rem;'>{match_title} <span style='font-size: 0.8rem; color: #8b949e;'>({match_type})</span></h4>", unsafe_allow_html=True)
        cols = st.columns(len(slots))
        for idx, slot_key in enumerate(slots):
            with cols[idx]:
                if slot_key in st.session_state.placed_slots:
                    # Show placed wrestler
                    wrestler = st.session_state.placed_slots[slot_key]
                    st.markdown(f'<div class="placed-slot">✅ {wrestler}</div>', unsafe_allow_html=True)
                else:
                    # Check gender/type compatibility rule
                    is_valid = (curr_talent is not None) and (curr_talent["type"] == match_type)
                    
                    btn_text = "PLACE HERE" if is_valid else f"⛔ {match_type.split()[0].upper()} ONLY"
                    
                    if st.button(btn_text, key=f"btn_{slot_key}", disabled=not is_valid):
                        place_talent_and_autodraw(slot_key)
