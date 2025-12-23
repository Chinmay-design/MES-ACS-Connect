import streamlit as st
from datetime import datetime, timedelta

def student_events_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">📅 Events & Clubs</h1>', unsafe_allow_html=True)
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Upcoming Events", "🎪 Clubs & Societies", "✅ My Registrations", "➕ Create Event"])
    
    with tab1:
        st.markdown("### Upcoming Events")
        
        # Search and filters
        col1, col2, col3 = st.columns(3)
        with col1:
            search_events = st.text_input("Search events...", placeholder="Event name, organizer, etc.")
        with col2:
            event_type = st.selectbox("Event Type", ["All", "Academic", "Cultural", "Sports", "Workshop", "Competition"])
        with col3:
            date_filter = st.selectbox("Date", ["All", "This Week", "This Month", "Next Month"])
        
        # Events grid
        events = [
            {
                "title": "Annual Tech Fest 2024",
                "date": "March 25-27",
                "time": "9:00 AM - 6:00 PM",
                "location": "Main Campus",
                "type": "Festival",
                "organizer": "Computer Science Dept",
                "registered": True,
                "seats": "120/200",
                "description": "Biggest tech festival with coding competitions, workshops, and tech talks",
                "tags": ["Coding", "Workshops", "Competitions"]
            },
            {
                "title": "Career Guidance Workshop",
                "date": "March 28",
                "time": "3:00 PM - 5:00 PM",
                "location": "Auditorium",
                "type": "Workshop",
                "organizer": "Placement Cell",
                "registered": False,
                "seats": "45/100",
                "description": "Learn about career opportunities and resume building",
                "tags": ["Career", "Workshop", "Guidance"]
            },
            {
                "title": "Inter-College Sports Day",
                "date": "April 5",
                "time": "8:00 AM - 4:00 PM",
                "location": "Sports Ground",
                "type": "Sports",
                "organizer": "Sports Committee",
                "registered": True,
                "seats": "Unlimited",
                "description": "Annual sports competition between colleges",
                "tags": ["Sports", "Competition", "Inter-College"]
            },
            {
                "title": "Science Exhibition",
                "date": "April 12",
                "time": "10:00 AM - 4:00 PM",
                "location": "Science Block",
                "type": "Academic",
                "organizer": "Science Club",
                "registered": False,
                "seats": "200/300",
                "description": "Showcase of student science projects and innovations",
                "tags": ["Science", "Exhibition", "Projects"]
            }
        ]
        
        # Display events
        for event in events:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{event['title']}**")
                st.caption(f"📅 {event['date']} | ⏰ {event['time']} | 📍 {event['location']}")
                st.caption(f"Type: {event['type']} • Organizer: {event['organizer']}")
                st.caption(f"Seats: {event['seats']}")
                
                # Tags
                tags_html = " ".join([f"<span style='background: #e5e7eb; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;'>{tag}</span>" 
                                    for tag in event['tags']])
                st.markdown(f"<div style='margin-top: 5px;'>{tags_html}</div>", unsafe_allow_html=True)
            
            with col2:
                if event['registered']:
                    st.success("✅ Registered")
                else:
                    if st.button("Register", key=f"reg_{event['title']}", use_container_width=True):
                        st.success(f"Registered for {event['title']}!")
            
            with col3:
                if st.button("Details", key=f"det_{event['title']}", use_container_width=True):
                    with st.expander("Event Details", expanded=True):
                        st.write(f"**Description:** {event['description']}")
                        st.write(f"**Organizer:** {event['organizer']}")
                        st.write(f"**Contact:** events@mes.edu")
                        st.write(f"**Requirements:** None")
                        
                        if not event['registered']:
                            if st.button("Register Now", key=f"regnow_{event['title']}"):
                                st.success(f"Successfully registered for {event['title']}!")
    
    with tab2:
        st.markdown("### 🎪 Clubs & Societies")
        
        # Clubs grid
        clubs = [
            {"name": "Science Club", "members": 45, "category": "Academic", "status": "Active", 
             "description": "For science enthusiasts and researchers", "meeting": "Weekly"},
            {"name": "Music Society", "members": 32, "category": "Arts", "status": "Active", 
             "description": "Music performances and workshops", "meeting": "Bi-weekly"},
            {"name": "Debate Club", "members": 28, "category": "Academic", "status": "Active", 
             "description": "Improve public speaking and debating skills", "meeting": "Weekly"},
            {"name": "Sports Club", "members": 65, "category": "Sports", "status": "Active", 
             "description": "Various sports activities and competitions", "meeting": "Daily"},
            {"name": "Coding Club", "members": 42, "category": "Technology", "status": "Active", 
             "description": "Programming competitions and workshops", "meeting": "Weekly"},
            {"name": "Photography Club", "members": 15, "category": "Arts", "status": "Active", 
             "description": "Photography workshops and exhibitions", "meeting": "Monthly"}
        ]
        
        # Display clubs in columns
        cols = st.columns(3)
        for idx, club in enumerate(clubs):
            with cols[idx % 3]:
                st.markdown(f"""
                <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                    <strong>{club['name']}</strong><br>
                    <small>👥 {club['members']} members • {club['category']}</small><br>
                    <small>📅 Meetings: {club['meeting']}</small><br>
                    <small>{club['description']}</small>
                </div>
                """, unsafe_allow_html=True)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("Join", key=f"join_club_{club['name']}", use_container_width=True):
                        st.success(f"Request sent to join {club['name']}")
                with col_b:
                    if st.button("Info", key=f"info_club_{club['name']}", use_container_width=True):
                        st.info(f"Club Info: {club}")
    
    with tab3:
        st.markdown("### My Event Registrations")
        
        # User's registered events
        my_events = [
            {"event": "Annual Tech Fest 2024", "date": "March 25", "status": "Confirmed", 
             "reminder": True, "ticket": "A-124", "checkin": "Not checked in"},
            {"event": "Inter-College Sports Day", "date": "April 5", "status": "Confirmed", 
             "reminder": True, "ticket": "S-045", "checkin": "Not checked in"},
            {"event": "Alumni Meet & Greet", "date": "April 15", "status": "Pending", 
             "reminder": False, "ticket": "Pending", "checkin": "N/A"}
        ]
        
        for evt in my_events:
            with st.expander(f"{evt['event']} - {evt['date']} ({evt['status']})"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Ticket:** {evt['ticket']}")
                    st.write(f"**Check-in:** {evt['checkin']}")
                with col2:
                    if evt['reminder']:
                        st.info("🔔 Reminders ON")
                    else:
                        st.info("🔕 Reminders OFF")
                with col3:
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button("Cancel", key=f"cancel_{evt['event']}", use_container_width=True):
                            st.warning(f"Cancel {evt['event']} registration?")
                    with col_b:
                        if st.button("Details", key=f"det_my_{evt['event']}", use_container_width=True):
                            st.info(f"Event details for {evt['event']}")
    
    with tab4:
        st.markdown("### Create New Event")
        
        with st.form("create_event_form"):
            # Event details
            event_title = st.text_input("Event Title *", placeholder="Enter event name")
            event_description = st.text_area("Description *", height=100, 
                                           placeholder="Describe your event...")
            
            # Date and time
            col1, col2 = st.columns(2)
            with col1:
                event_date = st.date_input("Event Date *")
                event_type = st.selectbox("Event Type *", 
                                        ["Academic", "Cultural", "Sports", "Workshop", "Competition", "Other"])
            with col2:
                start_time = st.time_input("Start Time *")
                end_time = st.time_input("End Time *")
            
            # Location
            col1, col2 = st.columns(2)
            with col1:
                location = st.text_input("Location *", placeholder="Venue/Room number")
                is_online = st.checkbox("Online Event")
            with col2:
                if is_online:
                    meeting_link = st.text_input("Meeting Link", placeholder="Zoom/Google Meet link")
                max_participants = st.number_input("Max Participants", min_value=2, value=100)
            
            # Additional info
            registration_deadline = st.date_input("Registration Deadline", 
                                                value=event_date - timedelta(days=1))
            contact_email = st.text_input("Contact Email", placeholder="event@mes.edu")
            
            if st.form_submit_button("📅 Create Event", use_container_width=True):
                if event_title and event_description and location:
                    st.success("Event created successfully!")
                    st.info("Event pending admin approval")
                else:
                    st.error("Please fill all required fields (*)")
