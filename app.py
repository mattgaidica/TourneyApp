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
            border-radius: 8px;
            margin: 20px 0;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        /* Date header styling */
        .date-header {
            color: #FAFAFA;
            font-size: 28px;
            font-weight: bold;
            padding: 20px;
            background-color: #1E1E1E;
            border-bottom: 2px solid #404040;
            margin: 0;
            text-align: center;
        }
        /* Game schedule table styling */
        .schedule-table {
            width: 100%;
            border-collapse: collapse;
            margin: 0;
            background-color: #262730;
        }
        .schedule-table th {
            background-color: #1E1E1E;
            color: #FAFAFA;
            padding: 15px;
            text-align: center;
            border-bottom: 2px solid #404040;
            font-size: 18px;
        }
        .schedule-table td {
            padding: 15px;
            text-align: center;
            color: #FAFAFA;
            border-bottom: 1px solid #404040;
            font-size: 16px;
        }
        .time-slot {
            font-weight: bold;
            color: #00CCFF;
        }
        .field-cell {
            background-color: #2D2D2D;
        }
        .team-cell {
            background-color: #2D2D2D;
        }
    </style>
""", unsafe_allow_html=True)

# Tournament Schedule Data
TOURNAMENT_SCHEDULE = {
    "2025-04-08": {
        "date": "08 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "completed", "teams": "Alpha vs. Bravo"},
            {"time": "1600", "field": "Field B", "status": "completed", "teams": "Charlie vs. Delta"},
            {"time": "1630", "field": "Field A", "status": "completed", "teams": ""},
            {"time": "1630", "field": "Field B", "status": "completed", "teams": ""}
        ]
    },
    "2025-04-15": {
        "date": "15 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "completed", "teams": "Echo vs. Cadre"},
            {"time": "1600", "field": "Field B", "status": "completed", "teams": "Bravo vs. Delta"},
            {"time": "1630", "field": "Field A", "status": "completed", "teams": ""},
            {"time": "1630", "field": "Field B", "status": "completed", "teams": ""}
        ]
    },
    "2025-04-23": {
        "date": "23 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming", "teams": "Bravo vs. Charlie"},
            {"time": "1600", "field": "Field B", "status": "upcoming", "teams": "Alpha vs. Echo"},
            {"time": "1630", "field": "Field A", "status": "upcoming", "teams": "Charlie vs. Cadre"},
            {"time": "1630", "field": "Field B", "status": "upcoming", "teams": "Bravo vs. Echo"}
        ]
    },
    "2025-04-29": {
        "date": "29 Apr 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming", "teams": "Alpha vs. Cadre"},
            {"time": "1600", "field": "Field B", "status": "upcoming", "teams": "Delta vs. Echo"},
            {"time": "1630", "field": "Field A", "status": "upcoming", "teams": "Bravo vs. Cadre"},
            {"time": "1630", "field": "Field B", "status": "upcoming", "teams": "Alpha vs. Delta"}
        ]
    },
    "2025-05-07": {
        "date": "07 May 2025",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming", "teams": "Charlie vs. Echo"},
            {"time": "1600", "field": "Field B", "status": "upcoming", "teams": "Delta vs. Cadre"},
            {"time": "1630", "field": "Field A", "status": "upcoming", "teams": "Alpha vs. Charlie"},
            {"time": "1630", "field": "Field B", "status": "upcoming", "teams": "Sudden Death"}
        ]
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
def display_schedule_table(date, games):
    table_html = f"""
    <div class='schedule-container'>
        <div class='date-header'>{date}</div>
        <table class='schedule-table'>
            <tr>
                <th colspan='2' class='time-slot'>1600</th>
                <th colspan='2' class='time-slot'>1630</th>
            </tr>
            <tr>
                <td class='field-cell'>Field A</td>
                <td class='field-cell'>Field B</td>
                <td class='field-cell'>Field A</td>
                <td class='field-cell'>Field B</td>
            </tr>
            <tr>
                <td class='team-cell'>{games[0]['teams']}</td>
                <td class='team-cell'>{games[1]['teams']}</td>
                <td class='team-cell'>{games[2]['teams']}</td>
                <td class='team-cell'>{games[3]['teams']}</td>
            </tr>
        </table>
    </div>
    """
    st.markdown(table_html, unsafe_allow_html=True)

# Upcoming Events Tab
with tab1:
    # Display upcoming games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'upcoming' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'])
    
# Past Events Tab
with tab2:
    # Display past games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'completed' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'])
    
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