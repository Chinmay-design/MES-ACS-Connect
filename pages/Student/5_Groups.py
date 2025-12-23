import streamlit as st

def student_groups_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">👥 Groups</h1>', unsafe_allow_html=True)
    
    # Tabs for different group sections
    tab1, tab2, tab3, tab4 = st.tabs(["📋 My Groups", "🔍 Discover Groups", "➕ Create Group", "📢 Group Announcements"])
    
    with tab1:
        st.markdown("### Your Groups")
        
        # Search my groups
        search_my_groups = st.text_input("Search your groups...", placeholder="Type group name")
        
        # User's groups
        my_groups = [
            {"name": "Science Study Group", "members": 24, "category": "Academic", "role": "Admin", 
             "activity": "High", "last_active": "2 hours ago"},
            {"name": "Math Club", "members": 15, "category": "Academic", "role": "Member", 
             "activity": "Medium", "last_active": "1 day ago"},
            {"name": "Basketball Team", "members": 12, "category": "Sports", "role": "Member", 
             "activity": "High", "last_active": "5 hours ago"},
            {"name": "Music Society", "members": 32, "category": "Arts", "role": "Moderator", 
             "activity": "Medium", "last_active": "3 days ago"},
            {"name": "Coding Club", "members": 42, "category": "Technology", "role": "Member", 
             "activity": "High", "last_active": "1 hour ago"}
        ]
        
        # Filter groups
        if search_my_groups:
            my_groups = [g for g in my_groups if search_my_groups.lower() in g['name'].lower()]
        
        # Display groups
        for group in my_groups:
            with st.expander(f"{group['name']} ({group['role']})"):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**Category:** {group['category']}")
                    st.write(f"**Members:** {group['members']}")
                    st.write(f"**Activity:** {group['activity']}")
                    st.write(f"**Last active:** {group['last_active']}")
                with col2:
                    if st.button("💬 Chat", key=f"gchat_{group['name']}", use_container_width=True):
                        st.info(f"Opening {group['name']} chat")
                with col3:
                    if st.button("👀 View", key=f"gview_{group['name']}", use_container_width=True):
                        st.info(f"Viewing {group['name']} details")
        
        if not my_groups:
            st.info("You haven't joined any groups yet. Discover groups to join!")
    
    with tab2:
        st.markdown("### Discover Groups")
        
        # Search and filters
        col1, col2, col3 = st.columns(3)
        with col1:
            search_groups = st.text_input("Search groups...")
        with col2:
            category_filter = st.selectbox("Category", ["All", "Academic", "Sports", "Arts", "Technology", "Social"])
        with col3:
            privacy_filter = st.selectbox("Privacy", ["All", "Public", "Private"])
        
        # Available groups
        groups = [
            {"name": "Physics Study Group", "members": 18, "category": "Academic", "privacy": "Public", 
             "description": "For physics enthusiasts", "rating": "4.8"},
            {"name": "Debate Society", "members": 28, "category": "Academic", "privacy": "Private", 
             "description": "Sharpen your debating skills", "rating": "4.5"},
            {"name": "Photography Club", "members": 15, "category": "Arts", "privacy": "Public", 
             "description": "For photography lovers", "rating": "4.2"},
            {"name": "Robotics Club", "members": 25, "category": "Technology", "privacy": "Public", 
             "description": "Build and compete with robots", "rating": "4.9"},
            {"name": "Environmental Club", "members": 20, "category": "Social", "privacy": "Public", 
             "description": "Promote environmental awareness", "rating": "4.3"}
        ]
        
        # Apply filters
        if category_filter != "All":
            groups = [g for g in groups if g['category'] == category_filter]
        if privacy_filter != "All":
            groups = [g for g in groups if g['privacy'] == privacy_filter]
        if search_groups:
            groups = [g for g in groups if search_groups.lower() in g['name'].lower()]
        
        # Display groups
        for group in groups:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{group['name']}**")
                st.caption(f"{group['category']} • {group['members']} members • ⭐ {group['rating']}")
                st.caption(group['description'])
                st.caption(f"Privacy: {group['privacy']}")
            with col2:
                if st.button("Join", key=f"join_{group['name']}", use_container_width=True):
                    # Check schedule conflicts
                    has_conflict = False  # Simulated check
                    if has_conflict:
                        st.error("Cannot join: Schedule conflict detected!")
                    else:
                        st.success(f"Join request sent to {group['name']}")
            with col3:
                if st.button("Info", key=f"info_{group['name']}", use_container_width=True):
                    st.info(f"Group info: {group}")
    
    with tab3:
        st.markdown("### Create New Group")
        
        with st.form("create_group_form"):
            # Basic Information
            st.markdown("#### 📝 Basic Information")
            group_name = st.text_input("Group Name *", placeholder="Enter group name")
            description = st.text_area("Description *", 
                                     placeholder="Describe your group's purpose, activities, and goals...",
                                     height=100)
            
            # Group Settings
            st.markdown("#### ⚙️ Group Settings")
            col1, col2 = st.columns(2)
            with col1:
                category = st.selectbox("Category *", 
                                      ["Academic", "Sports", "Arts", "Technology", "Social", "Other"])
                group_type = st.selectbox("Group Type *", 
                                        ["Student Only", "Mixed (Students & Alumni)", "Open to All"])
            with col2:
                privacy = st.selectbox("Privacy *", 
                                     ["Public (Anyone can join)", 
                                      "Private (Request to join)", 
                                      "Restricted (Invite only)"])
                max_members = st.number_input("Maximum Members", 
                                            min_value=2, max_value=500, value=100)
            
            # Schedule Restrictions
            st.markdown("#### ⚠️ Schedule Restrictions")
            st.info("""
            **Important:** Members cannot join groups that conflict with their academic schedule.
            The system will automatically check for conflicts when users try to join.
            """)
            
            # Group Rules
            st.markdown("#### 📜 Group Rules")
            rules = st.text_area("Group Rules (Optional)", 
                               placeholder="Enter rules for group members...\nExample:\n1. Be respectful\n2. No spam\n3. Stay on topic",
                               height=100)
            
            # Submit
            if st.form_submit_button("🚀 Create Group", use_container_width=True):
                if group_name and description:
                    st.success(f"Group '{group_name}' created successfully!")
                    st.info("Your group is now active. Share it with others!")
                else:
                    st.error("Please fill all required fields (*)")
    
    with tab4:
        st.markdown("### 📢 Group Announcements")
        
        # Group announcements feed
        announcements = [
            {"group": "Science Study Group", "title": "Weekly Study Session", 
             "content": "This Saturday at 3 PM in Library Room 204", "time": "2 hours ago", "author": "Group Admin"},
            {"group": "Math Club", "title": "Math Olympiad Registration", 
             "content": "Registration open for inter-college math competition", "time": "1 day ago", "author": "Club President"},
            {"group": "Music Society", "title": "Annual Music Fest Auditions", 
             "content": "Auditions for annual music festival next week", "time": "2 days ago", "author": "Society Head"}
        ]
        
        for ann in announcements:
            with st.expander(f"{ann['group']}: {ann['title']} - {ann['time']}"):
                st.write(f"**Posted by:** {ann['author']}")
                st.write(f"**Content:** {ann['content']}")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("👍 Like", key=f"like_{ann['group']}_{ann['title']}"):
                        st.success("Liked!")
                with col_b:
                    if st.button("💬 Comment", key=f"comment_{ann['group']}_{ann['title']}"):
                        comment = st.text_input("Add a comment", key=f"com_{ann['group']}_{ann['title']}")
                        if comment:
                            st.success("Comment added!")
