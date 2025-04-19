import streamlit as st

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
    </style>
""", unsafe_allow_html=True)

# Main title
st.title("MGT101 Ultimate Football Tournament 🏈")

# Add a description
st.markdown("""
Welcome to the MGT101 Ultimate Football Tournament management system. Track games, view schedules, and monitor team standings all in one place.
""")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Upcoming Games", "Past Games", "Standings"])

# Upcoming Games Tab
with tab1:
    st.header("Upcoming Games")
    st.write("View the tournament schedule and upcoming matchups.")
    
    # Example game card (mobile-friendly)
    with st.container():
        st.markdown("""
        <div style='padding: 10px; border-radius: 5px; background-color: #f0f2f6; margin: 10px 0;'>
            <h3 style='margin: 0;'>Game 1: Team A vs Team B</h3>
            <p style='margin: 5px 0;'>📅 Date: March 15, 2024</p>
            <p style='margin: 5px 0;'>⏰ Time: 14:00</p>
            <p style='margin: 5px 0;'>📍 Location: Main Field</p>
        </div>
        """, unsafe_allow_html=True)
    
# Past Games Tab
with tab2:
    st.header("Past Games")
    st.write("Review completed games and their results.")
    
    # Example past game result (mobile-friendly)
    with st.container():
        st.markdown("""
        <div style='padding: 10px; border-radius: 5px; background-color: #f0f2f6; margin: 10px 0;'>
            <h3 style='margin: 0;'>Team A 21 - Team B 14</h3>
            <p style='margin: 5px 0;'>📅 March 10, 2024</p>
            <p style='margin: 5px 0;'>🏆 MVP: John Doe</p>
        </div>
        """, unsafe_allow_html=True)
    
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
    - **Start Date**: March 10, 2024
    - **Teams**: 8
    - **Format**: Single Elimination
    - **Location**: Main Field
    """) 