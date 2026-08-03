import streamlit as st
import random
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AEW PPV Booker", page_icon="🏆", layout="wide")

# --- AEW UNIVERSE DATA ---
PPV_EVENTS = [
    "AEW Revolution", "AEW Dynasty", "AEW Double or Nothing", 
    "AEW x NJPW Forbidden Door", "AEW All In", 
    "AEW All Out", "AEW WrestleDream", "AEW Full Gear", "AEW Worlds End"
]

MATCH_COUNTS = [8, 9, 10]

# --- ROSTER & DATABASES (IDENTICAL TO PREVIOUS VERSION) ---
MENS_ROSTER = [
    "Will Ospreay", "MJF", "Swerve Strickland", "Hangman Adam Page", "Kazuchika Okada", "Samoa Joe", 
    "Darby Allin", "Eddie Kingston", "Jack Perry", "Orange Cassidy", "Mark Briscoe", "PAC", 
    "Daniel Garcia", "Konosuke Takeshita", "Ricochet", "Roderick Strong", "Claudio Castagnoli",
    "Kenny Omega", "Jon Moxley", "Kevin Knight", "Kyle Fletcher", "Shelton Benjamin", "Bobby Lashley", 
    "Hologram", "Christian Cage", "Buddy Matthews", "Brody King", "Sammy Guevara", "Katsuyori Shibata", 
    "Jay White", "Juice Robinson", "Hook", "The Beast Mortos", "Rush", "Wardlow", "Chris Jericho", 
    "Lio Rush", "Kyle O'Reilly", "Andrade El Idolo", "Alex Shelley", "Chris Sabin", "Brian Cage", 
    "Lance Archer", "Wheeler Yuta", "Trent Beretta", "Action Andretti", "Komander", 
    "Scorpio Sky", "Bandido", "Mike Bailey", "Anthony Bowens", "Bishop Kaun", 
    "Toa Liona", "Lee Johnson"
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
    "Private Party", "The Outrunners", "MxM Collection", "Grizzled Young Veterans", "Kings of the Black Throne",
    "Top Flight", "The Righteous", "The Premier Athletes", "La Facción Ingobernable", 
    "Motor City Machine Guns", "Dark Order", "Gates of Agony", "Iron Savages", "Brodido"
]

WOMENS_TAG_ROSTER = [
    "Divine Dominion", "The Babes of Wrath", "Timeless Love Bombs", "Sisters of Sin", "The Brawling Birds"
]

TRIOS_ROSTER = [
    "The Elite", "The Death Riders", "The Conglomeration", "The Hurt Syndicate", "The Don Callis Family", 
    "SkyFlight", "Undisputed Kingdom", "Bang Bang Gang", "La Facción Ingobernable", 
    "Dark Order", "The Demand", "The Opps"
]

FACTIONS = [
    "The Elite", "The Death Riders", "The Conglomeration", "The Don Callis Family", "The Hurt Syndicate", 
    "Bang Bang Gang", "Undisputed Kingdom", "La Facción Ingobernable", "Dark Order",
    "The Demand", "The Opps"
]

CROSSOVER_MENS = ["Shingo Takagi", "Zack Sabre Jr.", "Hiromu Takahashi", "Hiroshi Tanahashi", "Yota Tsuji", "Tomohiro Ishii", "Gabe Kidd", "Hechicero", "Mistico", "Atlantis Jr.", "Mascara Dorada", "Volador Jr.", "Titan", "El Desperado"]
CROSSOVER_WOMENS = ["Mayu Iwatani", "AZM", "Starlight Kid", "Momo Watanabe", "Persephone"]
CROSSOVER_TAG = ["TMDK", "Bishamon", "Guerreros Laguneros"]
CROSSOVER_TRIOS = ["TMDK", "Mistico, Volador Jr. & Atlantis Jr."]

BOOKING_FREQUENCY = {
    # Men
    "Jon Moxley": 4, "Roderick Strong": 4, "Konosuke Takeshita": 4, "Daniel Garcia": 4, "Kyle Fletcher": 4, 
    "Bandido": 4, "Mike Bailey": 4, "Claudio Castagnoli": 4, "Kevin Knight": 4, "Mark Briscoe": 4,
    "Ricochet": 3, "Kyle O'Reilly": 3, "Brody King": 3, "Wheeler Yuta": 3, "Samoa Joe": 3, 
    "Kazuchika Okada": 3, "Adam Page": 3, "Katsuyori Shibata": 3, "Orange Cassidy": 3, 
    "Anthony Bowens": 3, "Andrade El Idolo": 3, "Swerve Strickland": 2, "Will Ospreay": 2, "The Beast Mortos": 2, "Lance Archer": 2, 
    "Bobby Lashley": 2, "Shelton Benjamin": 2, "PAC": 2, "Hook": 2, "Hologram": 2, "Rush": 2,
    "Bishop Kaun": 2, "Toa Liona": 2, "MJF": 1, "Kenny Omega": 1, "Eddie Kingston": 1, "Darby Allin": 1, "Chris Jericho": 1, 
    "Jay White": 1, "Christian Cage": 1, "Juice Robinson": 1, "Komander": 1, "Lio Rush": 1, 
    "Brian Cage": 1, "Sammy Guevara": 1, "Trent Beretta": 1, "Action Andretti": 1, 
    "Scorpio Sky": 1, "Buddy Matthews": 1, "Wardlow": 1, "Alex Shelley": 1, 
    "Chris Sabin": 1, "Lee Johnson": 1,
    
    # Women
    "Megan Bayne": 4, "Toni Storm": 3, "Mercedes Moné": 3, "Willow Nightingale": 3, "Harley Cameron": 3, "Julia Hart": 3,
    "Kris Statlander": 2, "Skye Blue": 2, "Thekla": 2, "Mina Shirakawa": 2, "Jamie Hayter": 2, "Alex Windsor": 2, "Athena": 2,
    "Hikaru Shida": 1, "Deonna Purrazzo": 1, "Thunder Rosa": 1, "Kamille": 1, "Zeuxis": 1, "Serena Deeb": 1, "Queen Aminata": 1, "Billie Starkz": 1, "Red Velvet": 1, "Anna Jay": 1, "Maya World": 1, "Taya Valkyrie": 1, "Penelope Ford": 1, "Diamante": 1, "Emi Sakura": 1, "Lena Kross": 1, "Britt Baker": 1,
    
    # Teams & Factions 
    "FTR": 3, "The Young Bucks": 3, "The Death Riders": 4, "The Don Callis Family": 4, "The Conglomeration": 4, "The Hurt Syndicate": 2, "Bang Bang Gang": 2, "Motor City Machine Guns": 1, "The Outrunners": 2, "Private Party": 1, "Kings of the Black Throne": 3, "La Facción Ingobernable": 2, "Top Flight": 2, "Grizzled Young Veterans": 1, "The Gunns": 2, "MxM Collection": 1, "Undisputed Kingdom": 4, "Brodido": 3, "The Righteous": 1, "Gates of Agony": 2, "Dark Order": 1, "SkyFlight": 1, "The Premier Athletes": 1, "Iron Savages": 1, "The Elite": 3, "The Demand": 4, "The Opps": 4,
    "Timeless Love Bombs": 3, "The Babes of Wrath": 3, "Sisters of Sin": 2, "The Brawling Birds": 2, "Divine Dominion": 3,
    
    # Crossovers 
    "Zack Sabre Jr.": 3, "Shingo Takagi": 3, "Mistico": 3, "Hechicero": 3, "Hiromu Takahashi": 2, "Yota Tsuji": 2, "El Desperado": 2, "Tomohiro Ishii": 2, "Gabe Kidd": 2, "Volador Jr.": 2, "Atlantis Jr.": 2, "Mascara Dorada": 2, "Hiroshi Tanahashi": 1, "Titan": 1,
    "Mayu Iwatani": 3, "Starlight Kid": 3, "AZM": 2, "Momo Watanabe": 2, "Persephone": 2,
    "TMDK": 3, "Bishamon": 2, "Guerreros Laguneros": 2, "Mistico, Volador Jr. & Atlantis Jr.": 2
}

STAR_POWER_DB = {
    # Men's Top Tier & Crossover Megastars
    "Will Ospreay": 98, "MJF": 97, "Kenny Omega": 97, "Jon Moxley": 96, "Kazuchika Okada": 96, "Swerve Strickland": 95, "Zack Sabre Jr.": 94, "Shingo Takagi": 93, "Christian Cage": 92, "Mistico": 92, "Hiromu Takahashi": 91, "Hiroshi Tanahashi": 90, "Hangman Adam Page": 90, "Jay White": 90,
    # Men's Upper Midcard
    "Darby Allin": 89, "Samoa Joe": 88, "Bobby Lashley": 88, "Chris Jericho": 87, "Orange Cassidy": 87, "Tomohiro Ishii": 87, "PAC": 86, "Claudio Castagnoli": 86, "Hechicero": 86, "Yota Tsuji": 86, "Eddie Kingston": 85, "Konosuke Takeshita": 85, "Andrade El Idolo": 85, "El Desperado": 85, "Ricochet": 84, "Katsuyori Shibata": 84, "Bandido": 84, "Gabe Kidd": 84, "Volador Jr.": 84, "Mark Briscoe": 83, "Jack Perry": 82, "Buddy Matthews": 82, "Rush": 82, "Atlantis Jr.": 82, "Mascara Dorada": 82, "Mike Bailey": 82, "Kevin Knight": 83,
    # Men's Midcard
    "Shelton Benjamin": 81, "Brody King": 81, "Alex Shelley": 81, "Chris Sabin": 81, "Hook": 81, "Anthony Bowens": 80, "Roderick Strong": 80, "Juice Robinson": 80, "Wardlow": 80, "Kyle O'Reilly": 80, "Titan": 80, "Kyle Fletcher": 79, "Sammy Guevara": 79, "Brian Cage": 79, "Daniel Garcia": 78, "Wheeler Yuta": 78, "Lio Rush": 78, "Bishop Kaun": 78, "Toa Liona": 78, "The Beast Mortos": 77, "Lance Archer": 77, "Trent Beretta": 76, "Hologram": 75, "Scorpio Sky": 75, "Lee Johnson": 75, "Komander": 74, "Action Andretti": 71,
    # Women's Division & Crossovers
    "Mercedes Moné": 96, "Toni Storm": 94, "Mayu Iwatani": 93, "Jamie Hayter": 92, "Britt Baker": 91, "Athena": 89, "Hikaru Shida": 88, "Willow Nightingale": 88, "Mina Shirakawa": 86, "Starlight Kid": 86, "Kris Statlander": 85, "Thunder Rosa": 85, "AZM": 85, "Julia Hart": 84, "Momo Watanabe": 84, "Deonna Purrazzo": 83, "Serena Deeb": 82, "Kamille": 80, "Persephone": 80, "Skye Blue": 79, "Megan Bayne": 79, "Queen Aminata": 78, "Taya Valkyrie": 77, "Billie Starkz": 76, "Thekla": 75, "Anna Jay": 75, "Zeuxis": 75, "Red Velvet": 74, "Emi Sakura": 74, "Maya World": 73, "Alex Windsor": 73, "Harley Cameron": 72, "Penelope Ford": 72, "Lena Kross": 72, "Diamante": 71,
    # Tag Teams & Factions
    "The Elite": 95, "The Young Bucks": 95, "FTR": 94, "The Death Riders": 93, "Timeless Love Bombs": 90, "The Hurt Syndicate": 89, "Motor City Machine Guns": 88, "TMDK": 88, "Mistico, Volador Jr. & Atlantis Jr.": 88, "Bang Bang Gang": 87, "The Opps": 87, "The Conglomeration": 86, "Bishamon": 86, "The Demand": 86, "The Don Callis Family": 85, "Kings of the Black Throne": 85, "The Brawling Birds": 85, "Guerreros Laguneros": 85, "The Babes of Wrath": 84, "La Facción Ingobernable": 83, "Brodido": 83, "The Gunns": 82, "Sisters of Sin": 82, "Grizzled Young Veterans": 81, "Undisputed Kingdom": 81, "Top Flight": 80, "The Outrunners": 79, "Private Party": 78, "SkyFlight": 78, "MxM Collection": 77, "The Righteous": 76, "Gates of Agony": 76, "Divine Dominion": 76, "Dark Order": 75, "The Premier Athletes": 74, "Iron Savages": 72
}

# --- SESSION STATE INITIALIZATION ---
if "card_generated" not in st.session_state:
    st.session_state.card_generated = False
if "selected_ppv" not in st.session_state:
    st.session_state.selected_ppv = ""
if "total_matches" not in st.session_state:
    st.session_state.total_matches = 0
if "matches" not in st.session_state:
    st.session_state.matches = []
if "used_wrestlers" not in st.session_state:
    st.session_state.used_wrestlers = []

# --- HELPER FUNCTIONS ---
def roll_stipulation(match_type):
    if "Tag" in match_type:
        stips = [("Standard Tag Match", 2), ("3-Way Tag Team Match", 3), ("4-Way Tag Team Match", 4), ("Tornado Street Fight", 2), ("Tag Team Ladder Match", 2)]
        weights = [70, 10, 10, 5, 5]
    elif "Trios" in match_type:
        stips = [("Standard Trios Match", 2), ("3-Way Trios Match", 3), ("Trios Street Fight", 2)]
        weights = [80, 10, 10]
    elif match_type == "Anarchy in the Arena":
        return "", 2
    else:
        stips = [("Standard Match", 2), ("Triple Threat Match", 3), ("Fatal 4-Way Match", 4), ("6-Man Ladder Match", 6), ("Texas Deathmatch", 2), ("Steel Cage Match", 2), ("Street Fight", 2), ("Dog Collar Match", 2), ("Falls Count Anywhere", 2), ("Ladder Match", 2)]
        weights = [60, 10, 5, 5, 4, 4, 4, 3, 3, 2]
    return random.choices(stips, weights=weights)[0]

def get_match_rules(match_type, is_forbidden_door):
    # Inject crossovers if needed
    m_pool = MENS_ROSTER + CROSSOVER_MENS if is_forbidden_door else MENS_ROSTER
    w_pool = WOMENS_ROSTER + CROSSOVER_WOMENS if is_forbidden_door else WOMENS_ROSTER
    t_pool = TAG_ROSTER + CROSSOVER_TAG if is_forbidden_door else TAG_ROSTER
    tr_pool = TRIOS_ROSTER + CROSSOVER_TRIOS if is_forbidden_door else TRIOS_ROSTER

    if "Championship" in match_type:
        if match_type == "AEW Women's World Tag Team Championship": return True, WOMENS_TAG_ROSTER
        if "Women" in match_type or "TBS" in match_type: return True, w_pool
        if "Tag" in match_type: return True, t_pool
        if "Trios" in match_type: return True, tr_pool
        return True, m_pool
    if "Women" in match_type: return False, w_pool
    if "Tag" in match_type: return False, t_pool
    if "Trios" in match_type: return False, tr_pool
    if match_type == "Anarchy in the Arena": return False, FACTIONS
    
    return False, m_pool

def calculate_score(participants):
    scores = [STAR_POWER_DB.get(p.replace(" (c)", ""), 75) for p in participants]
    base_score = sum(scores) / len(scores) if scores else 75
    variance = random.uniform(-2.0, 4.0)
    final = min(100.0, max(0.0, base_score + variance))
    return round(final, 1)

def generate_full_card():
    # 1. Reset State
    st.session_state.used_wrestlers = []
    st.session_state.matches = []
    
    # 2. Pick Event & Count
    ppv = random.choice(PPV_EVENTS)
    count = random.choice(MATCH_COUNTS)
    st.session_state.selected_ppv = ppv
    st.session_state.total_matches = count
    
    is_fd = "FORBIDDEN DOOR" in ppv.upper()
    
    # 3. Setup Match Types Pool
    anchor_matches = ["AEW Women's World Championship", "AEW World Championship"]
    if "DOUBLE OR NOTHING" in ppv.upper(): anchor_matches.append("Anarchy in the Arena")
        
    pool = ["AEW World Tag Team Championship", "AEW Women's World Tag Team Championship", "AEW World Trios Championship", "AEW Continental Championship", "AEW International Championship", "AEW National Championship", "AEW TNT Championship", "AEW TBS Championship", "Men's Regular Match", "Women's Regular Match"]
    
    if is_fd:
        pool.remove("Men's Regular Match")
        pool.remove("Women's Regular Match")
        pool.extend(["Men's Owen Hart Final", "Women's Owen Hart Final"])
    if "WORLDS END" in ppv.upper():
        pool.remove("AEW Continental Championship")
        pool.append("Continental Classic Final")

    # 4. Generate Matches
    for idx in range(count):
        matches_remaining = count - idx
        is_anchor = matches_remaining <= len(anchor_matches)
        
        if is_anchor:
            raw_type = anchor_matches[-matches_remaining]
        else:
            raw_type = random.choice(pool)
            pool.remove(raw_type)
            
        stip_name, num_parts = roll_stipulation(raw_type)
        display_type = f"{raw_type.upper()} ({stip_name.upper()})" if stip_name and "Standard" not in stip_name else raw_type.upper()
        
        is_title, p_pool = get_match_rules(raw_type, is_fd)
        champ_slot = random.randint(0, num_parts - 1) if is_title else -1
        
        participants = []
        for p_idx in range(num_parts):
            avail = [x for x in p_pool if x not in st.session_state.used_wrestlers]
            if not avail: 
                participants.append("Mystery Entrant")
                continue
                
            weights = [BOOKING_FREQUENCY.get(w, 2) for w in avail]
            winner = random.choices(avail, weights=weights, k=1)[0]
            st.session_state.used_wrestlers.append(winner)
            
            if p_idx == champ_slot:
                participants.append(f"{winner} (c)")
            else:
                participants.append(winner)
                
        score = calculate_score(participants)
        
        # Label Formatting
        lbl = f"MATCH {idx+1}"
        if idx == count - 1: lbl = "🌟 MAIN EVENT 🌟"
        elif idx == count - 2 and len(anchor_matches) >= 2: lbl = "⚔️ CO-MAIN EVENT ⚔️"
        elif idx == count - 3 and len(anchor_matches) == 3: lbl = "⚔️ CO-MAIN EVENT ⚔️"
            
        st.session_state.matches.append({
            "label": lbl,
            "type": display_type,
            "participants": participants,
            "score": score
        })
        
    st.session_state.card_generated = True

# --- UI LAYOUT ---
st.title("AEW Ultimate PPV Booker")
st.markdown("Generate statistically accurate, data-backed 2026 AEW PPV Cards based on real TV booking frequencies and star power.")

st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("🎲 GENERATE NEW PPV CARD", use_container_width=True, type="primary"):
        with st.spinner("Booking the event..."):
            time.sleep(1) # Dramatic pause
            generate_full_card()

if st.session_state.card_generated:
    with col2:
        st.subheader(f"🏟️ {st.session_state.selected_ppv.upper()}")
        avg_score = sum(m["score"] for m in st.session_state.matches) / len(st.session_state.matches)
        st.write(f"**Total Matches:** {st.session_state.total_matches} | **Overall Event Score:** {avg_score:.1f} / 100")
        
    st.markdown("---")
    
    # Output the matches in a readable way
    for match in st.session_state.matches:
        st.caption(match["label"])
        st.markdown(f"### {match['type']}")
        
        if len(match["participants"]) == 2:
            st.markdown(f"#### {match['participants'][0]} **VS.** {match['participants'][1]}")
        else:
            p_string = " **VS.** ".join(match["participants"])
            st.markdown(f"#### {p_string}")
            
        st.write(f"*Match Rating: {match['score']} / 100*")
        st.markdown("---")
        
    # Plain text block for easy copying
    st.subheader("Copy to Clipboard")
    plain_text = f"=== {st.session_state.selected_ppv.upper()} ===\nOVERALL SCORE: {avg_score:.1f}/100\n\n"
    for m in st.session_state.matches:
        plain_text += f"{m['label']}\n{m['type']}\n"
        plain_text += " vs. ".join(m['participants']) + "\n"
        plain_text += f"Score: {m['score']}/100\n\n"
        
    st.text_area("Final Card", plain_text, height=300)
