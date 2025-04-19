import streamlit as st
from datetime import datetime
import hashlib

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
        /* Base styles */
        :root {
            --primary-bg: #1E1E1E;
            --secondary-bg: #262730;
            --border-color: #404040;
            --accent-blue: #00CCFF;
            --accent-green: #00FF00;
            --text-color: #FAFAFA;
            --spacing-sm: 8px;
            --spacing-md: 16px;
            --spacing-lg: 24px;
            --border-radius: 8px;
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.4);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.5);
            --shadow-lg: 0 6px 16px rgba(0, 0, 0, 0.6);
        }
        
        /* Event container wrapper and separator */
        .event-container-wrapper {
            position: relative;
            margin: 3.5rem auto 5rem;
            padding-top: 1.5rem;
        }
        
        .event-separator {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, var(--accent-blue) 50%, transparent 100%);
            box-shadow: 0 0 8px rgba(0, 204, 255, 0.5);
        }
        
        .event-container-wrapper::before {
            content: '';
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 30px;
            height: 30px;
            background-color: var(--primary-bg);
            border-radius: 50%;
            border: 2px solid var(--accent-blue);
            z-index: 2;
            box-shadow: 0 0 10px rgba(0, 204, 255, 0.7);
        }
        
        /* First event wrapper shouldn't have a separator */
        .stTabs [role="tabpanel"] .event-container-wrapper:first-child .event-separator {
            display: none;
        }
        
        .stTabs [role="tabpanel"] .event-container-wrapper:first-child {
            margin-top: 1.5rem;
        }
        
        /* Event container */
        .event-container {
            background-color: var(--secondary-bg);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-md);
            max-width: 800px;
            overflow: hidden;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            position: relative;
        }
        
        .event-container:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        .event-container::before {
            content: '';
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60%;
            height: 4px;
            background: linear-gradient(90deg, transparent, var(--accent-blue), transparent);
            border-radius: 2px;
        }
        
        /* Date header */
        .date-header {
            color: var(--text-color);
            font-size: 32px;
            font-weight: bold;
            padding: var(--spacing-lg);
            background-color: var(--primary-bg);
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 2px;
            border-bottom: 1px solid var(--border-color);
            margin: 0;
            position: relative;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        /* Game content */
        .game-content {
            padding: var(--spacing-lg);
        }
        
        /* Time slot */
        .time-slot {
            color: var(--accent-blue);
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            background-color: var(--primary-bg);
            padding: var(--spacing-md);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
        }
        
        /* Field label */
        .field-label {
            color: var(--text-color);
            font-size: 18px;
            font-weight: 500;
            text-align: center;
            background-color: var(--primary-bg);
            padding: var(--spacing-sm);
            border-radius: var(--border-radius);
            margin-bottom: var(--spacing-sm);
            border: 1px solid var(--border-color);
        }
        
        /* Team info */
        .team-info {
            background-color: var(--primary-bg);
            color: var(--text-color);
            padding: var(--spacing-md);
            border-radius: var(--border-radius);
            margin-bottom: var(--spacing-sm);
            font-size: 16px;
            border: 1px solid var(--border-color);
            text-align: center;
        }
        
        /* Winner cell */
        .winner-cell {
            background-color: var(--primary-bg);
            color: var(--accent-green);
            font-weight: bold;
            padding: var(--spacing-sm);
            border-radius: var(--border-radius);
            font-size: 14px;
            text-align: center;
            border: 1px solid var(--accent-green);
        }
        
        /* Field column */
        .field-column {
            display: flex;
            flex-direction: column;
        }
        
        /* Bootcamp header */
        .bootcamp-header {
            color: var(--text-color);
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin: var(--spacing-lg) 0 var(--spacing-md);
            padding: var(--spacing-md);
            background-color: var(--primary-bg);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
        }
        
        /* Bootcamp info */
        .bootcamp-info {
            background-color: var(--primary-bg);
            color: var(--text-color);
            padding: var(--spacing-md);
            border-radius: var(--border-radius);
            font-size: 16px;
            border: 1px solid var(--border-color);
            text-align: center;
        }

        /* Make sure Streamlit containers don't add unwanted spacing */
        .stHorizontalBlock {
            gap: var(--spacing-md);
        }
        
        /* Ensure content stays within container boundaries */
        .main .block-container {
            max-width: 1000px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Streamlit column spacing */
        div.stHorizontalBlock {
            gap: var(--spacing-md);
            padding: var(--spacing-sm);
        }
        
        div.stHorizontalBlock [data-testid="column"] {
            padding: 0;
        }

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: var(--secondary-bg);
            border-radius: var(--border-radius) var(--border-radius) 0 0;
            border: 1px solid var(--border-color);
            border-bottom: none;
        }

        .stTabs [aria-selected="true"] {
            background-color: var(--primary-bg);
            border-color: var(--accent-blue);
        }

        /* Make the event sections more distinct in tab content */
        .stTabs [role="tabpanel"] [data-testid="block-container"] {
            padding-top: 2rem;
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
    
    # Generate a unique ID for this event
    event_id = hashlib.md5(date.encode()).hexdigest()
    
    # Create wrapper with event ID
    st.markdown(f'<div class="event-container-wrapper" id="event-{event_id}">', unsafe_allow_html=True)
    st.markdown('<div class="event-separator"></div>', unsafe_allow_html=True)
    
    # Create the main event container that will hold all content
    event_container = st.container()
    
    with event_container:
        # Date header and initial game content container
        st.markdown(f'<div class="event-container" id="container-{event_id}">', unsafe_allow_html=True)
        st.markdown(f'<div class="date-header">{date}</div>', unsafe_allow_html=True)
        st.markdown('<div class="game-content">', unsafe_allow_html=True)
        
        # Create a 2-column layout for the main time slots
        time_col1, time_col2 = st.columns(2)
        
        # Time slots row
        with time_col1:
            st.markdown('<div class="time-slot">1600</div>', unsafe_allow_html=True)
        with time_col2:
            st.markdown('<div class="time-slot">1630</div>', unsafe_allow_html=True)
        
        # Create a 4-column layout for the fields
        field_cols = st.columns(4)
        
        # Helper function to create field HTML
        def field_html(game, field_label):
            winner_html = f'<div class="winner-cell">Winner: {game["winner"]}</div>' if show_winners else ''
            return f'''
                <div class="field-column">
                    <div class="field-label">{field_label}</div>
                    <div class="team-info">{game["teams"]}</div>
                    {winner_html}
                </div>
            '''
        
        # Field labels and team info
        for i, col in enumerate(field_cols):
            with col:
                field_label = "Field A" if i % 2 == 0 else "Field B"
                st.markdown(field_html(games[i], field_label), unsafe_allow_html=True)
        
        # Bootcamp section
        st.markdown('<div class="bootcamp-header">BOOTCAMP</div>', unsafe_allow_html=True)
        bootcamp_col1, bootcamp_col2 = st.columns(2)
        
        with bootcamp_col1:
            st.markdown(f'<div class="bootcamp-info">{bootcamp["games1_2"]}</div>', unsafe_allow_html=True)
        
        with bootcamp_col2:
            st.markdown(f'<div class="bootcamp-info">{bootcamp["games3_4"]}</div>', unsafe_allow_html=True)
        
        # Close the inner containers
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Close the wrapper container
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add custom JS to ensure all content stays within the container
    st.markdown(f"""
    <script>
        // This script will execute when the page loads
        (function() {{
            // Get all content related to this event container
            const eventContainer = document.getElementById('container-{event_id}');
            const wrapper = document.getElementById('event-{event_id}');
            
            // If elements exist, ensure proper nesting
            if (eventContainer && wrapper) {{
                // Find all related content
                const parentDiv = eventContainer.closest('.element-container').parentNode;
                const siblingDivs = Array.from(parentDiv.querySelectorAll('.element-container')).
                    filter(el => el.closest('#event-{event_id}') === null && 
                           !el.contains(document.getElementById('event-{event_id}')));
                
                // Move all content inside the event container
                siblingDivs.forEach(div => {{
                    if (div.querySelector('.game-content')) return; // Skip the game-content div
                    const gameContent = eventContainer.querySelector('.game-content');
                    if (gameContent) {{
                        gameContent.appendChild(div);
                    }}
                }});
            }}
        }})();
    </script>
    """, unsafe_allow_html=True)

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