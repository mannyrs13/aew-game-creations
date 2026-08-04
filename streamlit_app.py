import streamlit as st

# Define the pages
ppv_booker = st.Page("aew_ppv_booker.py", title="AEW PPV Booker", icon="🎟️")
tournament_gen = st.Page("aew_tournament.py", title="AEW Tournament Generator", icon="🏆")

# Set up navigation
pg = st.navigation([ppv_booker, tournament_gen])

# Configure global page settings
st.set_page_config(page_title="AEW Game Suite", layout="wide")

# Run the selected page
pg.run()
