import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for clean cards, uniform text, and fixed heights
st.markdown("""
    <style>
    /* Compact Layout */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 98% !important;
    }

    /* Style Streamlit buttons inside match containers */
    div.stButton > button {
        width: 100% !important;
        background-color: #1e293b !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
        padding: 0.35rem 0.4rem !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin: 1px 0 !important;
    }

    div.stButton > button:hover {
        border-color: #3b82f6 !important;
        background-color: #1e3a8a !important;
        color: #ffffff !important;
    }

    /* Round Title Headers */
    .round-title {
        text-align: center;
        font-weight: 700;
        font-size: 0.82rem;
        color: #9ca3af;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
        letter-spacing: 0.05em;
        height: 20px;
    }

    .center-title {
        text-align: center;
        color: #f59e0b;
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }

    /* Match Container Styling */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0f172a !important;
        border-color: #334155 !important;
        border-radius: 8px !important;
        padding: 4px 6px !important;
    }

    /* PRECISE ALIGNMENT SPACERS */
    .qf-top-spacer { height: 48px; }
    .qf-mid-spacer { height: 86px; }

    .sf-top-spacer { height: 138px; }

    .finals-top-spacer { height: 110px; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎮 Your GM Stats")
    st.metric(label="🏆 Best Tournament Grade", value="No completed tournaments yet")
    st.caption("*(Your score is saved privately on this device)*")
    st.button("Share")

# --- TOP NAVIGATION ---
col_btn, col_msg = st.columns([1.5, 4])
with col_btn:
    st.button("🚨 NEW TOURNAMENT", type="primary")
with col_msg:
    st.info("DRAFT COMPLETE! Click on match participants to advance winners.")

st.markdown("---")

# --- BRACKET LAYOUT (7 COLUMNS) ---
c1, c2, c3, c4, c5, c6, c7 = st.columns([1.2, 1.2, 1.1, 1.3, 1.1, 1.2, 1.2])

# 1. LEFT - Round of 16
with c1:
    st.markdown('<div class="round-title">Round of 16</div>', unsafe_allow_html=True)
    r16_l = [
        ("Will Ospreay", "Christian Cage"),
        ("Orange Cassidy", "Bandido"),
        ("Hologram", "Claudio Castagnoli"),
        ("Wheeler Yuta", "Roderick Strong")
    ]
    for idx, (p1, p2) in enumerate(r16_l):
        with st.container(border=True):
            st.button(p1, key=f"r16_l_{idx}_1")
            st.button(p2, key=f"r16_l_{idx}_2")
        if idx < 3:
            st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)

# 2. LEFT - Quarterfinals
with c2:
    st.markdown('<div class="round-title">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-top-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Will Ospreay ⭐ 97.5", key="qf_l_1")
        st.button("Bandido ⭐ 85.8", key="qf_l_2")
    
    st.markdown('<div class="qf-mid-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Claudio Castagnoli ⭐ 82.7", key="qf_l_3")
        st.button("Wheeler Yuta ⭐ 82.3", key="qf_l_4")

# 3. LEFT - Semifinals
with c3:
    st.markdown('<div class="round-title">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-top-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SF Slot 1", key="sf_l_1")
        st.button("SF Slot 2", key="sf_l_2")

# 4. CENTER - FINALS & CHAMPION
with c4:
    st.markdown('<div class="center-title">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div class="finals-top-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Finalist 1", key="finalist_1")
        st.markdown("<h5 style='text-align: center; color: #ef4444; margin: 0.2rem 0;'>VS</h5>", unsafe_allow_html=True)
        st.button("Finalist 2", key="finalist_2")
    
    st.markdown('<div class="center-title" style="margin-top: 1.5rem; color: #10b981;">🏆 CHAMPION 🏆</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("???", key="champion_slot")

# 5. RIGHT - Semifinals
with c5:
    st.markdown('<div class="round-title">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-top-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("SF Slot 1", key="sf_r_1")
        st.button("SF Slot 2", key="sf_r_2")

# 6. RIGHT - Quarterfinals
with c6:
    st.markdown('<div class="round-title">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-top-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Hangman Page ⭐ 91.2", key="qf_r_1")
        st.button("Kyle O'Reilly ⭐ 78.5", key="qf_r_2")
    
    st.markdown('<div class="qf-mid-spacer"></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.button("Jon Moxley ⭐ 89.3", key="qf_r_3")
        st.button("Ricochet ⭐ 79.8", key="qf_r_4")

# 7. RIGHT - Round of 16
with c7:
    st.markdown('<div class="round-title">Round of 16</div>', unsafe_allow_html=True)
    r16_r = [
        ("Darby Allin", "Hangman Adam Page"),
        ("Kyle Fletcher", "Kyle O'Reilly"),
        ("Katsuyori Shibata", "Jon Moxley"),
        ("Daniel Garcia", "Ricochet")
    ]
    for idx, (p1, p2) in enumerate(r16_r):
        with st.container(border=True):
            st.button(p1, key=f"r16_r_{idx}_1")
            st.button(p2, key=f"r16_r_{idx}_2")
        if idx < 3:
            st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
