import streamlit as st

# 1. Wide mode configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS to style buttons, center the bracket, and draw connector lines
st.markdown("""
    <style>
    /* Center container and fix spacing */
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 95%;
    }

    /* Button styling for clean look and no wrapping */
    div.stButton > button {
        width: 100% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        padding: 0.35rem 0.5rem !important;
        font-size: 0.85rem !important;
    }

    /* Bracket line connectors styling */
    .line-top {
        border-top: 2px solid #555;
        border-right: 2px solid #555;
        height: 50px;
        margin-right: -10px;
    }
    .line-bottom {
        border-bottom: 2px solid #555;
        border-right: 2px solid #555;
        height: 50px;
        margin-right: -10px;
    }
    .line-connector {
        border-top: 2px solid #555;
        height: 2px;
        width: 100%;
        margin-top: 25px;
    }

    /* Headers */
    .bracket-header {
        text-align: center;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        color: #d1d5db;
    }
    .center-header {
        text-align: center;
        color: #FFD700;
        white-space: nowrap;
        font-weight: bold;
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

# --- BRACKET GRID (9 Columns for Left, Center, Right + Connector Lines) ---
# R16 -> Connector -> QF -> SF -> CENTER -> SF -> QF -> Connector -> R16
cols = st.columns([1.3, 0.2, 1.3, 1.2, 1.5, 1.2, 1.3, 0.2, 1.3])

# --- LEFT SIDE BRACKET ---
with cols[0]:
    st.markdown('<div class="bracket-header">Round of 16</div>', unsafe_allow_html=True)
    r16_left = [
        "Will Ospreay", "Christian Cage", 
        "Orange Cassidy", "Bandido",
        "Hologram", "Claudio Castagnoli", 
        "Wheeler Yuta", "Roderick Strong"
    ]
    for i, p in enumerate(r16_left):
        st.button(p, key=f"r16_l_{i}")
        if i % 2 == 0:
            st.write("")  # Tight pairing gap

# Left Connectors
with cols[1]:
    st.write("")
    st.write("")
    st.markdown('<div class="line-top"></div><div class="line-bottom"></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="line-top"></div><div class="line-bottom"></div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<div class="bracket-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.write("")
    qf_left = [
        "Will Ospreay (⭐ 97.5)", "Bandido (⭐ 85.8)",
        "Claudio Castagnoli (⭐ 82.7)", "Wheeler Yuta (⭐ 82.3)"
    ]
    for i, p in enumerate(qf_left):
        st.button(p, key=f"qf_l_{i}")
        st.write("")
        st.write("")

with cols[3]:
    st.markdown('<div class="bracket-header">Semifinals</div>', unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.button("SF Slot 1", key="sf_l_1")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.button("SF Slot 2", key="sf_l_2")

# --- CENTER / FINALS ---
with cols[4]:
    st.markdown('<div class="center-header" style="font-size: 1.4rem;">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.write("")
    st.button("Finalist 1", key="finalist_1")
    st.markdown('<div class="center-header" style="margin: 0.5rem 0;">VS</div>', unsafe_allow_html=True)
    st.button("Finalist 2", key="finalist_2")
    
    st.markdown('<div class="center-header" style="font-size: 1.2rem; margin-top: 1.5rem;">👑 CHAMPION 👑</div>', unsafe_allow_html=True)
    st.button("???", key="champion_slot")

# --- RIGHT SIDE BRACKET ---
with cols[5]:
    st.markdown('<div class="bracket-header">Semifinals</div>', unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.button("SF Slot 1", key="sf_r_1")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.button("SF Slot 2", key="sf_r_2")

with cols[6]:
    st.markdown('<div class="bracket-header">Quarterfinals</div>', unsafe_allow_html=True)
    st.write("")
    qf_right = [
        "Hangman Adam Page (⭐ 91.2)", "Kyle O'Reilly (⭐ 78.5)",
        "Jon Moxley (⭐ 89.3)", "Ricochet (⭐ 79.8)"
    ]
    for i, p in enumerate(qf_right):
        st.button(p, key=f"qf_r_{i}")
        st.write("")
        st.write("")

# Right Connectors
with cols[7]:
    st.write("")
    st.write("")
    st.markdown('<div class="line-top" style="transform: scaleX(-1);"></div><div class="line-bottom" style="transform: scaleX(-1);"></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="line-top" style="transform: scaleX(-1);"></div><div class="line-bottom" style="transform: scaleX(-1);"></div>', unsafe_allow_html=True)

with cols[8]:
    st.markdown('<div class="bracket-header">Round of 16</div>', unsafe_allow_html=True)
    r16_right = [
        "Darby Allin", "Hangman Adam Page", 
        "Kyle Fletcher", "Kyle O'Reilly",
        "Katsuyori Shibata", "Jon Moxley", 
        "Daniel Garcia", "Ricochet"
    ]
    for i, p in enumerate(r16_right):
        st.button(p, key=f"r16_r_{i}")
        if i % 2 == 0:
            st.write("")
