import streamlit as st

st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom AEW Styling
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; max-width: 98% !important; }
    
    /* AEW Dark & Gold Button Styling */
    div.stButton > button {
        width: 100% !important;
        background-color: #161b22 !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-left: 3px solid #d4af37 !important;
        border-radius: 4px !important;
        padding: 0.4rem !important;
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

    .col-header {
        text-align: center;
        font-size: 0.85rem;
        font-weight: 900;
        color: #d4af37;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.8rem;
    }
    
    /* Container Box for Matchups */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0b0e14 !important;
        border-color: #30363d !important;
        border-radius: 6px !important;
        padding: 4px !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Interactive Bracket
if "winners" not in st.session_state:
    st.session_state.winners = {}

# --- TOP NAVIGATION ---
col_btn, col_msg = st.columns([1.5, 4])
with col_btn:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.winners = {}
        st.rerun()

with col_msg:
    st.info("DRAFT COMPLETE! Click on match participants to advance winners.")

st.markdown("---")

# --- INTERACTIVE BRACKET (7 COLUMNS) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.2, 1.2, 1.1, 1.3, 1.1, 1.2, 1.2])

# Left Side - R16
with c1:
    st.markdown('<div class="col-header">Round of 16</div>', unsafe_allow_html=True)
    r16_left = [
        ("Will Ospreay", "Christian Cage"),
        ("Orange Cassidy", "Bandido"),
        ("Hologram", "Claudio Castagnoli"),
        ("Wheeler Yuta", "Roderick Strong")
    ]
    for idx, (p1, p2) in enumerate(r16_left):
        with st.container(border=True):
            if st.button(p1, key=f"r16_l_{idx}_1"):
                st.session_state.winners[f"qf_l_{idx//2}_1"] = p1
            if st.button(p2, key=f"r16_l_{idx}_2"):
                st.session_state.winners[f"qf_l_{idx//2}_1"] = p2

# Left Side - QF
with c2:
    st.markdown('<div class="col-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        p1 = st.session_state.winners.get("qf_l_0_1", "QF Slot 1")
        st.button(p1, key="qf_btn_1")
    st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        p2 = st.session_state.winners.get("qf_l_1_1", "QF Slot 2")
        st.button(p2, key="qf_btn_2")

# Left Side - SF
with c3:
    st.markdown('<div class="col-header">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SF Slot 1", key="sf_l_1")

# Center - FINALS
with c4:
    st.markdown('<div class="col-header" style="color: #ffd700;">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Finalist 1", key="f_1")
        st.markdown("<h5 style='text-align:center; color:#ef4444; margin:2px 0;'>VS</h5>", unsafe_allow_html=True)
        st.button("Finalist 2", key="f_2")

# Right Side - SF
with c5:
    st.markdown('<div class="col-header">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SF Slot 2", key="sf_r_1")

# Right Side - QF
with c6:
    st.markdown('<div class="col-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Hangman Page ⭐ 91.2", key="qf_r_1")
    st.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Jon Moxley ⭐ 89.3", key="qf_r_2")

# Right Side - R16
with c7:
    st.markdown('<div class="col-header">Round of 16</div>', unsafe_allow_html=True)
    r16_right = [
        ("Darby Allin", "Hangman Page"),
        ("Kyle Fletcher", "Kyle O'Reilly"),
        ("Katsuyori Shibata", "Jon Moxley"),
        ("Daniel Garcia", "Ricochet")
    ]
    for idx, (p1, p2) in enumerate(r16_right):
        with st.container(border=True):
            st.button(p1, key=f"r16_r_{idx}_1")
            st.button(p2, key=f"r16_r_{idx}_2")
