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
        /* Ensure content doesn't overflow on mobile */
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        /* Game schedule table styling */
        .schedule-table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            background-color: #262730;
            border-radius: 8px;
            overflow: hidden;
        }
        .schedule-table th {
            background-color: #1E1E1E;
            color: #FAFAFA;
            padding: 12px;
            text-align: center;
            border-bottom: 2px solid #404040;
        }
        .schedule-table td {
            padding: 12px;
            text-align: center;
            color: #FAFAFA;
            border-bottom: 1px solid #404040;
        }
        .time-slot {
            font-weight: bold;
            color: #00CCFF;
        }
        .field-cell {
            background-color: #2D2D2D;
        }
        .date-header {
            color: #FAFAFA;
            margin-top: 20px;
            margin-bottom: 10px;
            padding: 10px;
            background-color: #1E1E1E;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Tournament Schedule Data
TOURNAMENT_SCHEDULE = {
    "2024-04-08": {
        "date": "08 Apr 2024",
        "games": [
            {"time": "1600", "field": "Field A", "status": "completed"},
            {"time": "1600", "field": "Field B", "status": "completed"},
            {"time": "1630", "field": "Field A", "status": "completed"},
            {"time": "1630", "field": "Field B", "status": "completed"}
        ]
    },
    "2024-04-15": {
        "date": "15 Apr 2024",
        "games": [
            {"time": "1600", "field": "Field A", "status": "completed"},
            {"time": "1600", "field": "Field B", "status": "completed"},
            {"time": "1630", "field": "Field A", "status": "completed"},
            {"time": "1630", "field": "Field B", "status": "completed"}
        ]
    },
    "2024-04-23": {
        "date": "23 Apr 2024",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming"},
            {"time": "1600", "field": "Field B", "status": "upcoming"},
            {"time": "1630", "field": "Field A", "status": "upcoming"},
            {"time": "1630", "field": "Field B", "status": "upcoming"}
        ]
    },
    "2024-04-29": {
        "date": "29 Apr 2024",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming"},
            {"time": "1600", "field": "Field B", "status": "upcoming"},
            {"time": "1630", "field": "Field A", "status": "upcoming"},
            {"time": "1630", "field": "Field B", "status": "upcoming"}
        ]
    },
    "2024-05-07": {
        "date": "07 May 2024",
        "games": [
            {"time": "1600", "field": "Field A", "status": "upcoming"},
            {"time": "1600", "field": "Field B", "status": "upcoming"},
            {"time": "1630", "field": "Field A", "status": "upcoming"},
            {"time": "1630", "field": "Field B", "status": "upcoming"}
        ]
    }
}

# Main title
st.title("MGT101 25B Athletics 🏃")

# Add a description
st.markdown("""
Welcome to the MGT101 25B Athletics portal. View upcoming and past games as well as other athletic events.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Upcoming Events", "Past Events", "Standings"])

# Function to display game schedule table
def display_schedule_table(date, games):
    table_html = f"""
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
    </table>
    """
    st.markdown(table_html, unsafe_allow_html=True)

# Upcoming Events Tab
with tab1:
    st.header("Upcoming Events")
    st.write("View scheduled games and upcoming athletic events.")
    
    # Display upcoming games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'upcoming' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'])
    
# Past Events Tab
with tab2:
    st.header("Past Events")
    st.write("Review completed games and past athletic events.")
    
    # Display past games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'completed' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'])
    
# Standings Tab
with tab3:
    st.header("Team Standings")
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