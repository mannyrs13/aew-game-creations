import streamlit as st
import random

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="AEW PPV GM Sorter",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. AEW UNIVERSE DATA & ROSTERS ---
PPV_EVENTS = [
    "AEW Revolution", "AEW Dynasty", "AEW Double or Nothing", 
    "AEW x NJPW Forbidden Door", "AEW All In", "AEW All Out", 
    "AEW WrestleDream", "AEW Full Gear", "AEW Worlds End"
]
MATCH_COUNTS = [8, 9, 10]

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

WOMENS_ROSTER = [
    "Mercedes Moné", "Thekla", "Hikaru Shida", "Jamie Hayter", "Toni Storm", "Britt Baker", 
    "Kris Statlander", "Deonna Purrazzo", "Mina Shirakawa", "Athena", "Julia Hart", "Willow Nightingale", 
    "Maya World", "Anna Jay", "Queen Aminata", "Kamille", "Serena Deeb", "Skye Blue", "Thunder Rosa", 
    "Billie Starkz", "Red Velvet", "Harley Cameron", "Megan Bayne", "Zeuxis",  
    "Diamante", "Penelope Ford", "Taya Valkyrie", "Emi Sakura", "Lena Kross", "Alex Windsor"
]

TAG_ROSTER = [
    "The Young Bucks", "FTR", "The Death Riders", "The Don Callis Family", "The Gunns", "The Hurt Syndicate", 
    "Private Party", "The Outrunners", "MxM Collection", "Top Flight", "The Righteous", "The Premier Athletes", 
    "La Facción Ingobernable", "Motor City Machine Guns", "Dark Order", "Gates of Agony"
]

WOMENS_TAG_ROSTER = [
    "Divine Dominion", "The Babes of Wrath", "Timeless Love Bombs", "Sisters of Sin", "The Brawling Birds"
]

TRIOS_ROSTER = [
    "The Elite", "The Death Riders", "The Conglomeration", "The Hurt Syndicate", "The Don Callis Family", 
    "Undisputed Kingdom", "Bang Bang Gang", "La Facción Ingobernable", "Dark Order", "The Acclaimed & Daddy Ass",
    "Top Flight & Action Andretti"
]

CROSSOVER_MENS = ["Shingo Takagi", "Zack Sabre Jr.", "Hiromu Takahashi", "Hiroshi Tanahashi", "Yota Tsuji", "Tomohiro Ishii", "Gabe Kidd", "Hechicero", "Mistico", "Atlantis Jr.", "Mascara Dorada", "Volador Jr.", "Titan", "El Desperado"]
CROSSOVER_WOMENS = ["Mayu Iwatani", "AZM", "Starlight Kid", "Momo Watanabe", "Persephone"]
CROSSOVER_TAG = ["TMDK", "Bishamon", "Guerreros Laguneros"]
CROSSOVER_TRIOS = ["TMDK", "Mistico, Volador Jr. & Atlantis Jr."]

BOOKING_FREQUENCY = {
    "Jon Moxley": 4, "Roderick Strong": 4, "Konosuke Takeshita": 4, "Daniel Garcia": 4, "Kyle Fletcher": 4, 
    "Bandido": 4, "Mike Bailey": 4, "Claudio Castagnoli": 4, "Kevin Knight": 4, "Mark Briscoe": 4,
    "Ricochet": 3, "Kyle O'Reilly": 3, "Brody King": 3, "Wheeler Yuta": 3, "Samoa Joe": 3, 
    "Kazuchika Okada": 3, "Adam Page": 3, "Katsuyori Shibata": 3, "Orange Cassidy": 3, 
    "Andrade El Idolo": 3,
    "Swerve Strickland": 2, "Will Ospreay": 2, "The Beast Mortos": 2, "Lance Archer": 2, 
    "Bobby Lashley": 2, "Shelton Benjamin": 2, "PAC": 2, "Hook": 2, "Hologram": 2, "Rush": 2,
    "MJF": 1, "Kenny Omega": 1, "Eddie Kingston": 1, "Darby Allin": 1, "Chris Jericho": 1, 
    "Jay White": 1, "Christian Cage": 1, "Juice Robinson": 1, "Komander": 1, "Lio Rush": 1, 
    "Brian Cage": 1, "Sammy Guevara": 1, "Trent Beretta": 1, "Action Andretti": 1, 
    "Scorpio Sky": 1, "Buddy Matthews": 1, "Wardlow": 1, "Lee Johnson": 1,
    "Megan Bayne": 4, "Toni Storm": 3, "Mercedes Moné": 3, "Willow Nightingale": 3, "Harley Cameron": 3, 
    "Julia Hart": 3,
    "Kris Statlander": 2, "Skye Blue": 2, "Thekla": 2, "Mina Shirakawa": 2, "Jamie Hayter": 2, 
    "Alex Windsor": 2, "Athena": 2,
    "Hikaru Shida": 1, "Deonna Purrazzo": 1, "Thunder Rosa": 1, "Kamille": 1, "Zeuxis": 1, 
    "Serena Deeb": 1, "Queen Aminata": 1, "Billie Starkz": 1, "Red Velvet": 1, 
    "Anna Jay": 1, "Maya World": 1, "Taya Valkyrie": 1, "Penelope Ford": 1, 
    "Diamante": 1, "Emi Sakura": 1, "Lena Kross": 1, "Britt Baker": 1,
    "FTR": 3, "The Young Bucks": 3, "The Death Riders": 4, "The Don Callis Family": 4, "The Conglomeration": 4, 
    "The Hurt Syndicate": 2, "Bang Bang Gang": 2, "Motor City Machine Guns": 1, "The Outrunners": 2, 
    "Private Party": 1, "La Facción Ingobernable": 2, 
    "Top Flight": 2, "The Gunns": 2, "MxM Collection": 1, "Undisputed Kingdom": 4, 
    "The Righteous": 1, "Gates of Agony": 2, "Dark Order": 1, "SkyFlight": 1, 
    "The Premier Athletes": 1, "The Elite": 3, "The Acclaimed & Daddy Ass": 4, "Top Flight & Action Andretti": 2,
    "Timeless Love Bombs": 3, "The Babes of Wrath": 3, "Sisters of Sin": 2, "The Brawling Birds": 2, "Divine Dominion": 3,
    "Zack Sabre Jr.": 3, "Shingo Takagi": 3, "Mistico": 3, "Hechicero": 3, "Hiromu Takahashi": 2, 
    "Yota Tsuji": 2, "El Desperado": 2, "Tomohiro Ishii": 2, "Gabe Kidd": 2, "Volador Jr.": 2, 
    "Atlantis Jr.": 2, "Mascara Dorada": 2, "Hiroshi Tanahashi": 1, "Titan": 1,
    "Mayu Iwatani": 3, "Starlight Kid": 3, "AZM": 2, "Momo Watanabe": 2, "Persephone": 2,
    "TMDK": 3, "Bishamon": 2, "Guerreros Laguneros": 2, "Mistico, Volador Jr. & Atlantis Jr.": 2
}

STAR_POWER_DB = {
    "Will Ospreay": 98, "MJF": 97, "Kenny Omega": 97, "Jon Moxley": 96, "Kazuchika Okada": 96, 
    "Swerve Strickland": 95, "Zack Sabre Jr.": 94, "Shingo Takagi": 93, 
    "Christian Cage": 92, "Mistico": 92, "Hiromu Takahashi": 91, "Hiroshi Tanahashi": 90, 
    "Hangman Adam Page": 90, "Jay White": 90, "Darby Allin": 89, "Samoa Joe": 88, 
    "Bobby Lashley": 88, "Chris Jericho": 87, "Orange Cassidy": 87, "Tomohiro Ishii": 87, 
    "PAC": 86, "Claudio Castagnoli": 86, "Hechicero": 86, "Yota Tsuji": 86, "Eddie Kingston": 85, 
    "Konosuke Takeshita": 85, "Andrade El Idolo": 85, "El Desperado": 85, "Ricochet": 84, 
    "Katsuyori Shibata": 84, "Bandido": 84, "Gabe Kidd": 84, "Volador Jr.": 84, "Mark Briscoe": 83, 
    "Jack Perry": 82, "Buddy Matthews": 82, "Rush": 82, "Atlantis Jr.": 82, "Mascara Dorada": 82, 
    "Mike Bailey": 82, "Kevin Knight": 83, "Shelton Benjamin": 81, "Brody King": 81, "Hook": 81, 
    "Roderick Strong": 80, "Juice Robinson": 80, "Wardlow": 80, "Kyle O'Reilly": 80, "Titan": 80, 
    "Kyle Fletcher": 79, "Sammy Guevara": 79, "Brian Cage": 79, "Daniel Garcia": 78, "Wheeler Yuta": 78, 
    "Lio Rush": 78, "The Beast Mortos": 77, "Lance Archer": 77, "Trent Beretta": 76, "Hologram": 75, 
    "Scorpio Sky": 75, "Lee Johnson": 75, "Komander": 74, "Action Andretti": 71,
    "Mercedes Moné": 96, "Toni Storm": 94, "Mayu Iwatani": 93, "Jamie Hayter": 92, "Britt Baker": 91, 
    "Athena": 89, "Hikaru Shida": 88, "Willow Nightingale": 88, "Mina Shirakawa": 86, "Starlight Kid": 86, 
    "Kris Statlander": 85, "Thunder Rosa": 85, "AZM": 85, "Julia Hart": 84, "Momo Watanabe": 84, 
    "Deonna Purrazzo": 83, "Serena Deeb": 82, "Kamille": 80, "Persephone": 80, "Skye Blue": 79, 
    "Megan Bayne": 79, "Queen Aminata": 78, "Taya Valkyrie": 77, "Billie Starkz": 76, "Thekla": 75, 
    "Anna Jay": 75, "Zeuxis": 75, "Red Velvet": 74, "Emi Sakura": 74, "Maya World": 73, "Alex Windsor": 73, 
    "Harley Cameron": 72, "Penelope Ford": 72, "Lena Kross": 72, "Diamante": 71,
    "The Elite": 95, "The Young Bucks": 95, "FTR": 94, "The Death Riders": 93, "Timeless Love Bombs": 90, 
    "The Hurt Syndicate": 89, "Motor City Machine Guns": 88, "TMDK": 88, "Mistico, Volador Jr. & Atlantis Jr.": 88, 
    "Bang Bang Gang": 87, "The Conglomeration": 86, "Bishamon": 86, "The Don Callis Family": 85, 
    "The Acclaimed & Daddy Ass": 85, "The Brawling Birds": 85, "Guerreros Laguneros": 85, "The Babes of Wrath": 84, 
    "La Facción Ingobernable": 83, "The Gunns": 82, "Sisters of Sin": 82, "Undisputed Kingdom": 81, "Top Flight": 80, 
    "Top Flight & Action Andretti": 79, "The Outrunners": 79, "Private Party": 78, "SkyFlight": 78, 
    "MxM Collection": 77, "The Righteous": 76, "Gates of Agony": 76, "Divine Dominion": 76, "Dark Order": 75, "The Premier Athletes": 74
}

# --- 3. PREMIUM FRIENDLY AEW THEME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&display=swap');

    html, body, [data-testid="stAppViewContainer"], .stApp {
        overflow-y: auto !important;
        height: auto !important;
    }

    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #080a0e; }
    ::-webkit-scrollbar-thumb { background: #ffd700; border-radius: 5px; }
    ::-webkit-scrollbar-thumb:hover { background: #ef4444; }

    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 98% !important;
    }

    .stApp {
        background: radial-gradient(circle at center, #1c2333 0%, #090c12 100%) !important;
    }

    .aew-main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 900;
        color: #ffd700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-top: 10px !important;
        margin-bottom: 0.8rem;
        font-family: 'Impact', 'Montserrat', sans-serif;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.6), 0 0 35px rgba(255, 215, 0, 0.3);
    }

    .clock-banner {
        background: linear-gradient(90deg, #1e2638 0%, #2a344d 50%, #1e2638 100%);
        border: 2px solid #ffd700;
        border-radius: 10px;
        padding: 12px 20px;
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.25);
        margin-bottom: 18px;
    }

    .clock-text {
        color: #ffd700;
        font-size: 1.15rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .clock-sub {
        color: #00ff66;
        font-weight: 800;
        font-size: 0.92rem;
        margin-left: 10px;
    }

    div.stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #00ff66 0%, #00cc52 100%) !important;
        color: #000000 !important;
        border: 1px solid #66ff99 !important;
        border-radius: 6px !important;
        padding: 0.55rem 0.2rem !important;
        font-weight: 900 !important;
        font-size: 0.85rem !important;
        font-family: 'Montserrat', sans-serif !important;
        letter-spacing: 0.04em !important;
        text-transform: uppercase !important;
        box-shadow: 0 4px 12px rgba(0, 255, 102, 0.3) !important;
        transition: all 0.15s ease-in-out !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #ffd700 0%, #d4af37 100%) !important;
        color: #000000 !important;
        border-color: #ffe566 !important;
        box-shadow: 0 0 18px rgba(255, 215, 0, 0.6) !important;
        transform: scale(1.02);
    }

    div.stButton > button:disabled {
        background: #182030 !important;
        color: #52627a !important;
        border: 1px solid #2b384e !important;
        opacity: 0.55 !important;
        font-weight: 800 !important;
    }

    .placed-slot {
        background: linear-gradient(180deg, #1e283d 0%, #111724 100%);
        border: 1px solid #2e3c59;
        border-left: 5px solid #00ff66;
        border-radius: 6px;
        padding: 10px 14px;
        color: #f1f5f9;
        font-weight: 800;
        font-size: 0.9rem;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #121824 !important;
        border: 1px solid #253147 !important;
        border-left: 4px solid #ffd700 !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        margin-bottom: 14px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. SESSION STATE INITIALIZATION ---
if "card_data" not in st.session_state:
    st.session_state.card_data = []
if "used_talent" not in st.session_state:
    st.session_state.used_talent = []
if "current_draw" not in st.session_state:
    st.session_state.current_draw = None
if "current_draw_type" not in st.session_state:
    st.session_state.current_draw_type = None
if "selected_ppv" not in st.session_state:
    st.session_state.selected_ppv = ""
if "is_fd" not in st.session_state:
    st.session_state.is_fd = False

# --- 5. HELPER FUNCTIONS ---
def get_slot_type(match_type):
    if "Women's World Tag" in match_type: return "Womens Tag"
    if "Women" in match_type or "TBS" in match_type: return "Womens Singles"
    if "World Tag Team" in match_type: return "Mens Tag"
    if "Trios" in match_type: return "Trios"
    if "Anarchy" in match_type: return "Mens Singles"
    return "Mens Singles"

def get_pool_for_type(slot_type, is_fd):
    if slot_type == "Womens Tag": return WOMENS_TAG_ROSTER
    if slot_type == "Womens Singles": return WOMENS_ROSTER + (CROSSOVER_WOMENS if is_fd else [])
    if slot_type == "Mens Tag": return TAG_ROSTER + (CROSSOVER_TAG if is_fd else [])
    if slot_type == "Trios": return TRIOS_ROSTER + (CROSSOVER_TRIOS if is_fd else [])
    return MENS_ROSTER + (CROSSOVER_MENS if is_fd else [])

def calc_score(slots):
    scores = [STAR_POWER_DB.get(s["filled"].replace(" (c)", ""), 75) for s in slots if s["filled"]]
    base = sum(scores) / len(scores) if scores else 75
    var = random.uniform(-2.0, 4.0)
    return min(100.0, max(0.0, base + var))

def auto_draw_next_talent():
    open_types = set()
    for m in st.session_state.card_data:
        for slot in m["slots"]:
            if slot["filled"] is None:
                open_types.add(slot["type"])
                
    if not open_types:
        st.session_state.current_draw = "CARD COMPLETE!"
        st.session_state.current_draw_type = None
        return

    chosen_type = random.choice(list(open_types))
    pool = get_pool_for_type(chosen_type, st.session_state.is_fd)
    avail = [t for t in pool if t not in st.session_state.used_talent]
    
    if avail:
        weights = [BOOKING_FREQUENCY.get(t, 2) for t in avail]
        drawn = random.choices(avail, weights=weights, k=1)[0]
        st.session_state.current_draw = drawn
        st.session_state.current_draw_type = chosen_type
        st.session_state.used_talent.append(drawn)
    else:
        st.session_state.current_draw = "Mystery Opponent"
        st.session_state.current_draw_type = chosen_type

def generate_skeleton():
    st.session_state.selected_ppv = random.choice(PPV_EVENTS)
    count = random.choice(MATCH_COUNTS)
    st.session_state.is_fd = "FORBIDDEN DOOR" in st.session_state.selected_ppv.upper()
    
    anchor_matches = ["AEW Women's World Championship", "AEW World Championship"]
    if "DOUBLE OR NOTHING" in st.session_state.selected_ppv.upper(): 
        anchor_matches.append("Anarchy in the Arena")
        
    pool = ["AEW World Tag Team Championship", "AEW Women's World Tag Team Championship", "AEW World Trios Championship", "AEW Continental Championship", "AEW International Championship", "AEW National Championship", "AEW TNT Championship", "AEW TBS Championship", "Men's Regular Match", "Women's Regular Match"]
    
    if st.session_state.is_fd:
        pool.remove("Men's Regular Match")
        pool.remove("Women's Regular Match")
        pool.extend(["Men's Owen Hart Final", "Women's Owen Hart Final"])
    if "WORLDS END" in st.session_state.selected_ppv.upper():
        pool.remove("AEW Continental Championship")
        pool.append("Continental Classic Final")

    st.session_state.card_data = []
    for idx in range(count):
        matches_remaining = count - idx
        is_anchor = matches_remaining <= len(anchor_matches)
        raw_type = anchor_matches[-matches_remaining] if is_anchor else random.choice(pool)
        if not is_anchor: pool.remove(raw_type)
            
        if "Anarchy in the Arena" in raw_type:
            num_slots = random.choice([8, 10]) 
            stip = f"{num_slots}-Man"
        elif "Tag" in raw_type:
            stipulations = [("Standard", 2), ("3-Way", 3), ("4-Way", 4)]
            stip, num_slots = random.choices(stipulations, weights=[70, 20, 10])[0]
        elif "Trios" in raw_type:
            stipulations = [("Standard", 2), ("3-Way", 3)]
            stip, num_slots = random.choices(stipulations, weights=[80, 20])[0]
        else:
            stipulations = [("Standard", 2), ("Triple Threat", 3), ("Fatal 4-Way", 4)]
            stip, num_slots = random.choices(stipulations, weights=[70, 20, 10])[0]
        
        display_type = f"{raw_type} ({stip})" if stip != "Standard" else raw_type
        slot_type = get_slot_type(raw_type)
        
        slots = [{"id": i, "type": slot_type, "filled": None} for i in range(num_slots)]
        st.session_state.card_data.append({"id": idx, "type": display_type, "slots": slots, "score": 0.0})
        
    st.session_state.used_talent = []
    auto_draw_next_talent()
    st.rerun()

def place_talent(m_idx, s_idx):
    st.session_state.card_data[m_idx]["slots"][s_idx]["filled"] = st.session_state.current_draw
    
    slots = st.session_state.card_data[m_idx]["slots"]
    if all(s["filled"] is not None for s in slots):
        st.session_state.card_data[m_idx]["score"] = calc_score(slots)
        
    auto_draw_next_talent()
    st.rerun()

# --- 6. FLOATING MODAL POP-UP DIALOG (REPLACES DESKTOP POPUP) ---
@st.dialog("🏆 FINAL CARD & SCORES")
def show_final_card_dialog():
    ppv_title = st.session_state.selected_ppv.upper()
    completed_scores = [m["score"] for m in st.session_state.card_data if m["score"] > 0]
    
    if len(completed_scores) == len(st.session_state.card_data) and len(st.session_state.card_data) > 0:
        avg_score = sum(completed_scores) / len(completed_scores)
        overall_summary = f"OVERALL EVENT SCORE: {avg_score:.1f} / 100"
    elif completed_scores:
        avg_score = sum(completed_scores) / len(completed_scores)
        overall_summary = f"CURRENT EVENT SCORE: {avg_score:.1f} / 100 (Incomplete Card)"
    else:
        overall_summary = "OVERALL EVENT SCORE: TBD (Incomplete Matches)"

    full_plain_text = f"=== {ppv_title} ===\n{overall_summary}\n\n"
    total_matches = len(st.session_state.card_data)
    
    anchor_matches = ["AEW Women's World Championship", "AEW World Championship"]
    if "DOUBLE OR NOTHING" in st.session_state.selected_ppv.upper(): 
        anchor_matches.append("Anarchy in the Arena")

    for i, match in enumerate(st.session_state.card_data):
        lbl_num = f"MATCH {i+1}"
        if i == total_matches - 1: lbl_num = "🌟 MAIN EVENT 🌟"
        elif i == total_matches - 2 and len(anchor_matches) >= 2: lbl_num = "⚔️ CO-MAIN EVENT ⚔️"
        elif i == total_matches - 3 and len(anchor_matches) == 3: lbl_num = "⚔️ CO-MAIN EVENT ⚔️"

        wrestlers = [s["filled"] if s["filled"] else "TBD" for s in match["slots"]]
        vs_string = " vs. ".join(wrestlers)
        score_text = f"{match['score']:.1f} / 100" if match["score"] > 0 else "Pending"

        full_plain_text += f"{lbl_num}\n{match['type']}\n{vs_string}\nScore: {score_text}\n\n"
        if i < total_matches - 1:
            full_plain_text += "───────────\n\n"

    st.markdown("<p style='color: #888888; font-size: 0.85rem;'>Select all and copy (Ctrl+C / Cmd+C):</p>", unsafe_allow_html=True)
    st.text_area("Final Card Export", value=full_plain_text, height=350, label_visibility="collapsed")

# --- 7. TOP HEADER & CONTROL PANEL ---
st.markdown('<div class="aew-main-title">🏟️ AEW PPV GM SORTER</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 4])
with col1:
    btn_lbl = f"🚨 {st.session_state.selected_ppv.upper()}" if st.session_state.selected_ppv else "🚨 GENERATE CARD"
    if st.button(btn_lbl, type="primary"):
        generate_skeleton()

with col2:
    if st.session_state.current_draw:
        if st.session_state.current_draw == "CARD COMPLETE!":
            st.markdown("""
                <div class="clock-banner" style="border-color: #00ff66;">
                    <span class="clock-text" style="color: #00ff66;">🎉 CARD COMPLETE! ALL MATCHES BOOKED.</span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="clock-banner">
                    <span class="clock-text">ON THE CLOCK: <span style="color:#ffffff;">{st.session_state.current_draw}</span></span>
                    <span class="clock-sub">| TYPE: <span style="color:#ffd700;">{st.session_state.current_draw_type.upper()}</span></span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="clock-banner">
                <span class="clock-text" style="color: #888888;">CLICK 'GENERATE CARD' TO BEGIN</span>
            </div>
        """, unsafe_allow_html=True)

# --- 8. MATCH CARD GRID ---
curr_draw = st.session_state.current_draw
curr_type = st.session_state.current_draw_type

for m_idx, match in enumerate(st.session_state.card_data):
    with st.container(border=True):
        score_txt = f"Score: {match['score']:.1f} / 100" if match['score'] > 0 else "Pending"
        st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <h4 style="color: #ffd700; margin: 0; font-size: 1.15rem;">Match {m_idx + 1}: {match['type']}</h4>
                <span style="color: #00ff66; font-weight: 800; font-size: 0.95rem;">{score_txt}</span>
            </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(len(match["slots"]))
        for s_idx, slot in enumerate(match["slots"]):
            with cols[s_idx]:
                if slot["filled"]:
                    st.markdown(f'<div class="placed-slot">✅ {slot["filled"]}</div>', unsafe_allow_html=True)
                else:
                    is_valid = (curr_draw is not None) and (curr_draw != "CARD COMPLETE!") and (curr_type == slot["type"])
                    btn_text = "PLACE HERE" if is_valid else f"⛔ {slot['type'].upper()}"
                    
                    if st.button(btn_text, key=f"btn_{m_idx}_{s_idx}", disabled=not is_valid):
                        place_talent(m_idx, s_idx)

# --- 9. VIEW FINAL CARD BUTTON & FLOATING MODAL POP-UP ---
if st.session_state.card_data:
    st.markdown("<br>", unsafe_allow_html=True)
    col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
    with col_b2:
        if st.button("📋 VIEW FINAL CARD & SCORES", key="btn_view_final_card"):
            show_final_card_dialog()
