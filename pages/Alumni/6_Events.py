import streamlit as st

def alumni_events_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">📅 Alumni Events</h1>', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📅 Upcoming Events", "🎓 Reunions", "✅ My Registrations"])
    
    with tab1:
        st.markdown("### Alumni Events Calendar")
        
        events = [
            {"title": "Annual Alumni Meet 2024", "date": "April 15", "location": "Campus", 
             "type": "Networking", "attendees": "150+", "status": "Open"},
            {"title": "Industry Leaders Summit", "date": "May 20", "location": "Virtual", 
             "type": "Conference", "attendees": "200+", "status": "Open"},
            {"title": "Mentorship Program Launch", "date": "June 10", "location": "Online", 
             "type": "Workshop", "attendees": "50", "status": "Invite Only"}
        ]
        
        for event in events:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{event['title']}**")
                st.caption(f"📅 {event['date']} • 📍 {event['location']}")
                st.caption(f"Type: {event['type']} • 👥 {event['attendees']} alumni")
            with col2:
                if event['status'] == 'Open':
                    if st.button("Register", key=f"areg_{event['title']}"):
                        st.success(f"Registered for {event['title']}!")
                elif event['status'] == 'Invite Only':
                    st.info("Invite Only")
            with col3:
                if st.button("Details", key=f"adet_{event['title']}"):
                    st.info(f"Event details: {event}")
    
    with tab2:
        st.markdown("### 🎓 Batch Reunions")
        
        reunions = [
            {"batch": "Class of 2015", "date": "Dec 15, 2024", "location": "Campus", 
             "organizer": "Batch Committee", "confirmed": 45},
            {"batch": "Class of 2010", "date": "Mar 20, 2025", "location": "City Hotel", 
             "organizer": "Alumni Association", "confirmed": 120},
            {"batch": "Class of 2005", "date": "Jun 10, 2025", "location": "Resort", 
             "organizer": "Batch Representatives", "confirmed": 65}
        ]
        
        for reunion in reunions:
            st.markdown(f"""
            <div class="card">
                <strong>{reunion['batch']} Reunion</strong><br>
                📅 {reunion['date']}<br>
                📍 {reunion['location']}<br>
                👤 Organizer: {reunion['organizer']}<br>
                ✅ {reunion['confirmed']} alumni confirmed
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("RSVP", key=f"rsvp_{reunion['batch']}"):
                st.success(f"RSVP'd for {reunion['batch']} reunion!")
    
    with tab3:
        st.markdown("### My Event Registrations")
        
        my_events = [
            {"event": "Annual Alumni Meet", "date": "April 15", "status": "Confirmed", "ticket": "VIP"},
            {"event": "Industry Summit", "date": "May 20", "status": "Pending", "ticket": "Standard"}
        ]
        
        for evt in my_events:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{evt['event']}**")
                st.caption(f"Date: {evt['date']} • Status: {evt['status']} • Ticket: {evt['ticket']}")
            with col2:
                if st.button("Cancel", key=f"acancel_{evt['event']}"):
                    st.warning(f"Cancel {evt['event']} registration?")
