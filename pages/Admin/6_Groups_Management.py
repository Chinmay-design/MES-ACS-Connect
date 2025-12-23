import streamlit as st

def admin_groups_management_page():
    st.markdown('<h1 class="main-header">👥 Groups Management</h1>', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📋 All Groups", "⚠️ Reported Groups", "📊 Group Analytics"])
    
    with tab1:
        st.markdown("### All Groups")
        
        # Group type filter
        group_type = st.selectbox("Filter by Type", ["All", "Student Groups", "Alumni Groups", "Mixed Groups"])
        
        # Groups data
        groups = [
            {"id": 1, "name": "Science Study Group", "type": "Student", "members": 24, 
             "category": "Academic", "created_by": "John Doe", "status": "Active", "created": "2024-01-10"},
            {"id": 2, "name": "Tech Alumni Network", "type": "Alumni", "members": 45, 
             "category": "Professional", "created_by": "Dr. Robert Brown", "status": "Active", "created": "2024-01-05"},
            {"id": 3, "name": "Entrepreneurs Forum", "type": "Mixed", "members": 28, 
             "category": "Business", "created_by": "Lisa Taylor", "status": "Pending", "created": "2024-01-15"},
            {"id": 4, "name": "Music Club", "type": "Student", "members": 32, 
             "category": "Arts", "created_by": "Emma Wilson", "status": "Active", "created": "2024-01-08"},
            {"id": 5, "name": "Debate Society", "type": "Student", "members": 28, 
             "category": "Academic", "created_by": "Mike Chen", "status": "Suspended", "created": "2024-01-12"}
        ]
        
        # Apply filter
        if group_type != "All":
            type_map = {
                "Student Groups": "Student",
                "Alumni Groups": "Alumni", 
                "Mixed Groups": "Mixed"
            }
            groups = [g for g in groups if g['type'] == type_map[group_type]]
        
        # Display groups
        for group in groups:
            with st.expander(f"{group['name']} ({group['type']} Group)"):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**Category:** {group['category']}")
                    st.write(f"**Members:** {group['members']}")
                    st.write(f"**Created by:** {group['created_by']}")
                    st.write(f"**Created:** {group['created']}")
                    st.write(f"**Status:** {group['status']}")
                with col2:
                    if st.button("👀 View", key=f"view_grp_{group['id']}", use_container_width=True):
                        st.info(f"Viewing {group['name']} details")
                with col3:
                    if group['status'] == 'Active':
                        if st.button("⚠️ Suspend", key=f"sus_{group['id']}", use_container_width=True):
                            st.warning(f"Suspended {group['name']}")
                    elif group['status'] == 'Suspended':
                        if st.button("✅ Activate", key=f"act_{group['id']}", use_container_width=True):
                            st.success(f"Activated {group['name']}")
                    elif group['status'] == 'Pending':
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button("✅", key=f"app_grp_{group['id']}"):
                                st.success(f"Approved {group['name']}")
                        with col_b:
                            if st.button("❌", key=f"rej_grp_{group['id']}"):
                                st.error(f"Rejected {group['name']}")
    
    with tab2:
        st.markdown("### ⚠️ Reported Groups")
        st.info("No groups have been reported recently.")
        
        if st.button("View Report History", use_container_width=True):
            st.info("Report history would show here")
    
    with tab3:
        st.markdown("### 📊 Group Analytics")
        
        # Statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Groups", "48", "+2")
        with col2:
            st.metric("Active Groups", "42", "+1")
        with col3:
            st.metric("Total Members", "1,245", "+35")
        
        # Group type distribution
        st.markdown("#### 📈 Group Type Distribution")
        
        type_data = {
            "Student Groups": 28,
            "Alumni Groups": 12,
            "Mixed Groups": 8
        }
        
        for gtype, count in type_data.items():
            st.write(f"**{gtype}:** {count} groups")
            st.progress(count / 48)
        
        # Most active groups
        st.markdown("#### 🏆 Most Active Groups")
        
        active_groups = [
            {"name": "Science Study Group", "activity": "High", "new_members": "5"},
            {"name": "Tech Alumni Network", "activity": "High", "new_members": "8"},
            {"name": "Coding Club", "activity": "Medium", "new_members": "3"}
        ]
        
        for group in active_groups:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(group['name'])
            with col2:
                st.write(f"**{group['activity']}**")
            with col3:
                st.write(f"+{group['new_members']}")
