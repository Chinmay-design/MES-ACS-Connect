import streamlit as st

def alumni_groups_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">👥 Alumni Groups</h1>', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["👥 My Groups", "🔍 Discover Groups", "➕ Create Alumni Group"])
    
    with tab1:
        st.markdown("### My Alumni Groups")
        
        alumni_groups = [
            {"name": "Tech Alumni Network", "members": 45, "category": "Professional", 
             "role": "Member", "activity": "High", "description": "For tech professionals"},
            {"name": "Entrepreneurs Forum", "members": 28, "category": "Business", 
             "role": "Admin", "activity": "Medium", "description": "Startup discussions"},
            {"name": "Mentorship Circle", "members": 32, "category": "Support", 
             "role": "Moderator", "activity": "High", "description": "Mentorship program"},
            {"name": "Batch 2020 Reunion", "members": 65, "category": "Social", 
             "role": "Member", "activity": "Low", "description": "2020 batch alumni"}
        ]
        
        for group in alumni_groups:
            with st.expander(f"{group['name']} ({group['role']})"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Category:** {group['category']}")
                    st.write(f"**Members:** {group['members']} alumni")
                    st.write(f"**Activity:** {group['activity']}")
                    st.write(f"**Description:** {group['description']}")
                with col2:
                    if st.button("💬 Chat", key=f"achat_{group['name']}", use_container_width=True):
                        st.info(f"Opening {group['name']} chat")
    
    with tab2:
        st.markdown("### Discover Alumni Groups")
        
        groups = [
            {"name": "Global Alumni Network", "members": 245, "category": "Professional", 
             "privacy": "Public", "description": "Worldwide alumni connections"},
            {"name": "Industry Leaders", "members": 89, "category": "Professional", 
             "privacy": "Private", "description": "C-level executives network"},
            {"name": "Women in Tech", "members": 56, "category": "Support", 
             "privacy": "Public", "description": "Supporting women in technology"},
            {"name": "Philanthropy Circle", "members": 42, "category": "Charity", 
             "privacy": "Public", "description": "Alumni giving back"}
        ]
        
        for group in groups:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{group['name']}**")
                st.caption(f"{group['category']} • {group['members']} members")
                st.caption(group['description'])
            with col2:
                if st.button("Join", key=f"ajoin_{group['name']}", use_container_width=True):
                    st.success(f"Request to join {group['name']} sent!")
    
    with tab3:
        st.markdown("### Create Alumni Group")
        
        with st.form("create_alumni_group"):
            group_name = st.text_input("Group Name *", placeholder="Alumni Group Name")
            description = st.text_area("Description *", height=100, 
                                     placeholder="Purpose of this alumni group...")
            
            col1, col2 = st.columns(2)
            with col1:
                category = st.selectbox("Category *", 
                                      ["Professional", "Social", "Business", "Support", "Charity", "Other"])
                group_type = st.selectbox("Group Type *", 
                                        ["Alumni Only", "Alumni + Students", "Open Network"])
            with col2:
                privacy = st.selectbox("Privacy *", 
                                     ["Public", "Private", "Restricted"])
                target_batch = st.multiselect("Target Batch Years", 
                                            ["2015-2020", "2021-2023", "2024+", "All"])
            
            if st.form_submit_button("Create Alumni Group", use_container_width=True):
                if group_name and description:
                    st.success(f"Alumni group '{group_name}' created!")
                    st.info("Share with fellow alumni to grow your network")
