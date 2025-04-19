import streamlit as st
from datetime import datetime

# Set page config with mobile-friendly settings
st.set_page_config(
    page_title="MGT101 25B Athletics",
    page_icon="🏃",
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
        /* Center the title and description */
        .title-container {
            text-align: center;
            margin-bottom: 2rem;
        }
        /* Center and style the tabs */
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 20px;
            padding: 15px 30px;
        }
        /* Note styling */
        .note {
            font-size: 0.9em;
            color: #666;
            font-style: italic;
            margin-top: 1rem;
        }
        /* Ensure content doesn't overflow on mobile */
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        /* Schedule container styling */
        .schedule-container {
            background-color: #262730;
            border-radius: 12px;
            margin: 20px auto;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 800px;
            padding: 20px;
        }
        /* Date header styling */
        .date-header {
            color: #FAFAFA;
            font-size: 28px;
            font-weight: bold;
            padding: 20px;
            background-color: #1E1E1E;
            margin: -20px -20px 20px -20px;
            text-align: center;
            border-radius: 12px 12px 0 0;
        }
        /* Time slot styling */
        .time-slot {
            color: #00CCFF;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
            text-align: center;
        }
        /* Field styling */
        .field-label {
            color: #B0B0B0;
            font-size: 18px;
            font-weight: 500;
            margin-bottom: 5px;
        }
        /* Team styling */
        .team-info {
            background-color: #2D2D2D;
            color: #FAFAFA;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-size: 16px;
        }
        /* Winner styling */
        .winner-cell {
            background-color: #1E1E1E;
            color: #00FF00;
            font-weight: bold;
            padding: 8px;
            border-radius: 6px;
            margin-top: 5px;
            font-size: 14px;
            text-align: center;
        }
        /* Bootcamp styling */
        .bootcamp-header {
            color: #FAFAFA;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin: 20px 0 10px 0;
            padding: 10px;
            background-color: #1E1E1E;
            border-radius: 8px;
        }
        .bootcamp-info {
            background-color: #2D2D2D;
            color: #FAFAFA;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-size: 16px;
        }
        /* Column styling */
        .st-emotion-cache-1r6slb0 {
            background-color: #262730;
            border-radius: 12px;
            padding: 15px;
            margin: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Tournament Schedule Data
TOURNAMENT_SCHEDULE = {
    "2025-04-08": {
        "date": "08 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "completed", "teams": "Alpha vs. Bravo", "winner": "Alpha"},
            {"time": "1600", "field": "Field B", "status": "completed", "teams": "Charlie vs. Delta", "winner": "Charlie"},
            {"time": "1630", "field": "Field A", "status": "completed", "teams": "Alpha vs. Bravo", "winner": "Alpha"},
            {"time": "1630", "field": "Field B", "status": "completed", "teams": "Charlie vs. Delta", "winner": "Charlie"}
        ],
        "bootcamp": {
            "games1_2": "Echo, Cadre",
            "games3_4": "Echo, Cadre"
        }
    },
    "2025-04-15": {
        "date": "15 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "completed", "teams": "Echo vs. Cadre", "winner": "Cadre"},
            {"time": "1600", "field": "Field B", "status": "completed", "teams": "Bravo vs. Delta", "winner": "Bravo"},
            {"time": "1630", "field": "Field A", "status": "completed", "teams": "Echo vs. Cadre", "winner": "Cadre"},
            {"time": "1630", "field": "Field B", "status": "completed", "teams": "Bravo vs. Delta", "winner": "Bravo"}
        ],
        "bootcamp": {
            "games1_2": "Alpha, Charlie",
            "games3_4": "Alpha, Charlie"
        }
    },
    "2025-04-23": {
        "date": "23 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming", "teams": "Bravo vs. Charlie"},
            {"time": "1600", "field": "Field B", "status": "upcoming", "teams": "Alpha vs. Echo"},
            {"time": "1630", "field": "Field A", "status": "upcoming", "teams": "Charlie vs. Cadre"},
            {"time": "1630", "field": "Field B", "status": "upcoming", "teams": "Bravo vs. Echo"}
        ],
        "bootcamp": {
            "games1_2": "Delta, Echo",
            "games3_4": "Alpha, Bravo"
        }
    },
    "2025-04-29": {
        "date": "29 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming", "teams": "Alpha vs. Cadre"},
            {"time": "1600", "field": "Field B", "status": "upcoming", "teams": "Delta vs. Echo"},
            {"time": "1630", "field": "Field A", "status": "upcoming", "teams": "Bravo vs. Cadre"},
            {"time": "1630", "field": "Field B", "status": "upcoming", "teams": "Alpha vs. Delta"}
        ],
        "bootcamp": {
            "games1_2": "Bravo, Cadre",
            "games3_4": "Charlie, Echo"
        }
    },
    "2025-05-07": {
        "date": "07 May 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming", "teams": "Charlie vs. Echo"},
            {"time": "1600", "field": "Field B", "status": "upcoming", "teams": "Delta vs. Cadre"},
            {"time": "1630", "field": "Field A", "status": "upcoming", "teams": "Alpha vs. Charlie"},
            {"time": "1630", "field": "Field B", "status": "upcoming", "teams": "Sudden Death"}
        ],
        "bootcamp": {
            "games1_2": "Alpha, Bravo",
            "games3_4": "N/A"
        }
    }
}

# Main title and description in a centered container
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.title("MGT101 25B Athletics")
st.markdown("""
**View upcoming and past games as well as other athletic events!**

Tournament Format: Each flight (plus Cadre) will play against each other once, with standings based on total number of wins and sudden death matches for tiebreakers.

<div class="note">Note: The standings are calculated based on the total number of wins—this eliminates the initial condition bias of typical brackets.</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Upcoming Events", "Past Events", "Standings"])

# Function to display game schedule table
def display_schedule_table(date, games, bootcamp):
    # Check if any games are completed to determine if we should show winners
    show_winners = any(game['status'] == 'completed' for game in games)
    
    # Create a container for the schedule
    with st.container():
        # Apply the schedule container class
        st.markdown('<div class="schedule-container">', unsafe_allow_html=True)
        
        # Date header
        st.markdown(f'<div class="date-header">{date}</div>', unsafe_allow_html=True)
        
        # Create columns for the time slots
        col1, col2 = st.columns(2)
        
        # 1600 time slot
        with col1:
            st.markdown('<div class="time-slot">1600</div>', unsafe_allow_html=True)
            
            # Field A
            st.markdown('<div class="field-label">Field A</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="team-info">{games[0]["teams"]}</div>', unsafe_allow_html=True)
            if show_winners:
                st.markdown(f'<div class="winner-cell">Winner: {games[0]["winner"]}</div>', unsafe_allow_html=True)
            
            # Field B
            st.markdown('<div class="field-label">Field B</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="team-info">{games[1]["teams"]}</div>', unsafe_allow_html=True)
            if show_winners:
                st.markdown(f'<div class="winner-cell">Winner: {games[1]["winner"]}</div>', unsafe_allow_html=True)
        
        # 1630 time slot
        with col2:
            st.markdown('<div class="time-slot">1630</div>', unsafe_allow_html=True)
            
            # Field A
            st.markdown('<div class="field-label">Field A</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="team-info">{games[2]["teams"]}</div>', unsafe_allow_html=True)
            if show_winners:
                st.markdown(f'<div class="winner-cell">Winner: {games[2]["winner"]}</div>', unsafe_allow_html=True)
            
            # Field B
            st.markdown('<div class="field-label">Field B</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="team-info">{games[3]["teams"]}</div>', unsafe_allow_html=True)
            if show_winners:
                st.markdown(f'<div class="winner-cell">Winner: {games[3]["winner"]}</div>', unsafe_allow_html=True)
        
        # Bootcamp section
        st.markdown('<div class="bootcamp-header">BOOTCAMP</div>', unsafe_allow_html=True)
        bootcamp_col1, bootcamp_col2 = st.columns(2)
        
        with bootcamp_col1:
            st.markdown('<div class="field-label">Games 1-2</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bootcamp-info">{bootcamp["games1_2"]}</div>', unsafe_allow_html=True)
        
        with bootcamp_col2:
            st.markdown('<div class="field-label">Games 3-4</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bootcamp-info">{bootcamp["games3_4"]}</div>', unsafe_allow_html=True)
        
        # Close the schedule container
        st.markdown('</div>', unsafe_allow_html=True)

# Upcoming Events Tab
with tab1:
    # Display upcoming games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'upcoming' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'], schedule['bootcamp'])
    
# Past Events Tab
with tab2:
    # Display past games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'completed' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'], schedule['bootcamp'])
    
# Standings Tab
with tab3:
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
    st.button("📝 Add New Event", use_container_width=True)
    st.button("📊 Update Scores", use_container_width=True)
    st.button("📋 View Rules", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Event Information")
    st.markdown("""
    - **Game Duration**: 30 minutes
    - **Game Times**: 1600 & 1630
    - **Fields**: A & B
    - **Format**: Single Elimination
    """) 