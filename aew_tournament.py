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

# 2. Perfected SVG & HTML Tournament Bracket Component
polished_bracket_html = """
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
        max-width: 1280px;
        margin: 0 auto;
        height: 700px;
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
        stroke: #475569;
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
        width: 15.5%;
        padding-top: 35px; /* Leave space for top column titles */
    }

    .col-finals {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 18%;
        padding-top: 35px;
    }

    /* Clean, Spanned Column Headers */
    .col-header {
        position: absolute;
        top: 0;
        text-align: center;
        font-size: 0.78rem;
        font-weight: 800;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        width: 100%;
    }

    /* Matchup Cards */
    .match-box {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 2px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
    }

    .slot {
        padding: 6px 10px;
        font-size: 0.82rem;
        font-weight: 600;
        color: #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #334155;
        white-space: nowrap;
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
        font-size: 0.75rem;
        font-weight: 700;
        margin-left: 6px;
    }

    /* Finals Centerpiece */
    .finals-card {
        background: #0f172a;
        border: 2px solid #f59e0b;
        border-radius: 10px;
        padding: 14px;
        width: 100%;
        text-align: center;
        box-shadow: 0 8px 16px rgba(245, 158, 11, 0.15);
    }

    .finals-title { color: #f59e0b; font-size: 1.05rem; font-weight: 800; margin-bottom: 8px; }
    .vs-text { color: #ef4444; font-weight: 800; font-size: 0.85rem; margin: 6px 0; }
    .champ-title { color: #10b981; font-size: 1rem; font-weight: 800; margin-top: 16px; margin-bottom: 8px; }
</style>
</head>
<body>

<div class="bracket-wrapper">
    <!-- SVG CONNECTING LINES (Clean coordinate mapping) -->
    <svg class="bracket-lines" viewBox="0 0 1200 700" preserveAspectRatio="none">
        <!-- LEFT SIDE BRANCHES -->
        <!-- R16 to QF -->
        <path d="M 185,90 H 215 V 170 H 185 M 215,130 H 245" />
        <path d="M 185,250 H 215 V 330 H 185 M 215,290 H 245" />
        <path d="M 185,410 H 215 V 490 H 185 M 215,450 H 245" />
        <path d="M 185,570 H 215 V 650 H 185 M 215,610 H 245" />

        <!-- QF to SF -->
        <path d="M 430,130 H 460 V 290 H 430 M 460,210 H 490" />
        <path d="M 430,450 H 460 V 610 H 430 M 460,530 H 490" />

        <!-- SF to FINALS -->
        <path d="M 675,210 H 705 V 530 H 675 M 705,370 H 735" />

        <!-- RIGHT SIDE BRANCHES -->
        <!-- SF to FINALS -->
        <path d="M 1015,90 H 985 V 170 H 1015 M 985,130 H 955" />
        <path d="M 1015,250 H 985 V 330 H 1015 M 985,290 H 955" />
        <path d="M 1015,410 H 985 V 490 H 1015 M 985,450 H 955" />
        <path d="M 1015,570 H 985 V 650 H 1015 M 985,610 H 955" />
    </svg>

    <!-- BRACKET CONTENT GRID -->
    <div class="bracket-grid">
        <!-- LEFT: R16 -->
        <div class="col" style="position: relative;">
            <div class="col-header">Round of 16</div>
            <div class="match-box"><div class="slot">Will Ospreay</div><div class="slot">Christian Cage</div></div>
            <div class="match-box"><div class="slot">Orange Cassidy</div><div class="slot">Bandido</div></div>
            <div class="match-box"><div class="slot">Hologram</div><div class="slot">Claudio Castagnoli</div></div>
            <div class="match-box"><div class="slot">Wheeler Yuta</div><div class="slot">Roderick Strong</div></div>
        </div>

        <!-- LEFT: QF -->
        <div class="col" style="position: relative;">
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
        <div class="col" style="position: relative;">
            <div class="col-header">Semifinals</div>
            <div class="match-box">
                <div class="slot">SF Slot 1</div>
                <div class="slot">SF Slot 2</div>
            </div>
        </div>

        <!-- CENTER: FINALS -->
        <div class="col-finals" style="position: relative;">
            <div class="col-header">Finals</div>
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
        <div class="col" style="position: relative;">
            <div class="col-header">Semifinals</div>
            <div class="match-box">
                <div class="slot">SF Slot 1</div>
                <div class="slot">SF Slot 2</div>
            </div>
        </div>

        <!-- RIGHT: QF -->
        <div class="col" style="position: relative;">
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
        <div class="col" style="position: relative;">
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

# Render embedded HTML bracket with 720px fixed height canvas
components.html(polished_bracket_html, height=720, scrolling=True)
