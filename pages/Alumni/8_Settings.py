import streamlit as st

def alumni_settings_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">⚙️ Alumni Settings</h1>', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["👤 Profile", "🔒 Privacy", "💼 Professional"])
    
    with tab1:
        st.markdown("### Alumni Profile Settings")
        
        with st.form("alumni_profile_settings"):
            col1, col2 = st.columns(2)
            with col1:
                company = st.text_input("Current Company", value=user.get('current_company', ''))
                position = st.text_input("Position", value=user.get('position', ''))
            with col2:
                linkedin = st.text_input("LinkedIn URL", value=user.get('linkedin_url', ''))
                website = st.text_input("Website/Portfolio")
            
            graduation_year = st.number_input("Graduation Year", 
                                            min_value=2000, 
                                            max_value=2024,
                                            value=int(user.get('graduation_year', 2020)))
            
            bio = st.text_area("Professional Bio", 
                             placeholder="Share your career journey, expertise, and interests...",
                             height=100)
            
            if st.form_submit_button("💾 Save Profile", use_container_width=True):
                st.success("Alumni profile updated!")
    
    with tab2:
        st.markdown("### Privacy Settings")
        
        # Visibility settings
        st.markdown("#### 👤 Profile Visibility")
        visibility = st.selectbox(
            "Who can see your alumni profile?",
            ["All Alumni", "Connections Only", "Only Me", "Students & Alumni"]
        )
        
        # Contact preferences
        st.markdown("#### 📞 Contact Preferences")
        col1, col2 = st.columns(2)
        with col1:
            allow_messages = st.checkbox("Allow messages from alumni", value=True)
            allow_mentoring = st.checkbox("Open to mentoring requests", value=True)
        with col2:
            show_contact = st.checkbox("Show contact information", value=False)
            show_salary = st.checkbox("Show salary range", value=False)
        
        # Data sharing
        st.markdown("#### 🔄 Data Sharing")
        share_stats = st.checkbox("Share anonymous usage statistics", value=True)
        share_research = st.checkbox("Participate in alumni research", value=False)
        
        if st.button("💾 Save Privacy", use_container_width=True):
            st.success("Privacy settings updated!")
    
    with tab3:
        st.markdown("### Professional Settings")
        
        # Availability for opportunities
        st.markdown("#### 💼 Opportunity Preferences")
        
        looking_for = st.multiselect(
            "Looking for",
            ["Mentoring Opportunities", "Collaboration Projects", "Job Opportunities", 
             "Speaking Engagements", "Advisory Roles", "Investment Opportunities"]
        )
        
        # Expertise areas
        st.markdown("#### 🛠️ Expertise Areas")
        
        expertise = st.multiselect(
            "Your expertise areas",
            ["Leadership", "Technology", "Finance", "Marketing", "Operations", 
             "Product Management", "Data Science", "Entrepreneurship"]
        )
        
        # Availability
        st.markdown("#### ⏰ Availability")
        
        availability = st.select_slider(
            "Time available for alumni activities",
            options=["Limited", "Moderate", "Generous", "Very Available"]
        )
        
        hours_per_month = st.slider("Hours per month available", 1, 40, 5)
        
        if st.button("💾 Save Professional", use_container_width=True):
            st.success("Professional settings updated!")
