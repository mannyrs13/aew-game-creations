import streamlit as st

# 1. Wide mode & Page Configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Complete CSS Overhaul for AEW Theme, Full Names, & Clean Top Padding
st.markdown("""
    <style>
    /* Remove default Streamlit top whitespace */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 99% !important;
    }

    /* Force background color */
    .stApp {
        background-color: #0b0e14 !important;
    }

    /* Column Headers */
    .col-header {
        text-align: center;
        font-size: 0.75rem !important;
        font-weight: 900 !important;
        color: #d4af37 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        white-space: nowrap !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 0 6px rgba(212, 175, 55, 0.4);
    }

    /* Tournament Buttons - Scaled font & full visibility */
    div.stButton > button {
        width: 100% !important;
        background-color: #161b22 !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-left: 3px solid #d4af37 !important;
        border-radius: 4px !important;
        padding: 0.35rem 0.15rem !important;
        font-weight: 700 !important;
        font-size: 0.72rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 1px 0 !important;
    }

    div.stButton > button:hover {
        border-color: #ef4444 !important;
        background-color: #991b1b !important;
        color: #ffffff !important;
    }

    /* Match Container Styling */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #11161d !important;
        border-color: #30363d !important;
        border-radius: 6px !important;
        padding: 3px !important;
        margin-bottom: 6px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Session State for Interactive Winners
if "winners" not in st.session_state:
    st.session_state.winners = {}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎮 Your GM Stats")
    st.metric(label="🏆 Best Tournament Grade", value="No completed tournaments yet")
    st.caption("*(Your score is saved privately on this device)*")
    st.button("Share")

# --- TOP NAVIGATION BAR ---
col_btn, col_msg = st.columns([1.2, 4.8])
with col_btn:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        st.session_state.winners = {}
        st.rerun()

with col_msg:
    st.info("DRAFT COMPLETE! Click on match participants to advance winners.")

st.markdown("---")

# --- BRACKET GRID (7 COLUMNS WITH ADJUSTED RATIOS) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.35, 1.25, 1.15, 1.35, 1.15, 1.25, 1.35])

# 1. LEFT - ROUND OF 16
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
                st.session_state.winners[f"qf_l_{idx//2}"] = p1
            if st.button(p2, key=f"r16_l_{idx}_2"):
                st.session_state.winners[f"qf_l_{idx//2}"] = p2

# 2. LEFT - QUARTERFINALS
with c2:
    st.markdown('<div class="col-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 22px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        p1 = st.session_state.winners.get("qf_l_0", "QF Slot 1")
        st.button(p1, key="qf_btn_l1")
    
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        p2 = st.session_state.winners.get("qf_l_1", "QF Slot 2")
        st.button(p2, key="qf_btn_l2")

# 3. LEFT - SEMIFINALS
with c3:
    st.markdown('<div class="col-header">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 90px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SF Slot 1", key="sf_btn_l1")

# 4. CENTER - FINALS & CHAMPION
with c4:
    st.markdown('<div class="col-header" style="color: #ffd700;">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Finalist 1", key="f_btn_1")
        st.markdown("<h5 style='text-align:center; color:#ef4444; margin:1px 0; font-size:0.75rem;'>VS</h5>", unsafe_allow_html=True)
        st.button("Finalist 2", key="f_btn_2")

# 5. RIGHT - SEMIFINALS
with c5:
    st.markdown('<div class="col-header">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 90px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SF Slot 2", key="sf_btn_r1")

# 6. RIGHT - QUARTERFINALS
with c6:
    st.markdown('<div class="col-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 22px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Hangman Page ⭐ 91.2", key="qf_btn_r1")
    
    st.markdown('<div style="height: 48px;"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Jon Moxley ⭐ 89.3", key="qf_btn_r2")

# 7. RIGHT - ROUND OF 16
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
