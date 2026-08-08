import streamlit as st

# 1. Force wide mode & set page config at the very top
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject custom CSS for clean layout, button sizing, and text wrapping
st.markdown("""
    <style>
    /* Prevent button text wrapping & ensure uniform appearance */
    div.stButton > button {
        width: 100% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.4rem 0.6rem !important;
    }
    
    /* Ensure the center FINALS & CHAMPION section doesn't wrap awkwardly */
    .finals-header {
        text-align: center;
        color: #FFD700;
        white-space: nowrap;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .champion-header {
        text-align: center;
        color: #FFD700;
        white-space: nowrap;
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    /* Reduce vertical padding to keep brackets compact */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (GM Stats) ---
with st.sidebar:
    st.markdown("### 🎮 Your GM Stats")
    st.metric(label="🏆 Best Tournament Grade", value="No completed tournaments yet")
    st.caption("*(Your score is saved privately on this device)*")
    st.button("Share")

# --- TOP HEADER ---
col_nav, col_btn, col_msg = st.columns([1, 1, 3])

with col_btn:
    if st.button("🚨 NEW TOURNAMENT", type="primary"):
        # Reset state logic here if needed
        pass

with col_msg:
    st.info("DRAFT COMPLETE! Click on match participants to advance winners.")

st.markdown("---")

# --- BRACKET LAYOUT (7 Columns) ---
# Give center column slightly more width to hold "CHAMPION" comfortably
cols = st.columns([1.2, 1.2, 1.1, 1.4, 1.1, 1.2, 1.2])

# Left Side: Round of 16 (Col 0)
with cols[0]:
    st.markdown("##### Round of 16")
    r16_left = [
        "Will Ospreay", "Christian Cage", 
        "Orange Cassidy", "Bandido",
        "Hologram", "Claudio Castagnoli", 
        "Wheeler Yuta", "Roderick Strong"
    ]
    for p in r16_left:
        st.button(p, key=f"r16_l_{p}")

# Left Side: Quarterfinals (Col 1)
with cols[1]:
    st.markdown("##### Quarterfinals")
    st.write("") # Spacing alignment
    qf_left = [
        "Will Ospreay (⭐ 97.5)", "Bandido (⭐ 85.8)",
        "Claudio Castagnoli (⭐ 82.7)", "Wheeler Yuta (⭐ 82.3)"
    ]
    for p in qf_left:
        st.button(p, key=f"qf_l_{p}")
        st.write("")

# Left Side: Semifinals (Col 2)
with cols[2]:
    st.markdown("##### Semifinals")
    st.write("")
    st.write("")
    st.button("SF Slot", key="sf_l_1")
    st.write("")
    st.write("")
    st.write("")
    st.button("SF Slot", key="sf_l_2")

# Center: FINALS & CHAMPION (Col 3)
with cols[3]:
    st.markdown('<div class="finals-header">👑 FINALS 👑</div>', unsafe_allow_html=True)
    st.write("")
    st.button("Finalist 1", key="finalist_1")
    st.markdown("<h4 style='text-align: center; margin: 0.5rem 0;'>VS</h4>", unsafe_allow_html=True)
    st.button("Finalist 2", key="finalist_2")
    
    st.markdown('<div class="champion-header">👑 CHAMPION 👑</div>', unsafe_allow_html=True)
    st.button("???", key="champion_slot")

# Right Side: Semifinals (Col 4)
with cols[4]:
    st.markdown("##### Semifinals")
    st.write("")
    st.write("")
    st.button("SF Slot", key="sf_r_1")
    st.write("")
    st.write("")
    st.write("")
    st.button("SF Slot", key="sf_r_2")

# Right Side: Quarterfinals (Col 5)
with cols[5]:
    st.markdown("##### Quarterfinals")
    st.write("")
    qf_right = [
        "Hangman Adam Page (⭐ 91.2)", "Kyle O'Reilly (⭐ 78.5)",
        "Jon Moxley (⭐ 89.3)", "Ricochet (⭐ 79.8)"
    ]
    for p in qf_right:
        st.button(p, key=f"qf_r_{p}")
        st.write("")

# Right Side: Round of 16 (Col 6)
with cols[6]:
    st.markdown("##### Round of 16")
    r16_right = [
        "Darby Allin", "Hangman Adam Page", 
        "Kyle Fletcher", "Kyle O'Reilly",
        "Katsuyori Shibata", "Jon Moxley", 
        "Daniel Garcia", "Ricochet"
    ]
    for p in r16_right:
        st.button(p, key=f"r16_r_{p}")
