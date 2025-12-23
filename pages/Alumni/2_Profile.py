import streamlit as st

def alumni_profile_page():
    user = st.session_state.user
    
    st.markdown(f'<h1 class="main-header">Alumni Profile</h1>', unsafe_allow_html=True)
    
    # Profile header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {user['first_name']} {user['last_name']}")
        st.markdown(f"**Batch:** {user.get('graduation_year', 'N/A')} • **Role:** {user.get('position', 'Alumni')} at {user.get('current_company', 'N/A')}")
    with col2:
        if st.button("✏️ Edit Profile", use_container_width=True):
            st.session_state.editing = True
    
    st.markdown("---")
    
    # Two-column layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Profile picture
        st.markdown("### Profile")
        st.image("https://via.placeholder.com/200x200/3B82F6/FFFFFF?text=Alumni", 
                width=200, caption="Alumni Profile")
        
        uploaded_file = st.file_uploader("Update photo", type=['jpg', 'png', 'jpeg'])
        if uploaded_file:
            st.success("Photo updated!")
        
        # Professional stats
        st.markdown("### 📊 Professional Stats")
        
        stats = {
            "Connections": "156",
            "Mentees": "3",
            "Contributions": "$2,500",
            "Events Attended": "12"
        }
        
        for key, value in stats.items():
            st.write(f"**{key}:** {value}")
        
        # Alumni badge
        st.markdown("### 🎓 Alumni Badge")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                    color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 1.2rem; font-weight: bold;">Class of {user.get('graduation_year', 'Alumni')}</div>
            <div style="font-size: 1rem;">Alumni Member</div>
            <div style="font-size: 0.9rem;">Since {user.get('created_at', '2024')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Professional Information
        st.markdown("### 💼 Professional Information")
        
        info_col1, info_col2 = st.columns(2)
        with info_col1:
            st.info(f"**Current Company:** {user.get('current_company', 'Not specified')}")
            st.info(f"**Position:** {user.get('position', 'Not specified')}")
            st.info(f"**Email:** {user.get('email', 'N/A')}")
        
        with info_col2:
            st.info(f"**LinkedIn:** {user.get('linkedin_url', 'Not linked')}")
            st.info(f"**Contact:** {user.get('contact_number', 'N/A')}")
            st.info(f"**Graduation Year:** {user.get('graduation_year', 'N/A')}")
        
        # Academic Background
        st.markdown("### 🎓 Academic Background")
        
        academic_info = {
            "Stream": user.get('stream', 'N/A'),
            "Year of Passing": user.get('graduation_year', 'N/A'),
            "Student ID": user.get('id_card_number', 'N/A'),
            "Promoted By": user.get('promoted_by', 'System')
        }
        
        for key, value in academic_info.items():
            st.write(f"**{key}:** {value}")
        
        # Skills & Expertise
        st.markdown("### 🛠️ Skills & Expertise")
        
        skills = ["Leadership", "Project Management", "Technical Skills", "Mentoring", "Public Speaking"]
        
        for skill in skills:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(skill)
            with col_b:
                level = st.select_slider("", ["Beginner", "Intermediate", "Advanced", "Expert"], 
                                       key=f"skill_{skill}", label_visibility="collapsed")
        
        # Availability for Mentorship
        st.markdown("### 👨‍🏫 Mentorship Availability")
        
        availability = st.selectbox(
            "Available for mentoring",
            ["Available", "Limited Availability", "Not Currently Available", "By Request Only"]
        )
        
        areas = st.multiselect(
            "Mentorship Areas",
            ["Career Guidance", "Technical Skills", "Interview Prep", "Resume Review", 
             "Startup Advice", "Industry Insights", "Academic Guidance"]
        )
        
        # Edit form
        if hasattr(st.session_state, 'editing') and st.session_state.editing:
            st.markdown("### ✏️ Edit Professional Profile")
            
            with st.form("edit_alumni_profile"):
                edit_col1, edit_col2 = st.columns(2)
                with edit_col1:
                    new_company = st.text_input("Company", value=user.get('current_company', ''))
                    new_position = st.text_input("Position", value=user.get('position', ''))
                    new_linkedin = st.text_input("LinkedIn URL", value=user.get('linkedin_url', ''))
                
                with edit_col2:
                    new_contact = st.text_input("Contact", value=user.get('contact_number', ''))
                    new_website = st.text_input("Website/Portfolio")
                    new_graduation = st.number_input("Graduation Year", 
                                                   min_value=2000, 
                                                   max_value=2024,
                                                   value=int(user.get('graduation_year', 2024)))
                
                bio = st.text_area("Professional Bio", 
                                 placeholder="Share your professional journey...",
                                 height=100)
                
                col_save, col_cancel = st.columns(2)
                with col_save:
                    if st.form_submit_button("💾 Save Changes", use_container_width=True):
                        st.success("Profile updated!")
                        st.session_state.editing = False
                        st.rerun()
                with col_cancel:
                    if st.form_submit_button("❌ Cancel", use_container_width=True):
                        st.session_state.editing = False
                        st.rerun()
    
    # Contribution History
    st.markdown("---")
    st.markdown("### 💰 Contribution History")
    
    contributions = [
        {"date": "2024-01-15", "amount": "$500", "type": "Scholarship", "status": "Completed"},
        {"date": "2023-11-20", "amount": "$1,000", "type": "Infrastructure", "status": "Completed"},
        {"date": "2023-08-05", "amount": "$1,000", "type": "General Fund", "status": "Completed"}
    ]
    
    for contrib in contributions:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write(contrib['date'])
        with col2:
            st.write(f"**{contrib['amount']}**")
        with col3:
            st.write(contrib['type'])
        with col4:
            st.success(contrib['status'])
