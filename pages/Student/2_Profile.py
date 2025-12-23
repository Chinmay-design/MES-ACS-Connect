import streamlit as st
from utils.database import db
from datetime import datetime

def student_profile_page():
    user = st.session_state.user
    
    st.markdown(f'<h1 class="main-header">My Profile</h1>', unsafe_allow_html=True)
    
    # Profile header with edit button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {user['first_name']} {user['last_name']}")
        st.markdown(f"**Student ID:** {user.get('id_card_number', 'Not assigned')}")
    with col2:
        if st.button("✏️ Edit Profile", use_container_width=True):
            st.session_state.editing = True
    
    st.markdown("---")
    
    # Two-column layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Profile picture section
        st.markdown("### Profile Picture")
        st.image("https://via.placeholder.com/200x200/3B82F6/FFFFFF?text=Profile", 
                width=200, caption="Your Profile Picture")
        
        uploaded_file = st.file_uploader("Upload new photo", type=['jpg', 'png', 'jpeg'])
        if uploaded_file:
            st.success("Photo uploaded successfully!")
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        
        stats_col1, stats_col2 = st.columns(2)
        with stats_col1:
            st.metric("Friends", "24")
            st.metric("Groups", "5")
        with stats_col2:
            st.metric("Posts", "42")
            st.metric("Events", "3")
        
        # Academic badge
        st.markdown("### 🎓 Academic Badge")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 1rem; border-radius: 10px; text-align: center;">
            <div style="font-size: 1.2rem; font-weight: bold;">{user.get('year', 'Student')}</div>
            <div style="font-size: 1rem;">{user.get('stream', 'Stream')}</div>
            <div style="font-size: 0.9rem;">Section {user.get('section', 'A')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Personal Information
        st.markdown("### 👤 Personal Information")
        
        info_col1, info_col2 = st.columns(2)
        with info_col1:
            st.info(f"**First Name:** {user.get('first_name', 'N/A')}")
            st.info(f"**Date of Birth:** {user.get('date_of_birth', 'N/A')}")
            st.info(f"**Email:** {user.get('email', 'N/A')}")
            st.info(f"**Student Since:** {user.get('created_at', 'N/A')}")
        
        with info_col2:
            st.info(f"**Last Name:** {user.get('last_name', 'N/A')}")
            st.info(f"**Contact:** {user.get('contact_number', 'N/A')}")
            st.info(f"**Login ID:** {user.get('login_id', 'N/A')}")
            st.info(f"**Last Login:** {user.get('last_login', 'N/A')}")
        
        # Academic Details
        st.markdown("### 🎓 Academic Details")
        
        academic_col1, academic_col2, academic_col3 = st.columns(3)
        with academic_col1:
            st.info(f"**Year:** {user.get('year', 'N/A')}")
        with academic_col2:
            st.info(f"**Stream:** {user.get('stream', 'N/A')}")
        with academic_col3:
            st.info(f"**Section:** {user.get('section', 'N/A')}")
        
        # Hobbies & Interests
        st.markdown("### 🎨 Hobbies & Interests")
        st.text_area("", value=user.get('hobbies', 'No hobbies listed'), height=100, disabled=True)
        
        # Edit form (conditional)
        if hasattr(st.session_state, 'editing') and st.session_state.editing:
            st.markdown("### ✏️ Edit Profile")
            
            with st.form("edit_profile_form"):
                edit_col1, edit_col2 = st.columns(2)
                with edit_col1:
                    new_first = st.text_input("First Name", value=user.get('first_name', ''))
                    new_email = st.text_input("Email", value=user.get('email', ''))
                    new_year = st.selectbox("Year", ["1st Year PUC", "2nd Year PUC"], 
                                          index=0 if user.get('year') == "1st Year PUC" else 1)
                
                with edit_col2:
                    new_last = st.text_input("Last Name", value=user.get('last_name', ''))
                    new_contact = st.text_input("Contact", value=user.get('contact_number', ''))
                    new_stream = st.selectbox("Stream", ["Science", "Commerce", "Arts"], 
                                            index=["Science", "Commerce", "Arts"].index(user.get('stream', 'Science')))
                
                new_hobbies = st.text_area("Hobbies & Interests", value=user.get('hobbies', ''), height=100)
                new_bio = st.text_area("Bio", placeholder="Tell us about yourself...", height=100)
                
                col_save, col_cancel = st.columns(2)
                with col_save:
                    if st.form_submit_button("💾 Save Changes", use_container_width=True):
                        st.success("Profile updated successfully!")
                        st.session_state.editing = False
                        st.rerun()
                with col_cancel:
                    if st.form_submit_button("❌ Cancel", use_container_width=True):
                        st.session_state.editing = False
                        st.rerun()
    
    # Security Section
    st.markdown("---")
    st.markdown("### 🔒 Account Security")
    
    sec_col1, sec_col2, sec_col3 = st.columns(3)
    with sec_col1:
        if st.button("Change Password", use_container_width=True):
            st.info("Password change feature")
    with sec_col2:
        if st.button("Update Security Q", use_container_width=True):
            st.info("Security question update")
    with sec_col3:
        if st.button("Privacy Settings", use_container_width=True):
            st.info("Privacy settings")
