import streamlit as st

# 1. Page Configuration - Maximize Viewport Width
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Complete AEW Theme Overhaul (CSS)
st.markdown("""
    <style>
    /* Remove default Streamlit top padding */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 98% !important;
    }

    /* AEW Dark Obsidian Background */
    .stApp {
        background-color: #0b0e14 !important;
    }

    /* AEW Gold Headers with Text Shadow */
    .col-header {
        text-align: center;
        font-size: 0.85rem !important;
        font-weight: 900 !important;
        color: #d4af37 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 0.6rem !important;
        text-shadow: 0 0 8px rgba(212, 175, 55, 0.4);
        white-space: nowrap !important;
    }

    /* AEW Dark & Gold Interactive Buttons */
    div.stButton > button {
        width: 100% !important;
        background-color: #161b22 !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-left: 3px solid #d4af37 !important;
        border-radius: 4px !important;
        padding: 0.45rem 0.4rem !important;
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 2px 0 !important;
    }

    /* Red Hover State on Wrestler Match Selection */
    div.stButton > button:hover {
        border-color: #e61c24 !important;
        border-left: 3px solid #e61c24 !important;
        background-color: #991b1b !important;
        color: #ffffff !important;
    }

    /* AEW Match Container Box */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #11161d !important;
        border: 1px solid #21262d !important;
        border-radius: 6px !important;
        padding: 4px 6px !important;
        margin-bottom: 8px !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Interactive Session State
if "winners" not in st.session_state:
    st.session_state.winners = {}

# --- TOP NAVIGATION BAR ---
col_btn, col_msg = st.columns([1.2, 4.8])
with col_btn:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.winners = {}
        st.rerun()

with col_msg:
    st.info("DRAFT COMPLETE! Click on any wrestler to advance them into the next round.")

st.markdown("---")

# --- BRACKET GRID (4 BALANCED COLUMNS) ---
c1, c2, c3, c4 = st.columns([2.0, 1.4, 1.3, 1.4])

# 1. ROUND OF 16 (Side-by-Side Wing Sub-Grid)
with c1:
    st.markdown('<div class="col-header">Round of 16</div>', unsafe_allow_html=True)
    sub_l, sub_r = st.columns(2)
    
    r16_left = [
        ("Will Ospreay", "Christian Cage", "qf_1"),
        ("Orange Cassidy", "Bandido", "qf_1"),
        ("Hologram", "Claudio Castagnoli", "qf_2"),
        ("Wheeler Yuta", "Roderick Strong", "qf_2")
    ]
    
    r16_right = [
        ("Darby Allin", "Hangman Adam Page", "qf_3"),
        ("Kyle Fletcher", "Kyle O'Reilly", "qf_3"),
        ("Katsuyori Shibata", "Jon Moxley", "qf_4"),
        ("Daniel Garcia", "Ricochet", "qf_4")
    ]

    # Left Wing Matches
    with sub_l:
        for idx, (p1, p2, target_qf) in enumerate(r16_left):
            with st.container(border=True):
                if st.button(p1, key=f"r16_l_{idx}_1"):
                    st.session_state.winners[f"{target_qf}_slot_{1 if idx%2==0 else 2}"] = p1
                    st.rerun()
                if st.button(p2, key=f"r16_l_{idx}_2"):
                    st.session_state.winners[f"{target_qf}_slot_{1 if idx%2==0 else 2}"] = p2
                    st.rerun()

    # Right Wing Matches
    with sub_r:
        for idx, (p1, p2, target_qf) in enumerate(r16_right):
            with st.container(border=True):
                if st.button(p1, key=f"r16_r_{idx}_1"):
                    st.session_state.winners[f"{target_qf}_slot_{1 if idx%2==0 else 2}"] = p1
                    st.rerun()
                if st.button(p2, key=f"r16_r_{idx}_2"):
                    st.session_state.winners[f"{target_qf}_slot_{1 if idx%2==0 else 2}"] = p2
                    st.rerun()

# 2. QUARTERFINALS
with c2:
    st.markdown('<div class="col-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
    
    qf_matches = [
        ("qf_1", "sf_1", "Slot 1"),
        ("qf_2", "sf_1", "Slot 2"),
        ("qf_3", "sf_2", "Slot 1"),
        ("qf_4", "sf_2", "Slot 2")
    ]

    for idx, (qf_id, target_sf, sf_slot) in enumerate(qf_matches):
        p1 = st.session_state.winners.get(f"{qf_id}_slot_1", f"QF {idx+1} Wrestler A")
        p2 = st.session_state.winners.get(f"{qf_id}_slot_2", f"QF {idx+1} Wrestler B")
        
        with st.container(border=True):
            if st.button(p1, key=f"qf_btn_{idx}_1"):
                st.session_state.winners[f"{target_sf}_{sf_slot}"] = p1
                st.rerun()
            if st.button(p2, key=f"qf_btn_{idx}_2"):
                st.session_state.winners[f"{target_sf}_{sf_slot}"] = p2
                st.rerun()
        st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)

# 3. SEMIFINALS
with c3:
    st.markdown('<div class="col-header">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)
    
    # Semifinal Match 1
    sf1_p1 = st.session_state.winners.get("sf_1_Slot 1", "SF 1 Winner A")
    sf1_p2 = st.session_state.winners.get("sf_1_Slot 2", "SF 1 Winner B")
    with st.container(border=True):
        if st.button(sf1_p1, key="sf1_btn_1"):
            st.session_state.winners["finalist_1"] = sf1_p1
            st.rerun()
        if st.button(sf1_p2, key="sf1_btn_2"):
            st.session_state.winners["finalist_1"] = sf1_p2
            st.rerun()

    st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)

    # Semifinal Match 2
    sf2_p1 = st.session_state.winners.get("sf_2_Slot 1", "SF 2 Winner A")
    sf2_p2 = st.session_state.winners.get("sf_2_Slot 2", "SF 2 Winner B")
    with st.container(border=True):
        if st.button(sf2_p1, key="sf2_btn_1"):
            st.session_state.winners["finalist_2"] = sf2_p1
            st.rerun()
        if st.button(sf2_p2, key="sf2_btn_2"):
            st.session_state.winners["finalist_2"] = sf2_p2
            st.rerun()

# 4. FINALS & CHAMPION
with c4:
    st.markdown('<div class="col-header" style="color: #ffd700;">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True)
    
    f1 = st.session_state.winners.get("finalist_1", "Finalist 1")
    f2 = st.session_state.winners.get("finalist_2", "Finalist 2")
    
    with st.container(border=True):
        if st.button(f1, key="f_btn_1"):
            st.session_state.winners["champion"] = f1
            st.rerun()
        st.markdown("<h5 style='text-align:center; color:#e61c24; margin:2px 0; font-size:0.85rem;'>VS</h5>", unsafe_allow_html=True)
        if st.button(f2, key="f_btn_2"):
            st.session_state.winners["champion"] = f2
            st.rerun()

    st.markdown('<div class="col-header" style="color: #10b981; margin-top: 1.5rem;">🏆 CHAMPION 🏆</div>', unsafe_allow_html=True)
    champ = st.session_state.winners.get("champion", "???")
    with st.container(border=True):
        st.button(f"👑 {champ}", key="champ_display")
