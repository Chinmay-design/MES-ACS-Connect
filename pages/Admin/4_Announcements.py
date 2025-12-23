import streamlit as st
import json
from datetime import datetime, timedelta

def admin_announcements_page():
    st.markdown('<h1 class="main-header">📢 Announcements Management</h1>', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📝 Create Announcement", "📋 All Announcements", "📊 Analytics"])
    
    with tab1:
        st.markdown("### Create New Announcement")
        
        with st.form("create_announcement_form"):
            # Basic information
            title = st.text_input("Title *", placeholder="Important Announcement")
            content = st.text_area("Content *", height=150, 
                                 placeholder="Enter announcement details...")
            
            # Media attachments
            st.markdown("### 🖼️ Media Attachments")
            col1, col2 = st.columns(2)
            with col1:
                uploaded_images = st.file_uploader("Upload Images", 
                                                 type=['jpg', 'png', 'jpeg', 'gif'],
                                                 accept_multiple_files=True,
                                                 help="Upload up to 5 images")
            with col2:
                uploaded_videos = st.file_uploader("Upload Videos", 
                                                 type=['mp4', 'mov', 'avi'],
                                                 accept_multiple_files=True,
                                                 help="Upload up to 2 videos")
            
            if uploaded_images:
                st.success(f"📸 {len(uploaded_images)} image(s) selected")
            if uploaded_videos:
                st.success(f"🎥 {len(uploaded_videos)} video(s) selected")
            
            # Announcement settings
            st.markdown("### ⚙️ Announcement Settings")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                announcement_type = st.selectbox("Type *", 
                                               ["General", "Urgent", "Event", "Academic", "Warning", "Other"])
                priority = st.select_slider("Priority", 
                                          options=["Low", "Medium", "High", "Critical"], 
                                          value="Medium")
            with col2:
                target_roles = st.multiselect("Target Audience *", 
                                            ["Students", "Alumni", "All Users"])
                publish_option = st.radio("Publish", ["Now", "Schedule"])
            with col3:
                if publish_option == "Schedule":
                    publish_date = st.date_input("Schedule Date", 
                                               min_value=datetime.today(),
                                               value=datetime.today() + timedelta(days=1))
                    publish_time = st.time_input("Schedule Time", 
                                               value=datetime.strptime("10:00", "%H:%M").time())
                
                expires = st.checkbox("Set expiry date")
                if expires:
                    expiry_date = st.date_input("Expiry Date", 
                                              min_value=datetime.today(),
                                              value=datetime.today() + timedelta(days=7))
            
            # Target specific groups/users
            st.markdown("### 🎯 Targeted Distribution")
            
            col1, col2 = st.columns(2)
            with col1:
                target_groups = st.multiselect("Target Groups (Optional)", 
                                             ["Science Students", "Commerce Students", "Arts Students",
                                              "All Alumni", "2024 Batch", "Club Members"])
            with col2:
                target_users_input = st.text_area("Specific User IDs (Optional)", 
                                                placeholder="Enter comma-separated user IDs\nExample: 101, 102, 103",
                                                height=100)
            
            # Preview section
            st.markdown("### 👁️ Preview")
            with st.expander("Show Preview"):
                st.markdown(f"**Title:** {title if title else '[Title]'}")
                st.markdown(f"**Type:** {announcement_type}")
                st.markdown(f"**Priority:** {priority}")
                st.markdown(f"**Target:** {', '.join(target_roles) if target_roles else 'All Users'}")
                st.markdown("**Content:**")
                st.write(content if content else '[Content will appear here]')
            
            # Submit button
            if st.form_submit_button("🚀 Publish Announcement", use_container_width=True):
                if not title or not content:
                    st.error("Title and content are required")
                elif not target_roles:
                    st.error("Please select target audience")
                else:
                    # Prepare announcement data
                    announcement_data = {
                        'title': title,
                        'content': content,
                        'type': announcement_type.lower(),
                        'priority': priority,
                        'target_roles': json.dumps(target_roles),
                        'is_published': 1 if publish_option == "Now" else 0
                    }
                    
                    st.success("✅ Announcement published successfully!")
                    st.balloons()
                    
                    # Show success details
                    st.markdown(f"""
                    <div class="success-box">
                    <strong>Announcement Published!</strong><br>
                    • Title: {title}<br>
                    • Type: {announcement_type}<br>
                    • Priority: {priority}<br>
                    • Target: {', '.join(target_roles)}<br>
                    • Status: {f'Scheduled for {publish_date} at {publish_time}' if publish_option == 'Schedule' else 'Published Now'}
                    </div>
                    """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### All Announcements")
        
        # Search and filter
        col1, col2, col3 = st.columns(3)
        with col1:
            search_ann = st.text_input("Search announcements")
        with col2:
            filter_type = st.selectbox("Filter by type", ["All", "General", "Urgent", "Event", "Academic"])
        with col3:
            filter_status = st.selectbox("Filter by status", ["All", "Active", "Expired", "Scheduled"])
        
        # Announcements list
        announcements = [
            {"id": 1, "title": "Exam Schedule Released", "type": "Academic", "priority": "High", 
             "published": "2024-01-15", "views": 245, "status": "Active", "author": "Admin"},
            {"id": 2, "title": "Campus Maintenance Notice", "type": "General", "priority": "Medium", 
             "published": "2024-01-10", "views": 180, "status": "Expired", "author": "Admin"},
            {"id": 3, "title": "Holiday Announcement", "type": "General", "priority": "Low", 
             "published": "2024-01-05", "views": 320, "status": "Active", "author": "Admin"},
            {"id": 4, "title": "Workshop Registration", "type": "Event", "priority": "Medium", 
             "published": "2024-01-12", "views": 150, "status": "Active", "author": "Admin"},
            {"id": 5, "title": "System Upgrade", "type": "Warning", "priority": "Critical", 
             "published": "2024-01-18", "views": 420, "status": "Active", "author": "Admin"}
        ]
        
        # Apply filters
        if filter_type != "All":
            announcements = [a for a in announcements if a['type'] == filter_type]
        if filter_status != "All":
            announcements = [a for a in announcements if a['status'] == filter_status]
        if search_ann:
            announcements = [a for a in announcements if search_ann.lower() in a['title'].lower()]
        
        # Display announcements
        for ann in announcements:
            with st.expander(f"{ann['title']} - {ann['published']} ({ann['status']})"):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**Type:** {ann['type']}")
                    st.write(f"**Priority:** {ann['priority']}")
                    st.write(f"**Views:** {ann['views']}")
                    st.write(f"**Author:** {ann['author']}")
                with col2:
                    if st.button("✏️ Edit", key=f"edit_{ann['id']}", use_container_width=True):
                        st.info(f"Editing announcement {ann['id']}")
                with col3:
                    if st.button("🗑️ Delete", key=f"delete_{ann['id']}", use_container_width=True):
                        st.warning(f"Delete announcement '{ann['title']}'?")
                        if st.button("Confirm Delete", key=f"confirm_del_{ann['id']}"):
                            st.error(f"Deleted announcement {ann['id']}")
    
    with tab3:
        st.markdown("### 📊 Announcement Analytics")
        
        # Statistics cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Announcements", "48", "+5")
        with col2:
            st.metric("Avg. Views", "215", "+12")
        with col3:
            st.metric("Engagement Rate", "68%", "+3%")
        with col4:
            st.metric("Active Now", "12", "-2")
        
        # Viewership chart
        st.markdown("#### 👀 Viewership Trend")
        
        # Sample data for chart
        import plotly.graph_objects as go
        
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        views = [150, 180, 220, 240, 210, 120, 90]
        
        fig = go.Figure(data=[
            go.Bar(x=days, y=views, name='Views', marker_color='#3b82f6')
        ])
        
        fig.update_layout(
            title='Weekly Announcement Views',
            xaxis_title='Day',
            yaxis_title='Views',
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Top performing announcements
        st.markdown("#### 🏆 Top Performing Announcements")
        
        top_announcements = [
            {"title": "System Upgrade Notice", "views": 420, "engagement": "85%"},
            {"title": "Exam Schedule", "views": 320, "engagement": "78%"},
            {"title": "Holiday Announcement", "views": 245, "engagement": "72%"}
        ]
        
        for ann in top_announcements:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{ann['title']}**")
            with col2:
                st.write(f"👀 {ann['views']}")
            with col3:
                st.write(f"📈 {ann['engagement']}")
