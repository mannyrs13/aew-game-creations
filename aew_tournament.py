import streamlit as st
import random

st.set_page_config(page_title="AEW Tournament Generator", page_icon="🏆", layout="wide")

# --- ACCURATE AUGUST 2026 MALE AEW ROSTER ---
MENS_ROSTER = [
    "Will Ospreay", "MJF", "Swerve Strickland", "Hangman Adam Page", "Kazuchika Okada", "Samoa Joe", 
    "Darby Allin", "Eddie Kingston", "Jack Perry", "Orange Cassidy", "Mark Briscoe", "PAC", 
    "Daniel Garcia", "Konosuke Takeshita", "Ricochet", "Roderick Strong", "Claudio Castagnoli",
    "Kenny Omega", "Jon Moxley", "Kevin Knight", "Kyle Fletcher", "Shelton Benjamin", "Bobby Lashley", 
    "Hologram", "Christian Cage", "Buddy Matthews", "Brody King", "Sammy Guevara", "Katsuyori Shibata", 
    "Jay White", "Juice Robinson", "Hook", "The Beast Mortos", "Rush", "Wardlow", "Chris Jericho", 
    "Lio Rush", "Kyle O'Reilly", "Andrade El Idolo", "Brian Cage", "Lance Archer", "Wheeler Yuta", 
    "Trent Beretta", "Action Andretti", "Komander", "Scorpio Sky", "Bandido", "Mike Bailey", "Lee Johnson"
]

BOOKING_FREQUENCY = {
    "Jon Moxley": 4, "Roderick Strong": 4, "Konosuke Takeshita": 4, "Daniel Garcia": 4, "Kyle Fletcher": 4, 
    "Bandido": 4, "Mike Bailey": 4, "Claudio Castagnoli": 4, "Kevin Knight": 4, "Mark Briscoe": 4,
    "Ricochet": 3, "Kyle O'Reilly": 3, "Brody King": 3, "Wheeler Yuta": 3, "Samoa Joe": 3, 
    "Kazuchika Okada": 3, "Adam Page": 3, "Katsuyori Shibata": 3, "Orange Cassidy": 3, "Andrade El Idolo": 3,
    "Swerve Strickland": 2, "Will Ospreay": 2, "The Beast Mortos": 2, "Lance Archer": 2, 
    "Bobby Lashley": 2, "Shelton Benjamin": 2, "PAC": 2, "Hook": 2, "Hologram": 2, "Rush": 2,
    "MJF": 1, "Kenny Omega": 1, "Eddie Kingston": 1, "Darby Allin": 1, "Chris Jericho": 1, 
    "Jay White": 1, "Christian Cage": 1, "Juice Robinson": 1, "Komander": 1, "Lio Rush": 1, 
    "Brian Cage": 1, "Sammy Guevara": 1, "Trent Beretta": 1, "Action Andretti": 1, 
    "Scorpio Sky": 1, "Buddy Matthews": 1, "Wardlow": 1, "Lee Johnson": 1
}

# --- STAR POWER SCORING DATABASE (Out of 100) ---
STAR_POWER_DB = {
    "Will Ospreay": 98, "MJF": 97, "Kenny Omega": 97, "Jon Moxley": 96, "Kazuchika Okada": 96, "Swerve Strickland": 95, 
    "Christian Cage": 92, "Hangman Adam Page": 90, "Jay White": 90, "Darby Allin": 89, "Samoa Joe": 88, 
    "Bobby Lashley": 88, "Chris Jericho": 87, "Orange Cassidy": 87, "PAC": 86, "Claudio Castagnoli": 86, 
    "Eddie Kingston": 85, "Konosuke Takeshita": 85, "Andrade El Idolo": 85, "Ricochet": 84, "Katsuyori Shibata": 84, 
    "Bandido": 84, "Mark Briscoe": 83, "Jack Perry": 82, "Buddy Matthews": 82, "Rush": 82, "Mike Bailey": 82, 
    "Kevin Knight": 83, "Shelton Benjamin": 81, "Brody King": 81, "Hook": 81, "Roderick Strong": 80, 
    "Juice Robinson": 80, "Wardlow": 80, "Kyle O'Reilly": 80, "Kyle Fletcher": 79, "Sammy Guevara": 79, 
    "Brian Cage": 79, "Daniel Garcia": 78, "Wheeler Yuta": 78, "Lio Rush": 78, "The Beast Mortos": 77, 
    "Lance Archer": 77, "Trent Beretta": 76, "Hologram": 75, "Scorpio Sky": 75, "Lee Johnson": 75, 
    "Komander": 74, "Action Andretti": 71
}

# --- LOGIC ENGINE ---
def draw_wrestler():
    avail = [w for w in MENS_ROSTER if w not in st.session_state.used_talent]
    if avail:
        weights = [BOOKING_FREQUENCY.get(w, 2) for w in avail]
        drawn = random.choices(avail, weights=weights, k=1)[0]
        st.session_state.current_draw = drawn
        st.session_state.used_talent.append(drawn)

def calc_match_score(p1, p2):
    s1 = STAR_POWER_DB.get(p1, 75)
    s2 = STAR_POWER_DB.get(p2, 75)
    base = (s1 + s2) / 2
    var = random.uniform(-2.0, 4.0)
    return min(100.0, max(0.0, base + var))

# --- STATE INITIALIZATION ---
if "tourney_init" not in st.session_state:
    st.session_state.r16 = [None] * 16
    st.session_state.qf = [None] * 8
    st.session_state.sf = [None] * 4
    st.session_state.finals = [None] * 2
    st.session_state.champion = None
    
    st.session_state.scores_r16 = [0.0] * 8
    st.session_state.scores_qf = [0.0] * 4
    st.session_state.scores_sf = [0.0] * 2
    st.session_state.score_finals = 0.0
    
    st.session_state.used_talent = []
    st.session_state.current_draw = None
    st.session_state.draft_complete = False
    st.session_state.tourney_init = True
    draw_wrestler() # Auto-draw the first wrestler on load

def reset_tournament():
    st.session_state.r16 = [None] * 16
    st.session_state.qf = [None] * 8
    st.session_state.sf = [None] * 4
    st.session_state.finals = [None] * 2
    st.session_state.champion = None
    
    st.session_state.scores_r16 = [0.0] * 8
    st.session_state.scores_qf = [0.0] * 4
    st.session_state.scores_sf = [0.0] * 2
    st.session_state.score_finals = 0.0
    
    st.session_state.used_talent = []
    st.session_state.current_draw = None
    st.session_state.draft_complete = False
    draw_wrestler() # Auto-draw the first wrestler on reset

def cascade_reset(stage, slot_idx):
    if stage == "qf":
        removed = st.session_state.qf[slot_idx]
        st.session_state.qf[slot_idx] = None
        st.session_state.scores_r16[slot_idx] = 0.0
        if removed:
            sf_idx = slot_idx // 2
            if st.session_state.sf[sf_idx] == removed:
                cascade_reset("sf", sf_idx)
    elif stage == "sf":
        removed = st.session_state.sf[slot_idx]
        st.session_state.sf[slot_idx] = None
        st.session_state.scores_qf[slot_idx] = 0.0
        if removed:
            final_idx = slot_idx // 2
            if st.session_state.finals[final_idx] == removed:
                cascade_reset("finals", final_idx)
    elif stage == "finals":
        removed = st.session_state.finals[slot_idx]
        st.session_state.finals[slot_idx] = None
        st.session_state.scores_sf[slot_idx] = 0.0
        if removed and st.session_state.champion == removed:
            st.session_state.champion = None
            st.session_state.score_finals = 0.0

def handle_click(stage, idx):
    # DRAFT PHASE
    if not st.session_state.draft_complete:
        if stage == "r16" and st.session_state.current_draw:
            if st.session_state.r16[idx] is None:
                st.session_state.r16[idx] = st.session_state.current_draw
                st.session_state.current_draw = None
                
                if None not in st.session_state.r16:
                    st.session_state.draft_complete = True
                else:
                    draw_wrestler() # Auto-draw the next wrestler immediately
        return

    # TOURNAMENT PHASE WITH SCORING
    if stage == "r16":
        match_idx = idx // 2
        p1 = st.session_state.r16[match_idx * 2]
        p2 = st.session_state.r16[match_idx * 2 + 1]
        clicked = st.session_state.r16[idx]
        if p1 and p2 and clicked:
            if st.session_state.qf[match_idx] == clicked:
                cascade_reset("qf", match_idx)
            else:
                cascade_reset("qf", match_idx)
                st.session_state.qf[match_idx] = clicked
                st.session_state.scores_r16[match_idx] = calc_match_score(p1, p2)

    elif stage == "qf":
        match_idx = idx // 2
        p1 = st.session_state.qf[match_idx * 2]
        p2 = st.session_state.qf[match_idx * 2 + 1]
        clicked = st.session_state.qf[idx]
        if p1 and p2 and clicked:
            if st.session_state.sf[match_idx] == clicked:
                cascade_reset("sf", match_idx)
            else:
                cascade_reset("sf", match_idx)
                st.session_state.sf[match_idx] = clicked
                st.session_state.scores_qf[match_idx] = calc_match_score(p1, p2)

    elif stage == "sf":
        match_idx = idx // 2
        p1 = st.session_state.sf[match_idx * 2]
        p2 = st.session_state.sf[match_idx * 2 + 1]
        clicked = st.session_state.sf[idx]
        if p1 and p2 and clicked:
            if st.session_state.finals[match_idx] == clicked:
                cascade_reset("finals", match_idx)
            else:
                cascade_reset("finals", match_idx)
                st.session_state.finals[match_idx] = clicked
                st.session_state.scores_sf[match_idx] = calc_match_score(p1, p2)

    elif stage == "finals":
        p1 = st.session_state.finals[0]
        p2 = st.session_state.finals[1]
        clicked = st.session_state.finals[idx]
        if p1 and p2 and clicked:
            if st.session_state.champion == clicked:
                st.session_state.champion = None
                st.session_state.score_finals = 0.0
            else:
                st.session_state.champion = clicked
                st.session_state.score_finals = calc_match_score(p1, p2)

# --- UI RENDERING ---
st.title("AEW 16-Man Tournament Generator")

ctrl1, ctrl2 = st.columns([1, 3])
with ctrl1:
    if st.button("🚨 NEW TOURNAMENT", use_container_width=True):
        reset_tournament()
        st.rerun()
with ctrl2:
    if st.session_state.champion:
        all_scores = st.session_state.scores_r16 + st.session_state.scores_qf + st.session_state.scores_sf + [st.session_state.score_finals]
        avg_score = sum(all_scores) / len(all_scores)
        st.success(f"🏆 {st.session_state.champion.upper()} WINS THE TOURNAMENT! (Final Grade: {avg_score:.1f} / 100) 🏆")
    elif st.session_state.draft_complete:
        st.info("DRAFT COMPLETE! Click on match participants to advance winners.")
    elif st.session_state.current_draw:
        st.warning(f"**ON THE CLOCK:** {st.session_state.current_draw} (Click an empty R16 slot to place)")

st.markdown("---")

# --- 7-COLUMN BRACKET LAYOUT ---
c0, c1, c2, c3, c4, c5, c6 = st.columns(7)

def render_btn(col, label, stage, idx, state_list, score_list=None):
    name = state_list[idx]
    
    if not st.session_state.draft_complete:
        if stage == "r16":
            btn_text = name if name else ("Place Here" if st.session_state.current_draw else label)
            btn_type = "secondary" if not name and not st.session_state.current_draw else "primary"
        else:
            btn_text = label
            btn_type = "secondary"
    else:
        if name:
            btn_text = f"{name} (⭐ {score_list[idx]:.1f})" if score_list and score_list[idx] > 0 else name
            btn_type = "primary"
        else:
            btn_text = label
            btn_type = "secondary"
        
    with col:
        if st.button(btn_text, key=f"{stage}_{idx}", use_container_width=True, type=btn_type):
            handle_click(stage, idx)
            st.rerun()

# LEFT SIDE
with c0:
    st.markdown("**Round of 16**")
    for i in range(8):
        render_btn(c0, f"Slot {i+1}", "r16", i, st.session_state.r16)
        if i % 2 == 1 and i != 7: st.write("")

with c1:
    st.markdown("**Quarterfinals**")
    st.write("")
    for i in range(4):
        render_btn(c1, "QF Slot", "qf", i, st.session_state.qf, st.session_state.scores_r16)
        if i != 3: st.write("")
        st.write("")
        
with c2:
    st.markdown("**Semifinals**")
    st.write("\n\n")
    for i in range(2):
        render_btn(c2, "SF Slot", "sf", i, st.session_state.sf, st.session_state.scores_qf)
        if i == 0: st.write("\n\n\n\n\n\n")

# CENTER
with c3:
    st.markdown("<h3 style='text-align: center; color: gold;'>FINALS</h3>", unsafe_allow_html=True)
    st.write("\n\n\n")
    render_btn(c3, "Finalist 1", "finals", 0, st.session_state.finals, st.session_state.scores_sf)
    st.markdown("<h4 style='text-align: center; color: gray;'>VS</h4>", unsafe_allow_html=True)
    render_btn(c3, "Finalist 2", "finals", 1, st.session_state.finals, st.session_state.scores_sf)
    
    st.write("\n\n")
    st.markdown("<h4 style='text-align: center;'>👑 CHAMPION 👑</h4>", unsafe_allow_html=True)
    if st.session_state.champion:
        st.button(f"{st.session_state.champion} (⭐ {st.session_state.score_finals:.1f})", key="champ_btn", type="primary", use_container_width=True)
    else:
        st.button("???", key="champ_btn_empty", disabled=True, use_container_width=True)

# RIGHT SIDE
with c4:
    st.markdown("**Semifinals**")
    st.write("\n\n")
    for i in range(2, 4):
        render_btn(c4, "SF Slot", "sf", i, st.session_state.sf, st.session_state.scores_qf)
        if i == 2: st.write("\n\n\n\n\n\n")

with c5:
    st.markdown("**Quarterfinals**")
    st.write("")
    for i in range(4, 8):
        render_btn(c5, "QF Slot", "qf", i, st.session_state.qf, st.session_state.scores_r16)
        if i != 7: st.write("")
        st.write("")

with c6:
    st.markdown("**Round of 16**")
    for i in range(8, 16):
        render_btn(c6, f"Slot {i+9}", "r16", i, st.session_state.r16)
        if i % 2 == 1 and i != 15: st.write("")
