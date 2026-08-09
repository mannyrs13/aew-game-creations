st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&display=swap');

    /* Enable Vertical Scrolling on the App Container */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        overflow-y: auto !important;
        height: auto !important;
    }

    /* Style the Scrollbar so it is clean & visible */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #080a0e;
    }
    ::-webkit-scrollbar-thumb {
        background: #ffd700;
        border-radius: 5px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #ef4444;
    }

    /* Page Spacing */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 98% !important;
    }

    /* Rest of your existing CSS below... */
    </style>
""", unsafe_allow_html=True)
