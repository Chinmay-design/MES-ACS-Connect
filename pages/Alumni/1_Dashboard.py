import streamlit as st
import pandas as pd
from datetime import datetime

def alumni_dashboard_page():
    user = st.session_state.user
    
    st.markdown(f'<h1 class="main-header">Welcome Back, {user["first_name"]}! 👨‍🎓</h1>', unsafe_allow_html=True)
    
    # Professional stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👥 Connections", "156", "+8")
    with col2:
        st.metric("👨‍🏫 Mentees", "3", "+1")
    with col3:
        st.metric("📅 Events", "4", "+1")
    with col4:
        st.metric("💰 Contributions", "$2,500", "+$500")
    
    st.markdown("---")
    
    # Main content in two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Professional Network Updates
        st.markdown("### 🤝 Professional Network")
        
        # Connection requests
        st.markdown("#### 📨 Connection Requests")
        requests = [
            {
                "name": "John Carter", 
                "position": "Senior Software Engineer", 
                "company": "Google", 
                "batch": "2020",
                "mutual": 5
            },
            {
                "name": "Priya Sharma", 
                "position": "Product Manager", 
                "company": "Microsoft", 
                "batch": "2021",
                "mutual": 3
            },
            {
                "name": "Raj Patel", 
                "position": "Data Scientist", 
                "company": "Amazon", 
                "batch": "2019",
                "mutual": 8
            }
        ]
        
        for req in requests:
            col_a, col_b, col_c, col_d = st.columns([4, 1, 1, 1])
            with col_a:
                st.write(f"**{req['name']}**")
                st.caption(f"{req['position']} at {req['company']}")
                st.caption(f"Batch {req['batch']} • 👥 {req['mutual']} mutual connections")
            with col_b:
                if st.button("✅", key=f"acc_alum_{req['name']}", help="Accept"):
                    st.success(f"Connected with {req['name']}")
            with col_c:
                if st.button("❌", key=f"rej_alum_{req['name']}", help="Reject"):
                    st.info(f"Ignored {req['name']}")
            with col_d:
                if st.button("👀", key=f"view_alum_{req['name']}", help="View Profile"):
                    st.info(f"Viewing {req['name']}'s profile")
        
        # Job Opportunities
        st.markdown("#### 💼 Job Opportunities")
        
        jobs = [
            {
                "title": "Senior Full Stack Developer",
                "company": "Amazon",
                "location": "Bangalore",
                "type": "Full-time",
                "posted": "2 days ago",
                "match": "95%"
            },
            {
                "title": "Data Science Lead",
                "company": "Microsoft",
                "location": "Hyderabad",
                "type": "Full-time",
                "posted": "1 week ago",
                "match": "88%"
            },
            {
                "title": "Product Manager",
                "company": "StartupXYZ",
                "location": "Remote",
                "type": "Contract",
                "posted": "3 days ago",
                "match": "92%"
            }
        ]
        
        for job in jobs:
            with st.expander(f"{job['title']} - {job['company']} ({job['match']} match)"):
                st.write(f"**Location:** {job['location']}")
                st.write(f"**Type:** {job['type']}")
                st.write(f"**Posted:** {job['posted']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("Apply", key=f"apply_{job['title']}"):
                        st.info("Redirecting to application...")
                with col_b:
                    if st.button("Save", key=f"save_{job['title']}"):
                        st.success("Job saved to your list!")
        
        # Quick Actions for Alumni
        st.markdown("### ⚡ Quick Actions")
        
        action_col1, action_col2, action_col3 = st.columns(3)
        with action_col1:
            if st.button("🤝 Network", use_container_width=True, icon="🤝"):
                st.session_state.page = "Alumni/3_Networking"
                st.rerun()
        with action_col2:
            if st.button("💼 Post Job", use_container_width=True, icon="💼"):
                st.info("Post a job opportunity")
        with action_col3:
            if st.button("👨‍🏫 Mentor", use_container_width=True, icon="👨‍🏫"):
                st.info("Become a mentor")
    
    with col2:
        # Alumni Reunions
        st.markdown("### 🎓 Alumni Reunions")
        
        reunions = [
            {
                "batch": "2015 Batch Reunion",
                "date": "Apr 15, 2024",
                "location": "Main Campus",
                "confirmed": 45,
                "status": "Open"
            },
            {
                "batch": "2010 Silver Jubilee",
                "date": "May 20, 2024",
                "location": "Virtual",
                "confirmed": 120,
                "status": "Open"
            },
            {
                "batch": "2005 Batch Meet",
                "date": "Jun 10, 2024",
                "location": "City Hotel",
                "confirmed": 65,
                "status": "Open"
            }
        ]
        
        for reunion in reunions:
            st.markdown(f"""
            <div class="card">
                <strong>{reunion['batch']}</strong><br>
                📅 {reunion['date']}<br>
                📍 {reunion['location']}<br>
                👥 {reunion['confirmed']} confirmed<br>
                <small>Status: <strong>{reunion['status']}</strong></small>
            </div>
            """, unsafe_allow_html=True)
            
            if reunion['status'] == 'Open':
                if st.button("RSVP", key=f"rsvp_{reunion['batch']}", use_container_width=True):
                    st.success(f"RSVP'd for {reunion['batch']}!")
        
        # Contribution Section
        st.markdown("### 💰 Make a Contribution")
        
        contribution_type = st.selectbox(
            "Contribution Type",
            ["Scholarship Fund", "Infrastructure", "Library Development", 
             "Sports Facilities", "Mentorship Program", "General Fund"]
        )
        
        amount = st.number_input(
            "Amount ($)", 
            min_value=10, 
            max_value=10000, 
            value=100,
            step=10
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            recurring = st.checkbox("Monthly donation")
        with col_b:
            anonymous = st.checkbox("Donate anonymously")
        
        if st.button("🤝 Donate Now", use_container_width=True):
            st.success(f"Thank you for your ${amount} donation to {contribution_type}!")
            st.balloons()
        
        # Quick Stats
        st.markdown("### 📊 Your Impact")
        
        impact_stats = {
            "Total Donated": "$2,500",
            "Students Helped": "12",
            "Mentorship Hours": "45",
            "Events Hosted": "3"
        }
        
        for stat, value in impact_stats.items():
            col_stat1, col_stat2 = st.columns([2, 1])
            with col_stat1:
                st.write(stat)
            with col_stat2:
                st.write(f"**{value}**")
    
    # Bottom section - Alumni News
    st.markdown("---")
    st.markdown("### 📰 Alumni News")
    
    news_items = [
        {"title": "Alumnus starts successful AI startup", "summary": "John Doe (2015) raises $5M funding", "date": "2 days ago"},
        {"title": "Alumni association scholarship announced", "summary": "10 scholarships for current students", "date": "1 week ago"},
        {"title": "Annual alumni meet photos", "summary": "Check out photos from last reunion", "date": "2 weeks ago"}
    ]
    
    for news in news_items:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{news['title']}**")
            st.caption(news['summary'])
        with col2:
            st.caption(news['date'])
            if st.button("Read", key=f"read_{news['title']}"):
                st.info(f"Reading: {news['title']}")
