import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

def admin_analytics_page():
    st.markdown('<h1 class="main-header">📈 System Analytics</h1>', unsafe_allow_html=True)
    
    # Tabs for different analytics
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "👥 User Analytics", "💬 Engagement", "📥 Downloads"])
    
    with tab1:
        st.markdown("### System Overview")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Users", "1,245", "+2.3%")
        with col2:
            st.metric("Active Today", "342", "-1.2%")
        with col3:
            st.metric("New This Month", "45", "+15%")
        with col4:
            st.metric("Engagement Rate", "68%", "+3%")
        
        # User growth chart
        st.markdown("### 📈 User Growth Trend")
        
        # Generate sample data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        students = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420]
        alumni = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=students, mode='lines+markers', name='Students', line=dict(color='#3b82f6', width=3)))
        fig.add_trace(go.Scatter(x=months, y=alumni, mode='lines+markers', name='Alumni', line=dict(color='#10b981', width=3)))
        
        fig.update_layout(
            title='Monthly User Growth',
            xaxis_title='Month',
            yaxis_title='Number of Users',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Platform usage
        st.markdown("### 📱 Platform Usage")
        
        platform_data = pd.DataFrame({
            'Platform': ['Web', 'Mobile Web', 'iOS', 'Android'],
            'Usage': [45, 30, 15, 10]
        })
        
        fig2 = px.pie(platform_data, values='Usage', names='Platform', 
                     color_discrete_sequence=['#3b82f6', '#60a5fa', '#93c5fd', '#bfdbfe'])
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        st.markdown("### 👥 User Analytics")
        
        # User demographics
        st.markdown("#### 🎓 Academic Distribution")
        
        academic_data = pd.DataFrame({
            'Stream': ['Science', 'Commerce', 'Arts'],
            'Students': [400, 300, 100],
            'Alumni': [200, 150, 50]
        })
        
        fig = px.bar(academic_data, x='Stream', y=['Students', 'Alumni'], 
                    barmode='group', title='Users by Stream',
                    color_discrete_sequence=['#3b82f6', '#10b981'])
        st.plotly_chart(fig, use_container_width=True)
        
        # Year-wise distribution
        st.markdown("#### 📅 Year-wise Distribution")
        
        year_data = pd.DataFrame({
            'Year': ['1st Year PUC', '2nd Year PUC'],
            'Count': [400, 400]
        })
        
        fig2 = px.pie(year_data, values='Count', names='Year', 
                     title='Student Year Distribution')
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        st.markdown("### 💬 Engagement Analytics")
        
        # Engagement metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Daily Posts", "45", "+5")
        with col2:
            st.metric("Comments", "128", "+12")
        with col3:
            st.metric("Messages", "342", "+23")
        
        # Activity by time of day
        st.markdown("#### ⏰ Activity by Time of Day")
        
        hours = list(range(24))
        activity = [10, 8, 5, 3, 2, 5, 15, 45, 65, 75, 80, 85, 
                   80, 75, 70, 75, 85, 90, 95, 85, 70, 45, 25, 15]
        
        fig = go.Figure(data=[
            go.Scatter(x=hours, y=activity, mode='lines+markers', 
                      line=dict(color='#8b5cf6', width=3))
        ])
        
        fig.update_layout(
            title='Hourly Activity Pattern',
            xaxis_title='Hour of Day',
            yaxis_title='Active Users',
            xaxis=dict(tickmode='linear', dtick=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature usage
        st.markdown("#### 🛠️ Feature Usage")
        
        features = ['Chat', 'Groups', 'Confessions', 'Events', 'Friends']
        usage = [85, 70, 65, 45, 80]
        
        fig2 = px.bar(x=features, y=usage, title='Feature Usage Percentage',
                     labels={'x': 'Feature', 'y': 'Usage %'},
                     color=usage, color_continuous_scale='Blues')
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab4:
        st.markdown("### 📥 Reports & Downloads")
        
        # Report types
        st.markdown("#### 📋 Available Reports")
        
        reports = [
            {"name": "User Registration Report", "format": "CSV/Excel", "size": "1.2MB"},
            {"name": "Activity Log Report", "format": "CSV/Excel", "size": "3.5MB"},
            {"name": "Financial Report", "format": "PDF", "size": "2.1MB"},
            {"name": "System Health Report", "format": "PDF", "size": "0.8MB"}
        ]
        
        for report in reports:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.write(f"**{report['name']}**")
            with col2:
                st.write(report['format'])
            with col3:
                st.write(report['size'])
            with col4:
                if st.button("Download", key=f"dl_{report['name']}"):
                    st.success(f"Downloading {report['name']}")
        
        # Custom report generator
        st.markdown("#### 🛠️ Custom Report Generator")
        
        with st.form("custom_report"):
            report_type = st.selectbox("Report Type", 
                                     ["User Activity", "Financial", "Engagement", "System Logs"])
            
            date_range = st.date_input(
                "Date Range",
                value=(datetime.now() - timedelta(days=30), datetime.now()),
                max_value=datetime.now()
            )
            
            format_type = st.radio("Export Format", ["CSV", "Excel", "PDF"])
            
            include_charts = st.checkbox("Include charts", value=True)
            
            if st.form_submit_button("Generate Report", use_container_width=True):
                st.success(f"Generating {report_type} report...")
                st.info("Report will be ready for download shortly")
