import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Styling to force strict alignment and center the layout
st.markdown("""
    <style>
    /* Center and constrain main container */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }

    /* Button styling for compact tournament slots */
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
    }

    div.stButton > button:hover {
        border-color: #3b82f6 !important;
        background-color: #1e3a8a !important;
        color: #ffffff !important;
    }

    /* Custom Spacer helper to align Quarterfinals with R16 lines */
    .qf-spacer {
        height: 22px;
    }
    .sf-spacer {
        height: 65px;
    }

    /* Connector lines between rounds */
    .connector-right {
        border-right: 2px solid #475569;
        border-top: 2px solid #475569;
        border-bottom: 2px solid #475569;
        height: 62px;
        margin-top: 14px;
        margin-bottom: 28px;
        border-radius: 0 6px 6px 0;
    }

    .connector-left {
        border-left: 2px solid #475569;
        border-top: 2px solid #475569;
        border-bottom: 2px solid #475569;
        height: 62px;
        margin-top: 14px;
        margin-bottom: 28px;
        border-radius: 6px 0 0 6px;
    }

    /* Column Headers */
    .round-title {
        text-align: center;
        font-weight: 700;
        font-size: 0.8rem;
        color: #9ca3af;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .center-title {
        text-align: center;
        color: #f59e0b;
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
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

# --- BRACKET LAYOUT (9 EQUAL COLUMNS) ---
c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns([1.2, 0.2, 1.2, 1.1, 1.3, 1.1, 1.2, 0.2, 1.2])

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
        st.button(p1, key=f"r16_l_{idx}_1")
        st.button(p2, key=f"r16_l_{idx}_2")
        if idx < 3:
            st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)

# 2. LEFT CONNECTORS
with c2:
    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="connector-right"></div>', unsafe_allow_html=True)
    st.markdown('<div class="connector-right"></div>', unsafe_allow_html=True)

# 3. LEFT - Quarterfinals
with c3:
    st.markdown('<div class="round-title">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    st.button("Will Ospreay ⭐ 97.5", key="qf_l_1")
    st.button("Bandido ⭐ 85.8", key="qf_l_2")
    
    st.markdown('<div style="height: 38px;"></div>', unsafe_allow_html=True)
    st.button("Claudio Castagnoli ⭐ 82.7", key="qf_l_3")
    st.button("Wheeler Yuta ⭐ 82.3", key="qf_l_4")

# 4. LEFT - Semifinals
with c4:
    st.markdown('<div class="round-title">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    st.button("SF Slot 1", key="sf_l_1")
    st.button("SF Slot 2", key="sf_l_2")

# 5. CENTER - FINALS & CHAMPION
with c5:
    st.markdown('<div class="center-title">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    st.button("Finalist 1", key="finalist_1")
    st.markdown("<h5 style='text-align: center; color: #ef4444; margin: 0.2rem 0;'>VS</h5>", unsafe_allow_html=True)
    st.button("Finalist 2", key="finalist_2")
    
    st.markdown('<div class="center-title" style="margin-top: 1rem; color: #10b981;">🏆 CHAMPION 🏆</div>', unsafe_allow_html=True)
    st.button("???", key="champion_slot")

# 6. RIGHT - Semifinals
with c6:
    st.markdown('<div class="round-title">Semifinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="sf-spacer"></div>', unsafe_allow_html=True)
    st.button("SF Slot 1", key="sf_r_1")
    st.button("SF Slot 2", key="sf_r_2")

# 7. RIGHT - Quarterfinals
with c7:
    st.markdown('<div class="round-title">Quarterfinals</div>', unsafe_allow_html=True)
    st.markdown('<div class="qf-spacer"></div>', unsafe_allow_html=True)
    st.button("Hangman Page ⭐ 91.2", key="qf_r_1")
    st.button("Kyle O'Reilly ⭐ 78.5", key="qf_r_2")
    
    st.markdown('<div style="height: 38px;"></div>', unsafe_allow_html=True)
    st.button("Jon Moxley ⭐ 89.3", key="qf_r_3")
    st.button("Ricochet ⭐ 79.8", key="qf_r_4")

# 8. RIGHT CONNECTORS
with c8:
    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="connector-left"></div>', unsafe_allow_html=True)
    st.markdown('<div class="connector-left"></div>', unsafe_allow_html=True)

# 9. RIGHT - Round of 16
with c9:
    st.markdown('<div class="round-title">Round of 16</div>', unsafe_allow_html=True)
    r16_r = [
        ("Darby Allin", "Hangman Adam Page"),
        ("Kyle Fletcher", "Kyle O'Reilly"),
        ("Katsuyori Shibata", "Jon Moxley"),
        ("Daniel Garcia", "Ricochet")
    ]
    for idx, (p1, p2) in enumerate(r16_r):
        st.button(p1, key=f"r16_r_{idx}_1")
        st.button(p2, key=f"r16_r_{idx}_2")
        if idx < 3:
            st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
