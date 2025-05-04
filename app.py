import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import hashlib

# Set page config with mobile-friendly settings
st.set_page_config(
    page_title="MGT101 25B Ultimate Tournament",
    page_icon="🏆",
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
            --field-a-bg: #03355A;
            --field-a-glow: rgba(0, 102, 204, 0.15);
            --field-b-bg: #572700;
            --field-b-glow: rgba(255, 102, 0, 0.15);
            --spacing-sm: 8px;
            --spacing-md: 16px;
            --spacing-lg: 24px;
            --border-radius: 8px;
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.4);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.5);
            --shadow-lg: 0 6px 16px rgba(0, 0, 0, 0.6);
        }
        
        /* Expander styling for date sections */
        .date-expander {
            margin: 0 auto 60px !important;
            border-radius: var(--border-radius) !important;
            border: 1px solid var(--accent-blue) !important;
            background-color: #262730 !important;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4), 0 0 15px rgba(0, 204, 255, 0.25) !important;
            overflow: hidden !important;
            max-width: 850px !important;
            position: relative !important;
            transform: translateZ(0);
            transition: all 0.2s ease-in-out;
        }
        
        /* Remove the double container by fixing Streamlit's default wrappers */
        .date-expander [data-testid="stExpander"] > div[data-testid="stExpanderDetails"] > div:first-child {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .date-expander [data-testid="stExpander"] > div[data-testid="stExpanderDetails"] > div:first-child > div {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Fix overlap of Streamlit's border wrappers */
        .date-expander [data-testid="stVerticalBlockBorderWrapper"] {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .date-expander:hover {
            transform: translateY(-2px) translateZ(0);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 204, 255, 0.3) !important;
        }
        
        /* Style the expander header */
        .date-expander > div[data-testid="stExpander"] > div:first-child {
            background-color: #1A1D24 !important;
            border-bottom: 2px solid var(--accent-blue) !important;
            padding: 0 !important;
        }
        
        /* Remove the default arrow */
        .date-expander [data-testid="stExpander"] > div:first-child > div:first-child {
            display: none !important;
        }
        
        /* Style the expander content area */
        .date-expander > div[data-testid="stExpander"] > div:nth-child(2) {
            background-color: var(--secondary-bg) !important;
            padding: var(--spacing-lg) !important;
            padding-bottom: calc(var(--spacing-lg) * 1.5) !important;
        }
        
        /* Date header */
        .date-header {
            color: var(--accent-blue);
            font-size: 38px;
            font-weight: 800;
            padding: var(--spacing-lg);
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin: 0;
            position: relative;
            text-shadow: 0 0 15px rgba(0, 204, 255, 0.4);
        }
        
        .date-header::before,
        .date-header::after {
            content: "⬥";
            color: var(--accent-blue);
            position: relative;
            margin: 0 15px;
            font-size: 24px;
            opacity: 0.8;
            text-shadow: 0 0 10px rgba(0, 204, 255, 0.5);
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
            margin-bottom: var(--spacing-md);
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
        
        /* Field Blue styling */
        .field-blue .field-label {
            background-color: var(--field-a-bg);
            border-color: #0066CC;
            box-shadow: 0 0 10px var(--field-a-glow);
            color: #66B2FF;
        }
        
        /* Field Orange styling */
        .field-orange .field-label {
            background-color: var(--field-b-bg);
            border-color: #CC5200;
            box-shadow: 0 0 10px var(--field-b-glow);
            color: #FF9966;
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
            padding: var(--spacing-md);
            background-color: var(--primary-bg);
            border-radius: var(--border-radius);
            border: 1px solid var(--border-color);
            margin: var(--spacing-lg) 0 var(--spacing-sm);
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

        /* Streamlit column spacing */
        div.stHorizontalBlock {
            gap: var(--spacing-md);
            padding: var(--spacing-sm);
        }
        
        div.stHorizontalBlock [data-testid="column"] {
            padding: 0;
        }
        
        /* Tab styling */
        .stTabs {
            max-width: 100% !important;
            margin: 0 auto 20px;
        }
        
        /* Remove distracting borders from tab panels */
        .stTabs [data-baseweb="tab-panel"] {
            border: none;
            background-color: #121218;
            border-radius: 0 0 8px 8px;
            padding-top: 30px !important;
            max-width: 100% !important;
            width: 100% !important;
        }
        
        /* More comprehensive tab styling */
        .stTabs [data-baseweb="tab"] {
            background-color: #1E1E1E !important;
            border: 1px solid #333 !important;
            border-bottom: none !important;
            border-radius: 10px 10px 0 0 !important;
            margin: 0 6px !important;
            font-weight: 400;
            transition: all 0.2s ease;
            padding: 14px 28px !important;
            font-size: 17px !important;
            letter-spacing: 0.5px;
            min-width: 150px;
            text-align: center;
            color: #CCCCCC;
        }
        
        /* Improved active tab styling */
        .stTabs [aria-selected="true"] {
            background-color: #2E2E3A !important;
            border-color: var(--accent-blue) !important;
            color: var(--accent-blue) !important;
            font-weight: 500 !important;
            box-shadow: 0 -2px 10px rgba(0, 204, 255, 0.2);
        }
        
        /* Hover effect for tabs */
        .stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
            background-color: #252530 !important;
            color: #FFFFFF;
        }
        
        /* Fix mobile tabs */
        @media (max-width: 768px) {
            .stTabs [data-baseweb="tab"] {
                padding: 10px 15px !important;
                font-size: 15px !important;
                min-width: 110px;
            }
        }
        
        /* Prevent tabs from stacking on mobile */
        .stTabs [data-baseweb="tab-list"] {
            background-color: transparent !important;
            border-bottom: 1px solid #333 !important;
            display: flex;
            justify-content: center;
            gap: 10px;
            padding: 15px 0 0 0 !important;
            margin-bottom: 0 !important;
            flex-wrap: nowrap !important;
            overflow-x: auto !important;
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* IE and Edge */
        }

        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            display: none; /* Chrome, Safari, Opera */
        }

        /* Make tabs appear as a single row on all screens */
        @media (max-width: 768px) {
            .stTabs [data-baseweb="tab-list"] {
                flex-wrap: nowrap !important;
                justify-content: space-between !important;
                width: 100% !important;
                gap: 2px !important;
                padding: 10px 0 5px 0 !important;
            }
            
            .stTabs [data-baseweb="tab"] {
                padding: 8px 8px !important;
                font-size: 14px !important;
                min-width: unset !important;
                flex: 1 !important;
                flex-shrink: 1 !important;
                white-space: nowrap !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
            }
        }
        
        /* Extra small screens */
        @media (max-width: 400px) {
            .stTabs [data-baseweb="tab"] {
                padding: 6px 4px !important;
                font-size: 12px !important;
                letter-spacing: 0 !important;
            }
        }
        
        /* Add a decorative element before each expander */
        .date-expander::before {
            content: '';
            display: block;
            height: 6px;
            background: linear-gradient(90deg, transparent, var(--accent-blue), transparent);
            position: absolute;
            top: -3px;
            left: 10%;
            right: 10%;
            border-radius: 3px;
        }
        
        /* Main app background - make it even darker */
        section[data-testid="stSidebar"] + section > div:first-child {
            background-color: #121218;
        }

        /* Event separator styling */
        .event-separator {
            height: 1px;
            background: #333;
            margin: 40px auto;
            width: 80%;
            opacity: 0.3;
        }

        /* Update the main background to be darker */
        .stApp {
            background-color: #0E1117 !important;
        }

        /* Make the content area use more of the screen width */
        .main .block-container {
            max-width: 1400px !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        /* Make content use full width */
        .stApp > header + div > div > div > div:has(> [data-testid="stVerticalBlock"]) {
            max-width: 100% !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
        }

        /* Make tab container use full width */
        .stTabs {
            max-width: 100% !important;
            margin: 0;
        }

        /* Ensure event containers can use more width */
        .date-expander {
            margin: 0 auto 60px !important;
            max-width: 92% !important;
        }

        /* Remove empty padding from expander content */
        .date-expander > div[data-testid="stExpander"] > div:nth-child(2) {
            padding: var(--spacing-lg) !important;
            width: 100% !important;
        }

        /* Style the expander details */
        [data-testid="stExpanderDetails"] {
            padding-bottom: 2rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        /* Style the title container */
        .title-container {
            text-align: center;
            margin-bottom: 30px;
            padding: var(--spacing-lg) 0;
        }

        /* Main app title styling */
        .main-title {
            color: var(--accent-blue);
            font-size: 48px;
            font-weight: 800;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin: 0 0 15px 0;
            text-shadow: 0 0 20px rgba(0, 204, 255, 0.4);
        }

        /* Main description styling */
        .main-description {
            color: #FFFFFF;
            font-size: 18px;
            margin: 20px auto;
            max-width: 800px;
            text-align: center;
            font-weight: 500;
        }

        /* Style the note under the title */
        .note {
            color: #999999;
            font-size: 14px;
            margin: 15px auto;
            max-width: 800px;
            text-align: center;
            font-style: italic;
        }

        .note strong {
            color: #BBBBBB;
            font-weight: 500;
        }

        /* Standings table styling */
        .standings-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: var(--secondary-bg);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow-md);
        }

        .standings-table th {
            background-color: var(--primary-bg);
            color: var(--accent-blue);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 16px;
            letter-spacing: 1px;
            padding: 15px 10px;
            text-align: center;
            border-bottom: 2px solid var(--border-color);
        }

        .standings-table td {
            padding: 12px 10px;
            text-align: center;
            border-bottom: 1px solid var(--border-color);
            font-size: 15px;
            color: var(--text-color);
        }

        .standings-table tr:last-child td {
            border-bottom: none;
        }

        /* Flight column styling */
        .standings-table td:first-child {
            font-weight: 600;
            text-align: left;
            padding-left: 20px;
        }

        /* Highlight top rows */
        .highlight-row td {
            background-color: rgba(0, 204, 255, 0.1);
            border-bottom: 1px solid rgba(0, 204, 255, 0.3);
        }

        .highlight-row td:first-child {
            border-left: 3px solid var(--accent-blue);
            padding-left: 17px; /* Adjust for the border */
        }

        /* Win rate styling */
        .win-rate {
            font-weight: 500;
        }

        /* Placing column styling */
        .placing {
            font-style: italic;
        }

        .placing-first {
            color: #FFD700; /* Gold */
        }

        .placing-middle {
            color: #C0C0C0; /* Silver */
        }

        .placing-last {
            color: #CD7F32; /* Bronze */
        }

        /* Mobile responsive adjustments */
        @media (max-width: 768px) {
            .standings-table th,
            .standings-table td {
                padding: 8px 5px;
                font-size: 14px;
            }
            
            .standings-table td:first-child {
                padding-left: 10px;
            }
            
            .highlight-row td:first-child {
                padding-left: 7px;
            }
        }

        /* Additional mobile responsive styles */
        @media (max-width: 768px) {
            .date-expander {
                max-width: 98% !important;
            }
            
            .date-header {
                font-size: 28px !important;
            }
            
            .time-slot {
                font-size: 18px !important;
            }
        }

        /* Improve mobile responsiveness for event elements */
        @media (max-width: 768px) {
            /* Time slots row improvements */
            .stHorizontalBlock {
                gap: var(--spacing-sm) !important;
            }
            
            /* Better field display on small screens */
            .field-column {
                margin-bottom: var(--spacing-md);
            }
            
            /* Prevent time slots from being too large */
            .time-slot {
                font-size: 18px !important;
                padding: var(--spacing-sm) !important;
            }
            
            /* Adjust field and team info for better small screen display */
            .field-label, .team-info {
                padding: 6px !important;
                font-size: 14px !important;
            }
            
            /* Make sure bootcamp elements stay aligned */
            .bootcamp-header {
                font-size: 16px !important;
                padding: 8px !important;
                margin-top: var(--spacing-md) !important;
            }
            
            .bootcamp-info {
                font-size: 14px !important;
                padding: 6px !important;
            }
            
            /* Fix for winner display on small screens */
            .winner-cell {
                font-size: 12px !important;
                padding: 4px !important;
            }
        }

        /* Very small screens (phone portrait) */
        @media (max-width: 480px) {
            /* Adjust spacing and sizing for very small screens */
            .stHorizontalBlock [data-testid="column"] {
                padding: 0 !important;
            }
            
            .date-header {
                font-size: 24px !important;
                padding: var(--spacing-sm) !important;
            }
            
            .field-label, .team-info, .bootcamp-info {
                font-size: 12px !important;
                padding: 4px !important;
            }
            
            /* Make sure elements don't get cut off */
            .date-expander > div[data-testid="stExpander"] > div:nth-child(2) {
                padding: var(--spacing-sm) var(--spacing-sm) var(--spacing-md) !important;
            }
        }

        /* Styles to prevent column stacking at all sizes */
        @media screen and (max-width: 640px) {
            /* Force columns to remain in a row */
            .stHorizontalBlock {
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                width: 100% !important;
                gap: 4px !important;
            }
            
            /* Ensure each column takes equal width and doesn't try to expand */
            .stHorizontalBlock [data-testid="column"] {
                width: 25% !important;
                min-width: 0 !important;
                flex: 1 1 0 !important;
                padding: 0 2px !important;
            }
            
            /* Make sure each column's content fits within */
            [data-testid="column"] > div {
                width: 100% !important;
                min-width: 0 !important;
            }
            
            /* Make content elements more compact */
            .time-slot, .field-label, .team-info, .bootcamp-header, .bootcamp-info {
                padding: 4px 2px !important;
                margin-bottom: 4px !important;
                font-size: 12px !important;
                border-radius: 4px !important;
                white-space: nowrap !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
            }
            
            .time-slot {
                font-size: 14px !important;
            }
            
            .winner-cell {
                font-size: 10px !important;
                padding: 2px !important;
            }
            
            /* Reduce overall padding in the expander content */
            .date-expander > div[data-testid="stExpander"] > div:nth-child(2) {
                padding: 8px 4px 16px !important;
            }
            
            /* Make date headers smaller */
            .date-header {
                font-size: 20px !important;
                padding: 8px 4px !important;
                letter-spacing: 1px !important;
            }
        }

        /* Target Streamlit's block structure explicitly to prevent stacking */
        div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
        }

        /* Enforce equal width columns regardless of content */
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            flex: 1 1 0 !important;
            width: 0 !important;
            min-width: 0 !important;
        }

        /* Override Streamlit's default emotion class styles that cause stacking */
        @media (max-width: 640px) {
            /* Target the specific emotion class that controls min-width */
            .st-emotion-cache-t74pzu,
            .st-emotion-cache-180ybpv,
            [class*="st-emotion-cache-"] {
                min-width: 0 !important;
                width: auto !important;
                flex: 1 !important;
            }
            
            /* Override any grid-based layouts */
            [data-testid="stHorizontalBlock"] {
                display: flex !important;
                grid-template-columns: none !important;
                grid-gap: 0 !important;
            }
            
            /* Allow text to wrap instead of truncating with ellipsis */
            .field-label, .bootcamp-header, .bootcamp-info {
                white-space: normal !important;
                overflow: visible !important;
                text-overflow: clip !important;
                word-wrap: break-word !important;
                hyphens: auto !important;
            }
            
            /* Specific styling for team info on small screens */
            .team-info {
                white-space: normal !important;
                overflow: visible !important;
                text-overflow: clip !important;
                word-wrap: break-word !important;
                hyphens: auto !important;
                font-size: 10px !important;
            }
        }

        /* Add specific overrides for Streamlit's column gaps */
        [data-testid="stHorizontalBlock"] {
            gap: 0.5rem !important;
        }

        @media (max-width: 480px) {
            [data-testid="stHorizontalBlock"] {
                gap: 0.25rem !important;
            }
        }

        /* Adjust main title and container on mobile */
        @media (max-width: 640px) {
            .title-container {
                padding: 10px 0 !important;
                margin-bottom: 15px !important;
            }
            
            .main-title {
                font-size: 36px !important;
                margin-top: 0 !important;
                padding-top: 0 !important;
            }
            
            .main-description {
                font-size: 14px !important;
                margin: 10px auto !important;
            }
            
            /* Reduce space above the first tab content */
            .stTabs [data-baseweb="tab-panel"] {
                padding-top: 15px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Tournament Schedule Data
TOURNAMENT_SCHEDULE = {
    "2025-04-08": {
        "date": "08 Apr 2025",
        "games": [
            {"time": "1550", "field": "Field Blue", "status": "completed", "teams": "Alpha vs. Bravo", "winner": "Alpha"},
            {"time": "1550", "field": "Field Orange", "status": "completed", "teams": "Charlie vs. Delta", "winner": "Charlie"},
            {"time": "1620", "field": "Field Blue", "status": "completed", "teams": "Alpha vs. Bravo", "winner": "Alpha"},
            {"time": "1620", "field": "Field Orange", "status": "completed", "teams": "Charlie vs. Delta", "winner": "Charlie"}
        ],
        "bootcamp": {
            "games1_2": "Echo, Cadre",
            "games3_4": "Echo, Cadre"
        }
    },
    "2025-04-15": {
        "date": "15 Apr 2025",
        "games": [
            {"time": "1550", "field": "Field Blue", "status": "completed", "teams": "Echo vs. Cadre", "winner": "Cadre"},
            {"time": "1550", "field": "Field Orange", "status": "completed", "teams": "Bravo vs. Delta", "winner": "Bravo"},
            {"time": "1620", "field": "Field Blue", "status": "completed", "teams": "Echo vs. Cadre", "winner": "Cadre"},
            {"time": "1620", "field": "Field Orange", "status": "completed", "teams": "Bravo vs. Delta", "winner": "Bravo"}
        ],
        "bootcamp": {
            "games1_2": "Alpha, Charlie",
            "games3_4": "Alpha, Charlie"
        }
    },
    "2025-04-23": {
        "date": "23 Apr 2025",
        "games": [
            {"time": "1550", "field": "Field Blue", "status": "completed", "teams": "Bravo vs. Charlie", "winner": "Bravo"},
            {"time": "1550", "field": "Field Orange", "status": "completed", "teams": "Alpha vs. Echo", "winner": "Alpha"},
            {"time": "1620", "field": "Field Blue", "status": "completed", "teams": "Charlie vs. Cadre", "winner": "Cadre"},
            {"time": "1620", "field": "Field Orange", "status": "completed", "teams": "Bravo vs. Echo", "winner": "Bravo"}
        ],
        "bootcamp": {
            "games1_2": "Delta, Cadre",
            "games3_4": "Alpha, Delta"
        }
    },
    "2025-04-28": {
        "date": "28 Apr 2025",
        "games": [
            {"time": "1550", "field": "Field Blue", "status": "completed", "teams": "Alpha vs. Cadre", "winner": "Cadre"},
            {"time": "1550", "field": "Field Orange", "status": "completed", "teams": "Delta vs. Echo", "winner": "Delta"},
            {"time": "1620", "field": "Field Blue", "status": "completed", "teams": "Bravo vs. Cadre", "winner": "Bravo"},
            {"time": "1620", "field": "Field Orange", "status": "completed", "teams": "Alpha vs. Delta", "winner": "Alpha"}
        ],
        "bootcamp": {
            "games1_2": "Bravo, Charlie",
            "games3_4": "Charlie, Echo"
        }
    },
    "2025-05-07": {
        "date": "07 May 2025",
        "games": [
            {"time": "1550", "field": "Field Blue", "status": "upcoming", "teams": "Charlie vs. Echo"},
            {"time": "1550", "field": "Field Orange", "status": "upcoming", "teams": "Delta vs. Cadre"},
            {"time": "1620", "field": "Field Blue", "status": "upcoming", "teams": "Alpha vs. Charlie"},
            {"time": "1620", "field": "Field Orange", "status": "upcoming", "teams": "Sudden Death"}
        ],
        "bootcamp": {
            "games1_2": "Alpha, Bravo",
            "games3_4": "N/A"
        }
    }
}

# Main title and description in a centered container
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">MGT101 25B Ultimate Tournament</h1>', unsafe_allow_html=True)
st.markdown('<div class="main-description">Each flight (plus Cadre) will play against each other once, with standings based on total number of wins and sudden death matches for tiebreakers.</div>', unsafe_allow_html=True)
st.markdown("""
<div class="note">Note: The standings are calculated based on the total number of wins—this eliminates the initial condition bias of typical brackets.</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Finals", "Past", "Standings"])

# Function to display game schedule table
def display_schedule_table(date, games, bootcamp):
    # Check if any games are completed to determine if we should show winners
    show_winners = any(game['status'] == 'completed' for game in games)
    
    # Create an expander with custom styling for the date (expanded by default)
    with st.expander("", expanded=True):
        # Apply custom CSS to style the expander
        st.markdown(f'<div class="date-header">{date}</div>', unsafe_allow_html=True)
        
        # Use the smallest possible column container for better control
        st.write('<style>.row-container { display: flex; width: 100%; }</style>', unsafe_allow_html=True)
        
        # Create a 2-column layout with fixed ratio for time slots
        cols = st.columns([1, 1])
        
        # Time slots row - force them to stay side by side
        with cols[0]:
            st.markdown('<div class="time-slot">1550</div>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown('<div class="time-slot">1620</div>', unsafe_allow_html=True)
        
        # Create a 4-column layout with equal widths for fields
        field_cols = st.columns([1, 1, 1, 1])
        
        # Helper function to create field HTML
        def field_html(game, field_label):
            winner_html = f'<div class="winner-cell">Winner: {game["winner"]}</div>' if show_winners and "winner" in game else ''
            
            # Set CSS class based on field
            field_class = "field-blue" if field_label == "Field Blue" else "field-orange"
            
            return f'''
                <div class="field-column {field_class}">
                    <div class="field-label">{field_label}</div>
                    <div class="team-info">{game["teams"]}</div>
                    {winner_html}
                </div>
            '''
        
        # Field labels and team info
        for i, col in enumerate(field_cols):
            with col:
                field_label = "Field Blue" if i % 2 == 0 else "Field Orange"
                st.markdown(field_html(games[i], field_label), unsafe_allow_html=True)
        
        # Bootcamp section headers
        bootcamp_cols = st.columns([1, 1])
        with bootcamp_cols[0]:
            st.markdown('<div class="bootcamp-header">BOOTCAMP</div>', unsafe_allow_html=True)
        with bootcamp_cols[1]:
            st.markdown('<div class="bootcamp-header">BOOTCAMP</div>', unsafe_allow_html=True)
        
        # Bootcamp info
        bootcamp_info_cols = st.columns([1, 1])
        with bootcamp_info_cols[0]:
            st.markdown(f'<div class="bootcamp-info">{bootcamp["games1_2"]}</div>', unsafe_allow_html=True)
        with bootcamp_info_cols[1]:
            st.markdown(f'<div class="bootcamp-info">{bootcamp["games3_4"]}</div>', unsafe_allow_html=True)
    
    # Add spacing and separator after the expander
    st.markdown('<div class="event-separator"></div>', unsafe_allow_html=True)
    
    # Apply custom class to the expander after it's created
    components.html(
        """
        <script>
            // Find the most recently created expander and add the date-expander class
            (function() {
                const expanders = Array.from(window.parent.document.querySelectorAll('[data-testid="stExpander"]'));
                const lastExpander = expanders[expanders.length - 1];
                if (lastExpander) {
                    lastExpander.closest('[data-testid="stVerticalBlock"]').classList.add('date-expander');
                }
                
                // Enforce column layout on small screens
                const columns = window.parent.document.querySelectorAll('[data-testid="column"]');
                columns.forEach(col => {
                    col.style.minWidth = '0';
                    col.style.width = '0';
                    col.style.flex = '1 1 0%';
                });
                
                // Ensure horizontal blocks stay horizontal
                const blocks = window.parent.document.querySelectorAll('[data-testid="stHorizontalBlock"]');
                blocks.forEach(block => {
                    block.style.display = 'flex';
                    block.style.flexDirection = 'row';
                    block.style.flexWrap = 'nowrap';
                });
            })();
        </script>
        """,
        height=0,
    )

# Function to display finals table
def display_finals_table(date, games):
    # Create an expander with custom styling for the date (expanded by default)
    with st.expander("", expanded=True):
        # Apply custom CSS to style the expander
        st.markdown(f'<div class="date-header">{date}</div>', unsafe_allow_html=True)
        
        # Create a 2-column layout for time slots (2:1 ratio)
        time_cols = st.columns([2, 1])
        
        # Time slots row
        with time_cols[0]:
            st.markdown('<div class="time-slot" style="text-align: center;">1540</div>', unsafe_allow_html=True)
        with time_cols[1]:
            st.markdown('<div class="time-slot">1600</div>', unsafe_allow_html=True)
        
        # Create a 3-column layout for fields
        field_cols = st.columns([1, 1, 1])
        
        # Helper function to create field HTML
        def field_html(game, field_label):
            # Set CSS class based on field
            field_class = "field-blue" if field_label == "Field Blue" else "field-orange"
            
            return f'''
                <div class="field-column {field_class}">
                    <div class="field-label">{field_label}</div>
                    <div class="team-info">{game["teams"]}</div>
                </div>
            '''
        
        # Field labels and team info
        # First time slot (1540) - both fields
        with field_cols[0]:
            st.markdown(field_html(games[0], "Field Blue"), unsafe_allow_html=True)
        with field_cols[1]:
            st.markdown(field_html(games[1], "Field Orange"), unsafe_allow_html=True)
        
        # Second time slot (1600) - only Blue field
        with field_cols[2]:
            st.markdown(field_html(games[2], "Field Blue"), unsafe_allow_html=True)
    
    # Add spacing and separator after the expander
    st.markdown('<div class="event-separator"></div>', unsafe_allow_html=True)

# Upcoming Events Tab
with tab1:
    # Display finals games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'upcoming' for game in schedule['games']):
            display_finals_table(schedule['date'], schedule['games'])
    
# Past Events Tab
with tab2:
    # Display past games
    for date, schedule in TOURNAMENT_SCHEDULE.items():
        if any(game['status'] == 'completed' for game in schedule['games']):
            display_schedule_table(schedule['date'], schedule['games'], schedule['bootcamp'])
    
# Standings Tab
with tab3:
    # Create a clean HTML table for the standings
    html = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <table class="standings-table">
            <thead>
                <tr>
                    <th>Flight</th>
                    <th>Plays</th>
                    <th>Wins</th>
                    <th>Win Rate</th>
                    <th>Placing</th>
                </tr>
            </thead>
            <tbody>
                <tr class="highlight-row">
                    <td>Bravo</td>
                    <td>5 / 5</td>
                    <td>4</td>
                    <td class="win-rate">80%</td>
                    <td class="placing placing-first">First</td>
                </tr>
                <tr>
                    <td>Alpha</td>
                    <td>4 / 5</td>
                    <td>3</td>
                    <td class="win-rate">75%</td>
                    <td class="placing placing-middle">Second</td>
                </tr>
                <tr>
                    <td>Cadre</td>
                    <td>4 / 5</td>
                    <td>3</td>
                    <td class="win-rate">75%</td>
                    <td class="placing">Not ranked</td>
                </tr>
                <tr>
                    <td>Charlie</td>
                    <td>3 / 5</td>
                    <td>1</td>
                    <td class="win-rate">33%</td>
                    <td class="placing placing-middle">Third</td>
                </tr>
                <tr>
                    <td>Delta</td>
                    <td>4 / 5</td>
                    <td>1</td>
                    <td class="win-rate">25%</td>
                    <td class="placing placing-middle">Fourth</td>
                </tr>
                <tr>
                    <td>Echo</td>
                    <td>4 / 5</td>
                    <td>0</td>
                    <td class="win-rate">0%</td>
                    <td class="placing placing-last">Fifth</td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    
    # Display the standings table
    st.markdown(html, unsafe_allow_html=True)
    
    # Add explanatory text
    st.markdown("""
    <div style="margin-top: 20px; text-align: center; font-style: italic; color: #AAAAAA;">
    Standings updated after completed games. Teams with the same win percentage are placed in the same tier.
    </div>
    """, unsafe_allow_html=True)

# Add a sidebar with mobile-friendly controls
with st.sidebar:
    st.header("Quick Actions")
    
    # Create a button that links to the Ultimate Rules GPT
    st.markdown(
        """
        <a href="https://chatgpt.com/g/g-67f06da3e3d48191a2057ffb5cbd7341-mgt101-ultimate-gpt" target="_blank">
            <button style="
                background-color: #262730;
                color: #FAFAFA;
                border: 1px solid #404040;
                border-radius: 4px;
                padding: 0.5rem 1rem;
                font-size: 1rem;
                cursor: pointer;
                width: 100%;
                transition: all 0.2s;
                margin-bottom: 8px;
            ">
                Ultimate Rules GPT
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    
    # Create a button that links to the official rules document
    st.markdown(
        """
        <a href="https://drive.google.com/file/d/1k-y8qDlXMqLd9z82zBIX0GdK35bIoBl9/view?usp=sharing" target="_blank">
            <button style="
                background-color: #262730;
                color: #FAFAFA;
                border: 1px solid #404040;
                border-radius: 4px;
                padding: 0.5rem 1rem;
                font-size: 1rem;
                cursor: pointer;
                width: 100%;
                transition: all 0.2s;
            ">
                Official Rules for MGT 101
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.markdown("### Game Play:")
    st.markdown("""
    - **Game Duration**: 30 minutes
    - **Game Times**: 1550 & 1620
    - **Fields**: A & B
    - **Format**: Single Elimination
    """) 