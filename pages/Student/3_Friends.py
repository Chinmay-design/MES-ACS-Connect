import streamlit as st

def student_friends_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">👥 Friends</h1>', unsafe_allow_html=True)
    
    # Tabs for different friend sections
    tab1, tab2, tab3, tab4 = st.tabs(["👥 Friends List", "📨 Friend Requests", "🔍 Find Friends", "🚫 Blocked Users"])
    
    with tab1:
        st.markdown("### Your Friends")
        
        # Friends list with search
        search_friend = st.text_input("🔍 Search friends...", placeholder="Search by name")
        
        # Friends grid
        friends = [
            {"name": "Alex Johnson", "year": "2nd Year PUC", "stream": "Science", "mutual": 8, "status": "Online"},
            {"name": "Sarah Miller", "year": "1st Year PUC", "stream": "Commerce", "mutual": 5, "status": "Offline"},
            {"name": "Mike Chen", "year": "2nd Year PUC", "stream": "Science", "mutual": 12, "status": "Online"},
            {"name": "Emma Wilson", "year": "1st Year PUC", "stream": "Arts", "mutual": 3, "status": "Offline"},
            {"name": "David Brown", "year": "2nd Year PUC", "stream": "Commerce", "mutual": 7, "status": "Online"},
            {"name": "Lisa Taylor", "year": "1st Year PUC", "stream": "Arts", "mutual": 4, "status": "Offline"}
        ]
        
        # Filter friends based on search
        if search_friend:
            friends = [f for f in friends if search_friend.lower() in f['name'].lower()]
        
        # Display friends in a grid
        cols = st.columns(3)
        for idx, friend in enumerate(friends):
            with cols[idx % 3]:
                st.markdown(f"""
                <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; text-align: center;">
                    <div style="font-size: 2rem;">👤</div>
                    <strong>{friend['name']}</strong><br>
                    <small>{friend['year']} • {friend['stream']}</small><br>
                    <small>👥 {friend['mutual']} mutual friends</small><br>
                    <small>{'🟢 Online' if friend['status'] == 'Online' else '⚫ Offline'}</small>
                </div>
                """, unsafe_allow_html=True)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("💬 Chat", key=f"chat_{friend['name']}", use_container_width=True):
                        st.session_state.page = "Student/4_Chat"
                        st.rerun()
                with col_b:
                    if st.button("👀 View", key=f"view_{friend['name']}", use_container_width=True):
                        st.info(f"Viewing {friend['name']}'s profile")
        
        if not friends:
            st.info("No friends found. Try adding some friends!")
    
    with tab2:
        st.markdown("### Friend Requests")
        
        # Incoming requests
        st.markdown("#### 📥 Incoming Requests")
        incoming_requests = [
            {"name": "John Carter", "id": "MES20240012", "stream": "Science", "time": "2 days ago"},
            {"name": "Priya Sharma", "id": "MES20240025", "stream": "Commerce", "time": "1 day ago"}
        ]
        
        for req in incoming_requests:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.write(f"**{req['name']}**")
                st.caption(f"ID: {req['id']} • {req['stream']} • {req['time']}")
            with col2:
                if st.button("✅ Accept", key=f"acc_{req['id']}"):
                    st.success(f"Accepted {req['name']}'s request")
            with col3:
                if st.button("❌ Reject", key=f"rej_{req['id']}"):
                    st.info(f"Rejected {req['name']}'s request")
            with col4:
                if st.button("🚫 Block", key=f"blk_{req['id']}"):
                    st.error(f"Blocked {req['name']}")
        
        # Outgoing requests
        st.markdown("#### 📤 Outgoing Requests")
        outgoing_requests = [
            {"name": "Raj Patel", "id": "MES20240018", "stream": "Science", "time": "3 days ago", "status": "Pending"},
            {"name": "Anjali Gupta", "id": "MES20240022", "stream": "Arts", "time": "1 week ago", "status": "Pending"}
        ]
        
        for req in outgoing_requests:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{req['name']}**")
                st.caption(f"ID: {req['id']} • {req['stream']} • {req['time']} • {req['status']}")
            with col2:
                if st.button("↩️ Cancel", key=f"cancel_{req['id']}"):
                    st.info(f"Cancelled request to {req['name']}")
    
    with tab3:
        st.markdown("### 🔍 Find Friends")
        
        # Search and filters
        col1, col2, col3 = st.columns(3)
        with col1:
            search_name = st.text_input("Search by name")
        with col2:
            filter_year = st.selectbox("Filter by Year", ["All", "1st Year PUC", "2nd Year PUC"])
        with col3:
            filter_stream = st.selectbox("Filter by Stream", ["All", "Science", "Commerce", "Arts"])
        
        # Suggested friends
        st.markdown("#### 🤝 Suggested Friends")
        
        suggestions = [
            {"name": "Kumar Singh", "id": "MES20240030", "stream": "Science", "mutual": 6, "reason": "Same stream"},
            {"name": "Meera Nair", "id": "MES20240031", "stream": "Commerce", "mutual": 4, "reason": "Same class"},
            {"name": "Rahul Verma", "id": "MES20240032", "stream": "Arts", "mutual": 8, "reason": "Mutual friends"}
        ]
        
        for suggestion in suggestions:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{suggestion['name']}**")
                st.caption(f"ID: {suggestion['id']} • {suggestion['stream']}")
                st.caption(f"👥 {suggestion['mutual']} mutual friends • {suggestion['reason']}")
            with col2:
                if st.button("Add Friend", key=f"add_{suggestion['id']}", use_container_width=True):
                    st.success(f"Friend request sent to {suggestion['name']}")
            with col3:
                if st.button("View", key=f"view_sug_{suggestion['id']}", use_container_width=True):
                    st.info(f"Viewing {suggestion['name']}'s profile")
    
    with tab4:
        st.markdown("### 🚫 Blocked Users")
        st.info("You have no blocked users.")
        
        if st.button("Manage Block List", use_container_width=True):
            st.info("Block list management")
