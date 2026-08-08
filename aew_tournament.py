import streamlit as st

# 1. Wide mode configuration
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for a true tournament bracket layout
st.markdown("""
    <style>
    /* Global Container Padding */
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 98%;
    }

    /* Bracket Container Layout using Flexbox */
    .bracket-wrapper {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: stretch;
        width: 100%;
        margin-top: 1rem;
        font-family: system-ui, -apple-system, sans-serif;
    }

    /* Individual Bracket Column */
    .bracket-column {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        flex: 1;
        min-width: 130px;
        margin: 0 4px;
    }

    /* Column Headers */
    .bracket-header {
        text-align: center;
        font-weight: 700;
        font-size: 0.95rem;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 1rem;
        height: 24px;
    }

    /* Matchup Pair Box */
    .matchup {
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        margin: 6px 0;
    }

    /* Team / Wrestler Slot */
    .slot {
        background-color: #1E293B;
        color: #F8FAFC;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 6px 10px;
        font-size: 0.82rem;
        font-weight: 600;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        margin: 2px 0;
        text-align: center;
    }

    .slot.winner {
        border-color: #3B82F6;
        background-color: #1E3A8A;
        color: #FFFFFF;
    }

    .slot.rating {
        color: #FBBF24;
    }

    /* Center Finals Styling */
    .finals-box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .finals-title {
        color: #F59E0B;
        font-weight: 800;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }

    .vs-badge {
        font-weight: 800;
        color: #EF4444;
        margin: 4px 0;
        font-size: 0.9rem;
    }

    .champion-title {
        color: #10B981;
        font-weight: 800;
        font-size: 1.1rem;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    /* Connectors using CSS Pseudo-elements */
    .bracket-column.left .matchup::after {
        content: "";
        position: absolute;
        right: -8px;
        top: 25%;
        bottom: 25%;
        width: 8px;
        border-right: 2px solid #475569;
        border-top: 2px solid #475569;
        border-bottom: 2px solid #475569;
    }

    .bracket-column.right .matchup::after {
        content: "";
        position: absolute;
        left: -8px;
        top: 25%;
        bottom: 25%;
        width: 8px;
        border-left: 2px solid #475569;
        border-top: 2px solid #475569;
        border-bottom: 2px solid #475569;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎮 Your GM Stats")
    st.metric(label="🏆 Best Tournament Grade", value="No completed tournaments yet")
    st.caption("*(Your score is saved privately on this device)*")
    st.button("Share")

# --- TOP BAR ---
col_btn, col_msg = st.columns([1.5, 4])
with col_btn:
    st.button("🚨 NEW TOURNAMENT", type="primary")
with col_msg:
    st.info("DRAFT COMPLETE! Click on match participants to advance winners.")

st.markdown("---")

# --- CLEAN HTML/CSS BRACKET RENDER ---
html_bracket = """
<div class="bracket-wrapper">
    <!-- LEFT SIDE: Round of 16 -->
    <div class="bracket-column left">
        <div class="bracket-header">Round of 16</div>
        <div class="matchup"><div class="slot">Will Ospreay</div><div class="slot">Christian Cage</div></div>
        <div class="matchup"><div class="slot">Orange Cassidy</div><div class="slot">Bandido</div></div>
        <div class="matchup"><div class="slot">Hologram</div><div class="slot">Claudio Castagnoli</div></div>
        <div class="matchup"><div class="slot">Wheeler Yuta</div><div class="slot">Roderick Strong</div></div>
    </div>

    <!-- LEFT SIDE: Quarterfinals -->
    <div class="bracket-column left">
        <div class="bracket-header">Quarterfinal</div>
        <div class="matchup"><div class="slot winner">Will Ospreay <span class="rating">⭐ 97.5</span></div><div class="slot">Bandido <span class="rating">⭐ 85.8</span></div></div>
        <div class="matchup"><div class="slot">Claudio Castagnoli <span class="rating">⭐ 82.7</span></div><div class="slot">Wheeler Yuta <span class="rating">⭐ 82.3</span></div></div>
    </div>

    <!-- LEFT SIDE: Semifinals -->
    <div class="bracket-column left">
        <div class="bracket-header">Semifinals</div>
        <div class="matchup"><div class="slot">SF Slot 1</div><div class="slot">SF Slot 2</div></div>
    </div>

    <!-- CENTER: FINALS & CHAMPION -->
    <div class="bracket-column finals-box">
        <div class="finals-title">👑 FINALS 👑</div>
        <div class="slot" style="min-width: 140px;">Finalist 1</div>
        <div class="vs-badge">VS</div>
        <div class="slot" style="min-width: 140px;">Finalist 2</div>
        
        <div class="champion-title">🏆 CHAMPION 🏆</div>
        <div class="slot winner" style="min-width: 140px;">???</div>
    </div>

    <!-- RIGHT SIDE: Semifinals -->
    <div class="bracket-column right">
        <div class="bracket-header">Semifinals</div>
        <div class="matchup"><div class="slot">SF Slot 1</div><div class="slot">SF Slot 2</div></div>
    </div>

    <!-- RIGHT SIDE: Quarterfinals -->
    <div class="bracket-column right">
        <div class="bracket-header">Quarterfinal</div>
        <div class="matchup"><div class="slot">Hangman Adam Page <span class="rating">⭐ 91.2</span></div><div class="slot">Kyle O'Reilly <span class="rating">⭐ 78.5</span></div></div>
        <div class="matchup"><div class="slot">Jon Moxley <span class="rating">⭐ 89.3</span></div><div class="slot">Ricochet <span class="rating">⭐ 79.8</span></div></div>
    </div>

    <!-- RIGHT SIDE: Round of 16 -->
    <div class="bracket-column right">
        <div class="bracket-header">Round of 16</div>
        <div class="matchup"><div class="slot">Darby Allin</div><div class="slot">Hangman Adam Page</div></div>
        <div class="matchup"><div class="slot">Kyle Fletcher</div><div class="slot">Kyle O'Reilly</div></div>
        <div class="matchup"><div class="slot">Katsuyori Shibata</div><div class="slot">Jon Moxley</div></div>
        <div class="matchup"><div class="slot">Daniel Garcia</div><div class="slot">Ricochet</div></div>
    </div>
</div>
"""

st.markdown(html_bracket, unsafe_allow_html=True)
