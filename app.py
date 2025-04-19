import streamlit as st
from datetime import datetime

# Set page config with mobile-friendly settings
st.set_page_config(
    page_title="MGT101 Ultimate Football Tournament",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="collapsed"  # Better for mobile
)

# Custom CSS for mobile responsiveness
st.markdown("""
    <style>
        /* Make text more readable on mobile */
        @media (max-width: 768px) {
            .stMarkdown, .stText {
                font-size: 16px;
            }
            h1 {
                font-size: 24px !important;
            }
            h2 {
                font-size: 20px !important;
            }
        }
        /* Ensure content doesn't overflow on mobile */
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        /* Game card styling */
        .game-card {
            padding: 15px;
            border-radius: 8px;
            background-color: #262730;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            color: #FAFAFA;
        }
        .game-card h3 {
            color: #FAFAFA;
            margin-bottom: 10px;
        }
        .game-card p {
            color: #FAFAFA;
            margin: 5px 0;
        }
        .game-time {
            color: #00CCFF;
            font-weight: bold;
        }
        .game-field {
            color: #00FF99;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Tournament Schedule Data
TOURNAMENT_SCHEDULE = {
    "2024-04-08": {
        "date": "08 Apr 2024",
        "games": [
            {"game": "Game 1", "time": "1600", "field": "Field A", "status": "completed"},
            {"game": "Game 2", "time": "1600", "field": "Field B", "status": "completed"},
            {"game": "Game 3", "time": "1630", "field": "Field A", "status": "completed"},
            {"game": "Game 4", "time": "1630", "field": "Field B", "status": "completed"}
        ]
    },
    "2024-04-15": {
        "date": "15 Apr 2024",
        "games": [
            {"game": "Game 1", "time": "1600", "field": "Field A", "status": "completed"},
            {"game": "Game 2", "time": "1600", "field": "Field B", "status": "completed"},
            {"game": "Game 3", "time": "1630", "field": "Field A", "status": "completed"},
            {"game": "Game 4", "time": "1630", "field": "Field B", "status": "completed"}
        ]
    },
    "2024-04-23": {
        "date": "23 Apr 2024",
        "games": [
            {"game": "Game 1", "time": "1600", "field": "Field A", "status": "upcoming"},
            {"game": "Game 2", "time": "1600", "field": "Field B", "status": "upcoming"},
            {"game": "Game 3", "time": "1630", "field": "Field A", "status": "upcoming"},
            {"game": "Game 4", "time": "1630", "field": "Field B", "status": "upcoming"}
        ]
    },
    "2024-04-29": {
        "date": "29 Apr 2024",
        "games": [
            {"game": "Game 1", "time": "1600", "field": "Field A", "status": "upcoming"},
            {"game": "Game 2", "time": "1600", "field": "Field B", "status": "upcoming"},
            {"game": "Game 3", "time": "1630", "field": "Field A", "status": "upcoming"},
            {"game": "Game 4", "time": "1630", "field": "Field B", "status": "upcoming"}
        ]
    },
    "2024-05-07": {
        "date": "07 May 2024",
        "games": [
            {"game": "Game 1", "time": "1600", "field": "Field A", "status": "upcoming"},
            {"game": "Game 2", "time": "1600", "field": "Field B", "status": "upcoming"},
            {"game": "Game 3", "time": "1630", "field": "Field A", "status": "upcoming"},
            {"game": "Game 4", "time": "1630", "field": "Field B", "status": "upcoming"}
        ]
    }
}

# Main title
st.title("MGT101 Ultimate Football Tournament 🏈")

# Add a description
st.markdown("""
Welcome to the MGT101 Ultimate Football Tournament management system. Each game day features four 30-minute games across two fields.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Upcoming Games", "Past Games", "Standings"])

# Function to display game card
def display_game_card(game, date, is_past=False):
    card_html = f"""
    <div class="game-card">
        <h3 style='margin: 0;'>{game['game']}</h3>
        <p style='margin: 5px 0;'>📅 {date}</p>
        <p style='margin: 5px 0;' class='game-time'>⏰ {game['time']}</p>
        <p style='margin: 5px 0;' class='game-field'>📍 {game['field']}</p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# Upcoming Games Tab
with tab1:
    st.header("Upcoming Games")
    st.write("View the tournament schedule and upcoming matchups.")
    
    # Display upcoming games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'upcoming' for game in schedule['games']):
            st.subheader(schedule['date'])
            for game in schedule['games']:
                if game['status'] == 'upcoming':
                    display_game_card(game, schedule['date'])
    
# Past Games Tab
with tab2:
    st.header("Past Games")
    st.write("Review completed games and their results.")
    
    # Display past games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'completed' for game in schedule['games']):
            st.subheader(schedule['date'])
            for game in schedule['games']:
                if game['status'] == 'completed':
                    display_game_card(game, schedule['date'], is_past=True)
    
# Standings Tab
with tab3:
    st.header("Tournament Standings")
    st.write("Current team rankings and statistics.")
    
    # Example standings table (mobile-friendly)
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        st.markdown("**Team**")
    with col2:
        st.markdown("**W-L**")
    with col3:
        st.markdown("**Points**")
    
    st.markdown("""
    <div style='padding: 5px; border-bottom: 1px solid #e0e0e0;'>
        <div style='display: flex; justify-content: space-between;'>
            <span style='flex: 2;'>Team A</span>
            <span style='flex: 1;'>2-0</span>
            <span style='flex: 1;'>42</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add a sidebar with mobile-friendly controls
with st.sidebar:
    st.header("Quick Actions")
    st.button("📝 Add New Game", use_container_width=True)
    st.button("📊 Update Scores", use_container_width=True)
    st.button("📋 View Rules", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Tournament Info")
    st.markdown("""
    - **Game Duration**: 30 minutes
    - **Game Times**: 1600 & 1630
    - **Fields**: A & B
    - **Format**: Single Elimination
    """) 