import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

def admin_dashboard_page():
    st.markdown('<h1 class="main-header">🛠️ Admin Dashboard</h1>', unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Users", "1,245", "+23")
    with col2:
        st.metric("Active Today", "342", "-12")
    with col3:
        st.metric("Pending Approvals", "15", "+3")
    with col4:
        st.metric("Groups", "48", "+2")
    
    st.markdown("---")
    
    # Role switching tabs
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "👨‍🎓 Student Management", "👨‍🎓 Alumni Management"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # User distribution chart
            st.markdown("### 👥 User Distribution")
            user_data = pd.DataFrame({
                'Role': ['Students', 'Alumni', 'Admins'],
                'Count': [800, 400, 45]
            })
            
            fig = px.pie(user_data, values='Count', names='Role', 
                        color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b'],
                        hole=0.3)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Daily active users
            st.markdown("### 📈 Daily Active Users")
            
            # Generate sample data for last 7 days
            dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7, 0, -1)]
            active_data = pd.DataFrame({
                'Date': dates,
                'Active Users': [300, 320, 350, 380, 400, 250, 200]
            })
            
            fig2 = px.line(active_data, x='Date', y='Active Users', 
                          title='Last 7 Days Activity',
                          markers=True)
            fig2.update_traces(line=dict(color='#3b82f6', width=3))
            st.plotly_chart(fig2, use_container_width=True)
        
        # Recent activities
        st.markdown("### ⚡ Recent Activities")
        
        activities = [
            {"user": "John Doe", "action": "Created new group 'Science Club'", "time": "10 min ago", "role": "Student"},
            {"user": "Sarah Smith", "action": "Posted anonymous confession", "time": "25 min ago", "role": "Student"},
            {"user": "Admin", "action": "Approved 5 student registrations", "time": "1 hour ago", "role": "Admin"},
            {"user": "Mike Chen", "action": "Reported inappropriate content", "time": "2 hours ago", "role": "Student"},
            {"user": "Dr. Robert Brown", "action": "Made $500 donation", "time": "3 hours ago", "role": "Alumni"}
        ]
        
        for act in activities:
            role_color = {
                "Student": "#3b82f6",
                "Alumni": "#10b981", 
                "Admin": "#f59e0b"
            }.get(act['role'], "#6b7280")
            
            st.markdown(f"""
            <div style="padding: 0.5rem; border-bottom: 1px solid #e5e7eb; display: flex; align-items: center;">
                <div style="background: {role_color}; color: white; padding: 2px 8px; border-radius: 12px; 
                          font-size: 0.8em; margin-right: 10px;">
                    {act['role'][0]}
                </div>
                <div>
                    <strong>{act['user']}</strong> {act['action']}<br>
                    <small style="color: #6b7280;">{act['time']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # System health
        st.markdown("### 🏥 System Health")
        
        health_col1, health_col2, health_col3, health_col4 = st.columns(4)
        with health_col1:
            st.metric("API Response", "98%", "2%")
        with health_col2:
            st.metric("Server Load", "45%", "-5%")
        with health_col3:
            st.metric("Database", "Healthy", "0%")
        with health_col4:
            st.metric("Uptime", "99.9%", "0%")
    
    with tab2:
        from pages.Admin._2_Student_Management import student_management_section
        student_management_section()
    
    with tab3:
        from pages.Admin._3_Alumni_Management import alumni_management_section
        alumni_management_section()

def student_management_section():
    st.markdown("### 👨‍🎓 Student Management")
    
    # Quick actions
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📋 View All", use_container_width=True):
            st.session_state.page = "Admin/2_Student_Management"
            st.rerun()
    with col2:
        if st.button("✅ Approve Pending", use_container_width=True):
            st.success("5 pending students approved")
    with col3:
        if st.button("📧 Send Bulk Email", use_container_width=True):
            st.info("Bulk email composer")
    with col4:
        if st.button("📊 Generate Report", use_container_width=True):
            st.success("Student report generated")
    
    # Student statistics
    st.markdown("#### 📊 Student Statistics")
    
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    with stats_col1:
        st.metric("Total Students", "800", "+15")
    with stats_col2:
        st.metric("1st Year PUC", "400", "+8")
    with stats_col3:
        st.metric("2nd Year PUC", "400", "+7")
    with stats_col4:
        st.metric("Pending", "15", "-3")
    
    # Recent student registrations
    st.markdown("#### 📝 Recent Registrations")
    
    recent_students = [
        {"name": "John Carter", "id": "MES20240012", "date": "2024-01-15", "status": "Pending"},
        {"name": "Priya Sharma", "id": "MES20240013", "date": "2024-01-14", "status": "Approved"},
        {"name": "Raj Patel", "id": "MES20240014", "date": "2024-01-13", "status": "Approved"}
    ]
    
    for student in recent_students:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"**{student['name']}**")
            st.caption(f"ID: {student['id']} • Registered: {student['date']}")
        with col2:
            if student['status'] == 'Pending':
                if st.button("Approve", key=f"app_{student['id']}"):
                    st.success(f"Approved {student['name']}")
        with col3:
            if st.button("View", key=f"view_{student['id']}"):
                st.info(f"Viewing {student['name']}")
        with col4:
            if st.button("Contact", key=f"contact_{student['id']}"):
                st.info(f"Contacting {student['name']}")

def alumni_management_section():
    st.markdown("### 👨‍🎓 Alumni Management")
    
    # Quick actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("👥 View All Alumni", use_container_width=True):
            st.session_state.page = "Admin/3_Alumni_Management"
            st.rerun()
    with col2:
        if st.button("📧 Newsletter", use_container_width=True):
            st.info("Alumni newsletter composer")
    with col3:
        if st.button("💰 Contribution Report", use_container_width=True):
            st.success("Contribution report generated")
    
    # Alumni statistics
    st.markdown("#### 📊 Alumni Statistics")
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    with stats_col1:
        st.metric("Total Alumni", "400", "+8")
    with stats_col2:
        st.metric("Active This Month", "156", "+12")
    with stats_col3:
        st.metric("Total Contributions", "$50,000", "+$5,000")
    
    # Top contributors
    st.markdown("#### 🏆 Top Contributors")
    
    contributors = [
        {"name": "Dr. Robert Brown", "amount": "$5,000", "year": 2020},
        {"name": "Lisa Taylor", "amount": "$3,500", "year": 2021},
        {"name": "David Wilson", "amount": "$2,000", "year": 2022}
    ]
    
    for contributor in contributors:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{contributor['name']}**")
            st.caption(f"Batch: {contributor['year']}")
        with col2:
            st.write(f"**{contributor['amount']}**")
        with col3:
            if st.button("Thank", key=f"thank_{contributor['name']}"):
                st.success(f"Thank you note sent to {contributor['name']}")
