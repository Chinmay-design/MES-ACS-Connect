import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MES Connect",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #374151;
        margin-bottom: 1rem;
    }
    .card {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #3B82F6;
    }
    .success-box {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'page' not in st.session_state:
    st.session_state.page = "Login"
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = "expanded"

def main():
    # If not authenticated, show login/signup
    if not st.session_state.authenticated:
        if st.session_state.page == "Login":
            from pages._1_🏠_Login import login_page
            login_page()
        elif st.session_state.page == "Student_Signup":
            from pages._2_👤_Student_Signup import student_signup_page
            student_signup_page()
        else:
            from pages._1_🏠_Login import login_page
            login_page()
    else:
        # User is authenticated, show role-specific navigation
        user = st.session_state.user
        
        # Sidebar navigation
        with st.sidebar:
            st.image("https://via.placeholder.com/150x50/3B82F6/FFFFFF?text=MES+Connect", 
                    use_column_width=True)
            
            st.markdown(f"### 👤 {user['first_name']} {user['last_name']}")
            st.markdown(f"**Role:** {user['role'].title()}")
            
            if user['role'] == 'student':
                st.markdown(f"**Year:** {user.get('year', 'N/A')}")
                st.markdown(f"**Stream:** {user.get('stream', 'N/A')}")
            elif user['role'] == 'alumni':
                st.markdown(f"**Graduation:** {user.get('graduation_year', 'N/A')}")
            
            st.markdown("---")
            
            # Navigation based on role
            if user['role'] == 'student':
                pages = {
                    "🏠 Dashboard": "Student/1_Dashboard",
                    "👤 Profile": "Student/2_Profile",
                    "👥 Friends": "Student/3_Friends",
                    "💬 Chat": "Student/4_Chat",
                    "👥 Groups": "Student/5_Groups",
                    "🤫 Confessions": "Student/6_Confessions",
                    "📅 Events": "Student/7_Events",
                    "⚙️ Settings": "Student/8_Settings"
                }
            elif user['role'] == 'alumni':
                pages = {
                    "🏠 Dashboard": "Alumni/1_Dashboard",
                    "👤 Profile": "Alumni/2_Profile",
                    "🤝 Networking": "Alumni/3_Networking",
                    "💬 Chat": "Alumni/4_Chat",
                    "👥 Groups": "Alumni/5_Groups",
                    "📅 Events": "Alumni/6_Events",
                    "💰 Contributions": "Alumni/7_Contributions",
                    "⚙️ Settings": "Alumni/8_Settings"
                }
            else:  # admin
                pages = {
                    "📊 Dashboard": "Admin/1_Dashboard",
                    "👨‍🎓 Student Management": "Admin/2_Student_Management",
                    "👨‍🎓 Alumni Management": "Admin/3_Alumni_Management",
                    "📢 Announcements": "Admin/4_Announcements",
                    "🤫 Confession Moderation": "Admin/5_Confession_Moderation",
                    "👥 Groups Management": "Admin/6_Groups_Management",
                    "📈 Analytics": "Admin/7_Analytics"
                }
            
            selected_page = st.selectbox("Navigation", list(pages.keys()))
            st.session_state.page = pages[selected_page]
            
            st.markdown("---")
            
            # Quick actions
            if user['role'] == 'student':
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🤫 Post", use_container_width=True):
                        st.session_state.page = "Student/6_Confessions"
                        st.rerun()
                with col2:
                    if st.button("👥 Create", use_container_width=True):
                        st.session_state.page = "Student/5_Groups"
                        st.rerun()
            
            elif user['role'] == 'alumni':
                if st.button("🤝 Connect", use_container_width=True):
                    st.session_state.page = "Alumni/3_Networking"
                    st.rerun()
            
            elif user['role'] == 'admin':
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📢 Post", use_container_width=True):
                        st.session_state.page = "Admin/4_Announcements"
                        st.rerun()
                with col2:
                    if st.button("👨‍🎓 Promote", use_container_width=True):
                        st.session_state.page = "Admin/2_Student_Management"
                        st.rerun()
            
            st.markdown("---")
            
            # Logout button
            if st.button("🚪 Logout", type="secondary", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.user = None
                st.session_state.page = "Login"
                st.rerun()
        
        # Load the selected page
        try:
            if "Student/" in st.session_state.page:
                if "1_Dashboard" in st.session_state.page:
                    from pages.Student._1_Dashboard import student_dashboard_page
                    student_dashboard_page()
                elif "2_Profile" in st.session_state.page:
                    from pages.Student._2_Profile import student_profile_page
                    student_profile_page()
                elif "3_Friends" in st.session_state.page:
                    from pages.Student._3_Friends import student_friends_page
                    student_friends_page()
                elif "4_Chat" in st.session_state.page:
                    from pages.Student._4_Chat import student_chat_page
                    student_chat_page()
                elif "5_Groups" in st.session_state.page:
                    from pages.Student._5_Groups import student_groups_page
                    student_groups_page()
                elif "6_Confessions" in st.session_state.page:
                    from pages.Student._6_Confessions import student_confessions_page
                    student_confessions_page()
                elif "7_Events" in st.session_state.page:
                    from pages.Student._7_Events import student_events_page
                    student_events_page()
                elif "8_Settings" in st.session_state.page:
                    from pages.Student._8_Settings import student_settings_page
                    student_settings_page()
            
            elif "Alumni/" in st.session_state.page:
                if "1_Dashboard" in st.session_state.page:
                    from pages.Alumni._1_Dashboard import alumni_dashboard_page
                    alumni_dashboard_page()
                elif "2_Profile" in st.session_state.page:
                    from pages.Alumni._2_Profile import alumni_profile_page
                    alumni_profile_page()
                elif "3_Networking" in st.session_state.page:
                    from pages.Alumni._3_Networking import alumni_networking_page
                    alumni_networking_page()
                elif "4_Chat" in st.session_state.page:
                    from pages.Alumni._4_Chat import alumni_chat_page
                    alumni_chat_page()
                elif "5_Groups" in st.session_state.page:
                    from pages.Alumni._5_Groups import alumni_groups_page
                    alumni_groups_page()
                elif "6_Events" in st.session_state.page:
                    from pages.Alumni._6_Events import alumni_events_page
                    alumni_events_page()
                elif "7_Contributions" in st.session_state.page:
                    from pages.Alumni._7_Contributions import alumni_contributions_page
                    alumni_contributions_page()
                elif "8_Settings" in st.session_state.page:
                    from pages.Alumni._8_Settings import alumni_settings_page
                    alumni_settings_page()
            
            elif "Admin/" in st.session_state.page:
                if "1_Dashboard" in st.session_state.page:
                    from pages.Admin._1_Dashboard import admin_dashboard_page
                    admin_dashboard_page()
                elif "2_Student_Management" in st.session_state.page:
                    from pages.Admin._2_Student_Management import admin_student_management_page
                    admin_student_management_page()
                elif "3_Alumni_Management" in st.session_state.page:
                    from pages.Admin._3_Alumni_Management import admin_alumni_management_page
                    admin_alumni_management_page()
                elif "4_Announcements" in st.session_state.page:
                    from pages.Admin._4_Announcements import admin_announcements_page
                    admin_announcements_page()
                elif "5_Confession_Moderation" in st.session_state.page:
                    from pages.Admin._5_Confession_Moderation import admin_confession_moderation_page
                    admin_confession_moderation_page()
                elif "6_Groups_Management" in st.session_state.page:
                    from pages.Admin._6_Groups_Management import admin_groups_management_page
                    admin_groups_management_page()
                elif "7_Analytics" in st.session_state.page:
                    from pages.Admin._7_Analytics import admin_analytics_page
                    admin_analytics_page()
        
        except Exception as e:
            st.error(f"Error loading page: {str(e)}")
            st.info("Returning to dashboard...")
            st.session_state.page = f"{user['role'].title()}/1_Dashboard"
            st.rerun()

if __name__ == "__main__":
    main()
