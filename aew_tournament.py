import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapses sidebar by default to maximize screen width
)

# 2. Custom AEW Styling & Fluid Layout
st.markdown("""
    <style>
    /* Maximize canvas width and remove top padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 98% !important;
    }

    .stApp {
        background-color: #0b0e14 !important;
    }

    /* Column Headers */
    .col-header {
        text-align: center;
        font-size: 0.85rem !important;
        font-weight: 900 !important;
        color: #d4af37 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        margin-bottom: 0.6rem !important;
        text-shadow: 0 0 8px rgba(212, 175, 55, 0.4);
    }

    /* Interactive AEW Buttons - Full visibility & clean text */
    div.stButton > button {
        width: 100% !important;
        background-color: #161b22 !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-left: 3px solid #d4af37 !important;
        border-radius: 4px !important;
        padding: 0.45rem 0.5rem !important;
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 2px 0 !important;
    }

    div.stButton > button:hover {
        border-color: #ef4444 !important;
        background-color: #991b1b !important;
        color: #ffffff !important;
    }

    /* Match Container Cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #11161d !important;
        border-color: #30363d !important;
        border-radius: 6px !important;
        padding: 4px 6px !important;
        margin-bottom: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Interactive Winners
if "winners" not in st.session_state:
    st.session_state.winners = {}

# --- TOP NAVIGATION BAR ---
col_btn, col_msg = st.columns([1.5, 5])
with col_btn:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.winners = {}
        st.rerun()

with col_msg:
    st.info("DRAFT COMPLETE! Click on match participants to advance winners into the next round.")

st.markdown("---")

# --- BRACKET GRID (4 BALANCED WIDE COLUMNS) ---
# [ROUND OF 16 (Wide Left), QUARTERFINALS, SEMIFINALS, FINALS & CHAMPION]
c1, c2, c3, c4 = st.columns([2.2, 1.4, 1.3, 1.5])

# 1. ROUND OF 16 (2-Column Sub-Grid for 8 Matches)
with c1:
    st.markdown('<div class="col-header">Round of 16 (All Matches)</div>', unsafe_allow_html=True)
    r16_sub1, r16_sub2 = st.columns(2)
    
    r16_left_bracket = [
        ("Will Ospreay", "Christian Cage"),
        ("Orange Cassidy", "Bandido"),
        ("Hologram", "Claudio Castagnoli"),
        ("Wheeler Yuta", "Roderick Strong")
    ]
    
    r16_right_bracket = [
        ("Darby Allin", "Hangman Adam Page"),
        ("Kyle Fletcher", "Kyle O'Reilly"),
        ("Katsuyori Shibata", "Jon Moxley"),
        ("Daniel Garcia", "Ricochet")
    ]

    # Left Side Bracket Matches
    with r16_sub1:
        for idx, (p1, p2) in enumerate(r16_left_bracket):
            with st.container(border=True):
                if st.button(p1, key=f"r16_l_{idx}_1"):
                    st.session_state.winners[f"qf_0"] = p1
                if st.button(p2, key=f"r16_l_{idx}_2"):
                    st.session_state.winners[f"qf_0"] = p2

    # Right Side Bracket Matches
    with r16_sub2:
        for idx, (p1, p2) in enumerate(r16_right_bracket):
            with st.container(border=True):
                if st.button(p1, key=f"r16_r_{idx}_1"):
                    st.session_state.winners[f"qf_1"] = p1
                if st.button(p2, key=f"r16_r_{idx}_2"):
                    st.session_state.winners[f"qf_1"] = p2

# 2. QUARTERFINALS
with c2:
    st.markdown('<div class="col-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 15px;"></div>', unsafe_allow_html=True)
    
    qf_matches = [
        ("qf_0", "Will Ospreay ⭐ 97.5", "Bandido ⭐ 85.8", "qf_btn_1"),
        ("qf_1", "Claudio Castagnoli ⭐ 82.7", "Wheeler Yuta ⭐ 82.3", "qf_btn_2"),
        ("qf_2", "Hangman Page ⭐ 91.2", "Kyle O'Reilly ⭐ 78.5", "qf_btn_3"),
        ("qf_3", "Jon Moxley ⭐ 89.3", "Ricochet ⭐ 79.8", "qf_btn_4")
    ]
    
    for key_id, def_p1, def_p2, btn_key in qf_matches:
        with st.container(border=True):
            p1 = st.session_state.winners.get(key_id, def_p1)
            if st.button(p1, key=f"{btn_key}_1"):
                st.session_state.winners[f"sf_{key_id}"] = p1

# 3. SEMIFINALS
with c3:
    st.markdown('<div class="col-header">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.button("SF Slot 1", key="sf_btn_1")
        st.button("SF Slot 2", key="sf_btn_2")
        
    st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.button("SF Slot 3", key="sf_btn_3")
        st.button("SF Slot 4", key="sf_btn_4")

# 4. FINALS & CHAMPION
with c4:
    st.markdown('<div class="col-header" style="color: #ffd700;">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.button("Finalist 1", key="f_btn_1")
        st.markdown("<h5 style='text-align:center; color:#ef4444; margin:3px 0; font-size:0.85rem;'>VS</h5>", unsafe_allow_html=True)
        st.button("Finalist 2", key="f_btn_2")
        
    st.markdown('<div class="col-header" style="color: #10b981; margin-top: 1.5rem;">🏆 CHAMPION 🏆</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("???", key="champ_btn")
