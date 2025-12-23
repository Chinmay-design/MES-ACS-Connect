import streamlit as st

def student_settings_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">⚙️ Settings</h1>', unsafe_allow_html=True)
    
    # Tabs for different settings
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Account", "🔒 Privacy", "🔔 Notifications", "🛠️ Advanced"])
    
    with tab1:
        st.markdown("### Account Settings")
        
        with st.form("account_settings"):
            # Personal Information
            st.markdown("#### Personal Information")
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name", value=user.get('first_name', ''))
                email = st.text_input("Email", value=user.get('email', ''))
            with col2:
                last_name = st.text_input("Last Name", value=user.get('last_name', ''))
                contact = st.text_input("Contact Number", value=user.get('contact_number', ''))
            
            # Academic Information
            st.markdown("#### Academic Information")
            col1, col2, col3 = st.columns(3)
            with col1:
                year = st.selectbox("Year", ["1st Year PUC", "2nd Year PUC"], 
                                  index=0 if user.get('year') == "1st Year PUC" else 1)
            with col2:
                stream = st.selectbox("Stream", ["Science", "Commerce", "Arts"], 
                                    index=["Science", "Commerce", "Arts"].index(user.get('stream', 'Science')))
            with col3:
                section = st.selectbox("Section", ["A", "B", "C", "D"], 
                                     index=["A", "B", "C", "D"].index(user.get('section', 'A')))
            
            # Bio and Hobbies
            bio = st.text_area("Bio", placeholder="Tell others about yourself...", height=100)
            hobbies = st.text_area("Hobbies & Interests", value=user.get('hobbies', ''), height=100)
            
            if st.form_submit_button("💾 Save Changes", use_container_width=True):
                st.success("Account settings updated!")
    
    with tab2:
        st.markdown("### Privacy Settings")
        
        # Profile visibility
        st.markdown("#### 👤 Profile Visibility")
        profile_visibility = st.selectbox(
            "Who can see your profile?",
            ["Everyone", "Friends Only", "Only Me"]
        )
        
        # Search visibility
        st.markdown("#### 🔍 Search Visibility")
        col1, col2 = st.columns(2)
        with col1:
            show_in_search = st.checkbox("Show in search results", value=True)
            show_email = st.checkbox("Show email to others", value=False)
        with col2:
            show_contact = st.checkbox("Show contact number", value=False)
            show_year_stream = st.checkbox("Show year & stream", value=True)
        
        # Connection settings
        st.markdown("#### 🤝 Connection Settings")
        connection_settings = {
            "friend_requests": st.selectbox("Who can send friend requests?", 
                                          ["Everyone", "Friends of Friends", "No One"]),
            "message_requests": st.selectbox("Who can message you?", 
                                           ["Friends Only", "Everyone", "No One"]),
            "auto_add_friends": st.checkbox("Auto-accept friend requests from classmates", value=True)
        }
        
        # Blocked users
        st.markdown("#### 🚫 Blocked Users")
        st.info("You have no blocked users.")
        if st.button("Manage Blocked Users", use_container_width=True):
            st.info("Block list management")
        
        if st.button("💾 Save Privacy Settings", use_container_width=True):
            st.success("Privacy settings updated!")
    
    with tab3:
        st.markdown("### Notification Settings")
        
        # Notification channels
        st.markdown("#### 📱 Notification Channels")
        col1, col2, col3 = st.columns(3)
        with col1:
            email_notifications = st.checkbox("Email", value=True)
            push_notifications = st.checkbox("Push", value=True)
        with col2:
            sms_notifications = st.checkbox("SMS", value=False)
            in_app_notifications = st.checkbox("In-App", value=True)
        
        # Notification types
        st.markdown("#### 🔔 Notification Types")
        
        notification_types = {
            "Friend Requests": st.checkbox("Friend requests", value=True),
            "Messages": st.checkbox("New messages", value=True),
            "Group Invites": st.checkbox("Group invitations", value=True),
            "Event Reminders": st.checkbox("Event reminders", value=True),
            "Announcements": st.checkbox("Important announcements", value=True),
            "Confession Comments": st.checkbox("Comments on your confessions", value=True),
            "Study Group Updates": st.checkbox("Study group updates", value=True),
            "Academic Notices": st.checkbox("Academic notices", value=True)
        }
        
        # Notification frequency
        st.markdown("#### ⏰ Notification Frequency")
        frequency = st.select_slider(
            "How often should we notify you?",
            options=["Never", "Only Important", "Normal", "Frequent", "Real-time"]
        )
        
        # Quiet hours
        st.markdown("#### 🌙 Quiet Hours")
        quiet_hours = st.checkbox("Enable quiet hours", value=False)
        if quiet_hours:
            col1, col2 = st.columns(2)
            with col1:
                start_time = st.time_input("Start time", value=datetime.strptime("22:00", "%H:%M").time())
            with col2:
                end_time = st.time_input("End time", value=datetime.strptime("07:00", "%H:%M").time())
        
        if st.button("💾 Save Notification Settings", use_container_width=True):
            st.success("Notification settings updated!")
    
    with tab4:
        st.markdown("### Advanced Settings")
        
        # Security
        st.markdown("#### 🔒 Security")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Change Password", use_container_width=True):
                with st.expander("Change Password"):
                    current_pass = st.text_input("Current Password", type="password")
                    new_pass = st.text_input("New Password", type="password")
                    confirm_pass = st.text_input("Confirm New Password", type="password")
                    
                    if st.button("Update Password"):
                        if new_pass == confirm_pass:
                            st.success("Password updated successfully!")
                        else:
                            st.error("Passwords don't match")
        
        with col2:
            if st.button("Update Security Question", use_container_width=True):
                st.info("Security question update")
        
        # Account management
        st.markdown("#### 🛠️ Account Management")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Download My Data", use_container_width=True):
                st.info("Your data will be prepared for download")
        
        with col2:
            if st.button("Deactivate Account", use_container_width=True, type="secondary"):
                st.warning("Are you sure you want to deactivate your account?")
                if st.button("Yes, Deactivate", type="primary"):
                    st.error("Account deactivated")
        
        # App settings
        st.markdown("#### 📱 App Settings")
        
        theme = st.selectbox("Theme", ["Light", "Dark", "System Default"])
        language = st.selectbox("Language", ["English", "हिन्दी", "മലയാളം", "தமிழ்"])
        
        # Data and storage
        st.markdown("#### 💾 Data & Storage")
        
        cache_size = st.slider("Cache Size (MB)", 50, 500, 100)
        auto_clear_cache = st.checkbox("Auto-clear cache weekly", value=True)
        
        if st.button("Clear Cache Now", use_container_width=True):
            st.success("Cache cleared!")
        
        # About
        st.markdown("#### ℹ️ About")
        st.info("""
        **MES Connect v1.0.0**  
        Developed for MES Educational Institutions  
        © 2024 MES Connect. All rights reserved.
        
        For support: support@mesconnect.edu  
        For feedback: feedback@mesconnect.edu
        """)
        
        if st.button("Check for Updates", use_container_width=True):
            st.success("You have the latest version!")
