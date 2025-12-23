import streamlit as st
from utils.database import db

def login_page():
    st.markdown('<h1 class="main-header">MES Connect</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header" style="text-align: center;">Connect, Collaborate, Grow Together</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("login_form"):
            st.markdown("### 🔐 Login to Your Account")
            
            login_id = st.text_input("Login ID or Email", placeholder="Enter your login ID or email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            role = st.selectbox("Login As", ["student", "alumni", "admin"], 
                              help="Select your account type")
            
            col_a, col_b = st.columns(2)
            with col_a:
                login_button = st.form_submit_button("🚀 Login", use_container_width=True)
            with col_b:
                forgot_button = st.form_submit_button("🔓 Forgot Password?", use_container_width=True)
            
            if login_button:
                if not login_id or not password:
                    st.error("Please enter both login ID and password")
                else:
                    with st.spinner("Authenticating..."):
                        user = db.authenticate_user(login_id, password, role)
                        if user:
                            st.session_state.authenticated = True
                            st.session_state.user = user
                            st.success(f"Welcome back, {user['first_name']}!")
                            st.rerun()
                        else:
                            st.error("Invalid credentials or account type mismatch")
            
            if forgot_button:
                st.info("Password reset feature coming soon!")
        
        st.markdown("---")
        
        # Registration option
        st.markdown("### 📝 New Student?")
        if st.button("🎓 Student Registration", use_container_width=True):
            st.session_state.page = "Student_Signup"
            st.rerun()
        
        st.markdown("""
        <div class="info-box">
        <strong>Note for Alumni & Admin:</strong><br>
        • Alumni accounts are created when students are promoted<br>
        • Admin accounts are created by system administrator<br>
        • Contact support if you need access
        </div>
        """, unsafe_allow_html=True)
