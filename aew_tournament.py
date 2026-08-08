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

# 2. Pure SVG & HTML Tournament Bracket matching the user image
exact_bracket_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    body {
        background-color: #0e1117;
        color: #ffffff;
        padding: 10px;
    }

    .bracket-wrapper {
        position: relative;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        height: 650px;
    }

    /* SVG Overlay for Bracket Lines */
    .bracket-lines {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
        pointer-events: none;
    }

    .bracket-lines path {
        stroke: #64748b;
        stroke-width: 2;
        fill: none;
    }

    /* Column Containers */
    .bracket-grid {
        display: flex;
        justify-content: space-between;
        height: 100%;
        position: relative;
        z-index: 2;
    }

    .col {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        width: 15%;
    }

    .col-finals {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 18%;
    }

    .col-header {
        text-align: center;
        font-size: 0.75rem;
        font-weight: 700;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        position: absolute;
        top: 0;
        width: 100%;
    }

    /* Matchup Cards */
    .match-box {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 4px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
    }

    .slot {
        padding: 6px 8px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #334155;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .slot:last-child {
        border-bottom: none;
    }

    .slot.winner {
        background: #1e3a8a;
        color: #ffffff;
        font-weight: 700;
        border-radius: 4px;
    }

    .rating {
        color: #fbbf24;
        font-size: 0.72rem;
        margin-left: 4px;
    }

    /* Finals Centerpiece */
    .finals-card {
        background: #0f172a;
        border: 2px solid #f59e0b;
        border-radius: 8px;
        padding: 12px;
        width: 100%;
        text-align: center;
    }

    .finals-title { color: #f59e0b; font-size: 1rem; font-weight: 800; margin-bottom: 6px; }
    .vs-text { color: #ef4444; font-weight: 800; font-size: 0.8rem; margin: 4px 0; }
    .champ-title { color: #10b981; font-size: 0.95rem; font-weight: 800; margin-top: 14px; margin-bottom: 6px; }
</style>
</head>
<body>

<div class="bracket-wrapper">
    <!-- SVG CONNECTING LINES (Exact shape from user diagram) -->
    <svg class="bracket-lines" viewBox="0 0 1000 650" preserveAspectRatio="none">
        <!-- LEFT SIDE BRANCHES -->
        <!-- R16 to QF -->
        <path d="M 150,60 H 180 V 130 H 150 M 180,95 H 210" />
        <path d="M 150,200 H 180 V 270 H 150 M 180,235 H 210" />
        <path d="M 150,340 H 180 V 410 H 150 M 180,375 H 210" />
        <path d="M 150,480 H 180 V 550 H 150 M 180,515 H 210" />

        <!-- QF to SF -->
        <path d="M 360,95 H 390 V 235 H 360 M 390,165 H 420" />
        <path d="M 360,375 H 390 V 515 H 360 M 390,445 H 420" />

        <!-- SF to FINALS -->
        <path d="M 570,165 H 600 V 445 H 570 M 600,305 H 630" />

        <!-- RIGHT SIDE BRANCHES -->
        <!-- R16 to QF -->
        <path d="M 850,60 H 820 V 130 H 850 M 820,95 H 790" />
        <path d="M 850,200 H 820 V 270 H 850 M 820,235 H 790" />
        <path d="M 850,340 H 820 V 410 H 850 M 820,375 H 790" />
        <path d="M 850,480 H 820 V 550 H 850 M 820,515 H 790" />

        <!-- QF to SF -->
        <path d="M 640,95 H 610 V 235 H 640 M 610,165 H 580" opacity="0" /> <!-- Spacer -->
    </svg>

    <!-- BRACKET CONTENT GRID -->
    <div class="bracket-grid">
        <!-- LEFT: R16 -->
        <div class="col" style="padding-top: 25px;">
            <div class="col-header">Round of 16</div>
            <div class="match-box"><div class="slot">Will Ospreay</div><div class="slot">Christian Cage</div></div>
            <div class="match-box"><div class="slot">Orange Cassidy</div><div class="slot">Bandido</div></div>
            <div class="match-box"><div class="slot">Hologram</div><div class="slot">Claudio Castagnoli</div></div>
            <div class="match-box"><div class="slot">Wheeler Yuta</div><div class="slot">Roderick Strong</div></div>
        </div>

        <!-- LEFT: QF -->
        <div class="col" style="padding-top: 25px;">
            <div class="col-header">Quarterfinals</div>
            <div class="match-box">
                <div class="slot winner">Will Ospreay <span class="rating">⭐ 97.5</span></div>
                <div class="slot">Bandido <span class="rating">⭐ 85.8</span></div>
            </div>
            <div class="match-box">
                <div class="slot">Claudio Castagnoli <span class="rating">⭐ 82.7</span></div>
                <div class="slot">Wheeler Yuta <span class="rating">⭐ 82.3</span></div>
            </div>
        </div>

        <!-- LEFT: SF -->
        <div class="col" style="padding-top: 25px;">
            <div class="col-header">Semifinals</div>
            <div class="match-box">
                <div class="slot">SF Slot 1</div>
                <div class="slot">SF Slot 2</div>
            </div>
        </div>

        <!-- CENTER: FINALS -->
        <div class="col-finals">
            <div class="col-header" style="top: 25px;">Finals</div>
            <div class="finals-card">
                <div class="finals-title">👑 FINALS 👑</div>
                <div class="slot" style="justify-content: center; background: #1e293b; border-radius: 4px;">Finalist 1</div>
                <div class="vs-text">VS</div>
                <div class="slot" style="justify-content: center; background: #1e293b; border-radius: 4px;">Finalist 2</div>
                
                <div class="champ-title">🏆 CHAMPION 🏆</div>
                <div class="slot winner" style="justify-content: center; border-radius: 4px;">???</div>
            </div>
        </div>

        <!-- RIGHT: SF -->
        <div class="col" style="padding-top: 25px;">
            <div class="col-header">Semifinals</div>
            <div class="match-box">
                <div class="slot">SF Slot 1</div>
                <div class="slot">SF Slot 2</div>
            </div>
        </div>

        <!-- RIGHT: QF -->
        <div class="col" style="padding-top: 25px;">
            <div class="col-header">Quarterfinals</div>
            <div class="match-box">
                <div class="slot">Hangman Page <span class="rating">⭐ 91.2</span></div>
                <div class="slot">Kyle O'Reilly <span class="rating">⭐ 78.5</span></div>
            </div>
            <div class="match-box">
                <div class="slot">Jon Moxley <span class="rating">⭐ 89.3</span></div>
                <div class="slot">Ricochet <span class="rating">⭐ 79.8</span></div>
            </div>
        </div>

        <!-- RIGHT: R16 -->
        <div class="col" style="padding-top: 25px;">
            <div class="col-header">Round of 16</div>
            <div class="match-box"><div class="slot">Darby Allin</div><div class="slot">Hangman Page</div></div>
            <div class="match-box"><div class="slot">Kyle Fletcher</div><div class="slot">Kyle O'Reilly</div></div>
            <div class="match-box"><div class="slot">Katsuyori Shibata</div><div class="slot">Jon Moxley</div></div>
            <div class="match-box"><div class="slot">Daniel Garcia</div><div class="slot">Ricochet</div></div>
        </div>
    </div>
</div>

</body>
</html>
"""

# Render embedded HTML bracket with 680px fixed height canvas
components.html(exact_bracket_html, height=680, scrolling=True)
