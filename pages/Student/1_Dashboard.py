import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def student_dashboard_page():
    user = st.session_state.user
    
    st.markdown(f'<h1 class="main-header">Welcome, {user["first_name"]}!</h1>', unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👥 Friends", "24", "+3")
    with col2:
        st.metric("👥 Groups", "5", "+1")
    with col3:
        st.metric("📅 Events", "3", "0")
    with col4:
        st.metric("💬 Messages", "12", "+2")
    
    st.markdown("---")
    
    # Main content in two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Announcements Feed
        st.markdown("### 📢 Recent Announcements")
        
        announcements = [
            {
                "title": "Campus Hackathon 2024",
                "content": "Annual hackathon registration is now open. Prizes worth ₹1,00,000! Last date: March 25th",
                "date": "2 hours ago",
                "priority": "🔴 High",
                "type": "Event"
            },
            {
                "title": "Final Exam Schedule Released",
                "content": "Final exam schedule for PUC students has been published on the notice board",
                "date": "1 day ago",
                "priority": "🟡 Medium",
                "type": "Academic"
            },
            {
                "title": "Library Extended Hours",
                "content": "During exam period, library will remain open till 10 PM",
                "date": "2 days ago",
                "priority": "🟢 Low",
                "type": "General"
            }
        ]
        
        for ann in announcements:
            with st.expander(f"{ann['priority']} {ann['title']} - {ann['date']} ({ann['type']})"):
                st.write(ann['content'])
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("📋 View Details", key=f"view_{ann['title']}"):
                        st.info(f"Detailed view for {ann['title']}")
                with col_b:
                    if st.button("📌 Save", key=f"save_{ann['title']}"):
                        st.success("Saved to your bookmarks!")
        
        # Quick Actions
        st.markdown("### ⚡ Quick Actions")
        
        action_col1, action_col2, action_col3 = st.columns(3)
        with action_col1:
            if st.button("👥 Find Friends", use_container_width=True, icon="👥"):
                st.session_state.page = "Student/3_Friends"
                st.rerun()
        with action_col2:
            if st.button("🤫 Post Confession", use_container_width=True, icon="🤫"):
                st.session_state.page = "Student/6_Confessions"
                st.rerun()
        with action_col3:
            if st.button("👥 Create Group", use_container_width=True, icon="👥"):
                st.session_state.page = "Student/5_Groups"
                st.rerun()
        
        # Recent Activity
        st.markdown("### 📈 Recent Activity")
        
        activities = [
            {"friend": "Alex Johnson", "action": "accepted your friend request", "time": "10 min ago"},
            {"friend": "Math Club", "action": "posted new announcement", "time": "1 hour ago"},
            {"friend": "Sarah Miller", "action": "commented on your post", "time": "3 hours ago"},
            {"friend": "Coding Club", "action": "invited you to join", "time": "1 day ago"}
        ]
        
        for activity in activities:
            st.markdown(f"""
            <div style="padding: 0.5rem; border-bottom: 1px solid #e5e7eb;">
                👤 <strong>{activity['friend']}</strong> {activity['action']}<br>
                <small style="color: #6b7280;">{activity['time']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Upcoming Events
        st.markdown("### 📅 Upcoming Events")
        
        events = [
            {
                "name": "Alumni Talk - Tech Careers",
                "date": "Mar 20",
                "time": "3:00 PM",
                "location": "Auditorium",
                "status": "Registered"
            },
            {
                "name": "Inter-College Coding Contest",
                "date": "Mar 22",
                "time": "10:00 AM",
                "location": "CS Lab",
                "status": "Open"
            },
            {
                "name": "Annual Career Fair",
                "date": "Mar 25",
                "time": "9:00 AM",
                "location": "Main Hall",
                "status": "Open"
            },
            {
                "name": "Sports Day",
                "date": "Apr 5",
                "time": "8:00 AM",
                "location": "Sports Ground",
                "status": "Coming Soon"
            }
        ]
        
        for event in events:
            st.markdown(f"""
            <div class="card">
                <strong>{event['name']}</strong><br>
                📅 {event['date']} | ⏰ {event['time']}<br>
                📍 {event['location']}<br>
                <small>Status: <strong>{event['status']}</strong></small>
            </div>
            """, unsafe_allow_html=True)
            
            if event['status'] == 'Open':
                if st.button("Register Now", key=f"reg_{event['name']}", use_container_width=True):
                    st.success(f"Registered for {event['name']}!")
            elif event['status'] == 'Registered':
                st.success("✅ Already Registered")
        
        # Suggested Groups
        st.markdown("### 👥 Suggested Groups")
        
        groups = [
            {"name": "Science Study Group", "members": 24, "category": "Academic"},
            {"name": "Coding Club", "members": 42, "category": "Technology"},
            {"name": "Debate Society", "members": 28, "category": "Academic"},
            {"name": "Music Club", "members": 32, "category": "Arts"}
        ]
        
        for group in groups:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(f"**{group['name']}**")
                st.caption(f"{group['category']} • {group['members']} members")
            with col_b:
                if st.button("Join", key=f"join_{group['name']}"):
                    st.success(f"Request sent to join {group['name']}")
        
        # Quick Links
        st.markdown("### 🔗 Quick Links")
        
        if st.button("📚 Study Materials", use_container_width=True):
            st.info("Opening study materials...")
        
        if st.button("📅 My Schedule", use_container_width=True):
            st.info("Opening your schedule...")
        
        if st.button("📊 Academic Progress", use_container_width=True):
            st.info("Opening academic progress...")
    
    # Bottom section - Notifications
    st.markdown("---")
    st.markdown("### 🔔 Recent Notifications")
    
    notifications = [
        {"type": "📬", "message": "New message from Alex Johnson", "time": "5 min ago"},
        {"type": "👥", "message": "Sarah Miller sent you a friend request", "time": "1 hour ago"},
        {"type": "📅", "message": "Reminder: Alumni talk tomorrow at 3 PM", "time": "3 hours ago"},
        {"type": "👥", "message": "You've been added to 'Science Study Group'", "time": "1 day ago"}
    ]
    
    for notif in notifications:
        col1, col2 = st.columns([1, 11])
        with col1:
            st.write(notif['type'])
        with col2:
            st.write(f"**{notif['message']}**")
            st.caption(notif['time'])
