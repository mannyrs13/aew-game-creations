import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config
st.set_page_config(
    page_title="AEW 16-Man Tournament GM",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# 2. Pure HTML/CSS ESPN Bracket Component
espn_bracket_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    body {
        background-color: #0e1117;
        color: #ffffff;
        padding: 10px;
        overflow-x: auto;
    }

    .bracket-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        min-width: 1100px;
        margin: 0 auto;
    }

    .column {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        flex: 1;
        height: 680px;
        padding: 0 5px;
    }

    .col-header {
        text-align: center;
        font-size: 0.75rem;
        font-weight: 700;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 8px;
    }

    .matchup {
        display: flex;
        flex-direction: column;
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 2;
    }

    .team {
        padding: 8px 10px;
        font-size: 0.82rem;
        font-weight: 600;
        color: #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #334155;
        white-space: nowrap;
    }

    .team:last-child {
        border-bottom: none;
    }

    .team.winner {
        background: #1e3a8a;
        color: #ffffff;
        font-weight: 700;
    }

    .rating {
        color: #fbbf24;
        font-size: 0.75rem;
        margin-left: 6px;
    }

    /* CENTER FINALS CARD */
    .finals-column {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        flex: 1.1;
        height: 680px;
    }

    .finals-card {
        background: #0f172a;
        border: 2px solid #f59e0b;
        border-radius: 10px;
        padding: 16px;
        width: 100%;
        max-width: 200px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(245, 158, 11, 0.2);
    }

    .finals-title {
        color: #f59e0b;
        font-size: 1.1rem;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .vs-text {
        color: #ef4444;
        font-weight: 800;
        font-size: 0.85rem;
        margin: 6px 0;
    }

    .champ-title {
        color: #10b981;
        font-size: 1rem;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    /* ESPN BRACKET BRANCH CONNECTORS */
    .bracket-column {
        position: relative;
    }

    /* Left side connectors */
    .left-r16 .matchup::after {
        content: "";
        position: absolute;
        right: -12px;
        top: 50%;
        width: 12px;
        height: 2px;
        background: #475569;
    }

    /* Right side connectors */
    .right-r16 .matchup::before {
        content: "";
        position: absolute;
        left: -12px;
        top: 50%;
        width: 12px;
        height: 2px;
        background: #475569;
    }
</style>
</head>
<body>

<div class="bracket-container">
    <!-- LEFT: ROUND OF 16 -->
    <div class="column left-r16">
        <div class="col-header">Round of 16</div>
        <div class="matchup"><div class="team">Will Ospreay</div><div class="team">Christian Cage</div></div>
        <div class="matchup"><div class="team">Orange Cassidy</div><div class="team">Bandido</div></div>
        <div class="matchup"><div class="team">Hologram</div><div class="team">Claudio Castagnoli</div></div>
        <div class="matchup"><div class="team">Wheeler Yuta</div><div class="team">Roderick Strong</div></div>
    </div>

    <!-- LEFT: QUARTERFINALS -->
    <div class="column">
        <div class="col-header">Quarterfinals</div>
        <div class="matchup">
            <div class="team winner">Will Ospreay <span class="rating">⭐ 97.5</span></div>
            <div class="team">Bandido <span class="rating">⭐ 85.8</span></div>
        </div>
        <div class="matchup">
            <div class="team">Claudio Castagnoli <span class="rating">⭐ 82.7</span></div>
            <div class="team">Wheeler Yuta <span class="rating">⭐ 82.3</span></div>
        </div>
    </div>

    <!-- LEFT: SEMIFINALS -->
    <div class="column">
        <div class="col-header">Semifinals</div>
        <div class="matchup">
            <div class="team">SF Slot 1</div>
            <div class="team">SF Slot 2</div>
        </div>
    </div>

    <!-- CENTER: FINALS & CHAMPION -->
    <div class="finals-column">
        <div class="finals-card">
            <div class="finals-title">👑 FINALS 👑</div>
            <div class="team" style="justify-content: center; background: #1e293b; border-radius: 4px;">Finalist 1</div>
            <div class="vs-text">VS</div>
            <div class="team" style="justify-content: center; background: #1e293b; border-radius: 4px;">Finalist 2</div>
            
            <div class="champ-title">🏆 CHAMPION 🏆</div>
            <div class="team winner" style="justify-content: center; border-radius: 4px;">???</div>
        </div>
    </div>

    <!-- RIGHT: SEMIFINALS -->
    <div class="column">
        <div class="col-header">Semifinals</div>
        <div class="matchup">
            <div class="team">SF Slot 1</div>
            <div class="team">SF Slot 2</div>
        </div>
    </div>

    <!-- RIGHT: QUARTERFINALS -->
    <div class="column">
        <div class="col-header">Quarterfinals</div>
        <div class="matchup">
            <div class="team">Hangman Adam Page <span class="rating">⭐ 91.2</span></div>
            <div class="team">Kyle O'Reilly <span class="rating">⭐ 78.5</span></div>
        </div>
        <div class="matchup">
            <div class="team">Jon Moxley <span class="rating">⭐ 89.3</span></div>
            <div class="team">Ricochet <span class="rating">⭐ 79.8</span></div>
        </div>
    </div>

    <!-- RIGHT: ROUND OF 16 -->
    <div class="column right-r16">
        <div class="col-header">Round of 16</div>
        <div class="matchup"><div class="team">Darby Allin</div><div class="team">Hangman Adam Page</div></div>
        <div class="matchup"><div class="team">Kyle Fletcher</div><div class="team">Kyle O'Reilly</div></div>
        <div class="matchup"><div class="team">Katsuyori Shibata</div><div class="team">Jon Moxley</div></div>
        <div class="matchup"><div class="team">Daniel Garcia</div><div class="team">Ricochet</div></div>
    </div>
</div>

</body>
</html>
"""

# Render embedded HTML bracket with 720px fixed height canvas
components.html(espn_bracket_html, height=720, scrolling=True)
