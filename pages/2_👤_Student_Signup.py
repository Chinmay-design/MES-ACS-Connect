import streamlit as st
from utils.database import db
import re
from datetime import datetime

def student_signup_page():
    st.markdown('<h1 class="main-header">Student Registration</h1>', unsafe_allow_html=True)
    
    with st.form("signup_form"):
        # Personal Information
        st.markdown("### 👤 Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name *", placeholder="John")
            date_of_birth = st.date_input("Date of Birth *", 
                                         max_value=datetime.today(),
                                         value=datetime(2005, 1, 1))
            email = st.text_input("Email Address *", placeholder="student@mes.edu")
        
        with col2:
            last_name = st.text_input("Last Name *", placeholder="Doe")
            id_card_number = st.text_input("ID Card Number *", placeholder="MES20240001")
            contact_number = st.text_input("Contact Number *", placeholder="9876543210")
        
        # Academic Information
        st.markdown("### 🎓 Academic Information")
        col1, col2, col3 = st.columns(3)
        with col1:
            year = st.selectbox("Year *", ["1st Year PUC", "2nd Year PUC"])
        with col2:
            stream = st.selectbox("Stream *", ["Science", "Commerce", "Arts"])
        with col3:
            section = st.selectbox("Section", ["A", "B", "C", "D", "Not Assigned"])
        
        # Account Information
        st.markdown("### 🔐 Account Information")
        col1, col2 = st.columns(2)
        with col1:
            login_id = st.text_input("Login ID *", placeholder="john_doe2024")
            password = st.text_input("Password *", type="password", 
                                   help="Must contain: 8+ chars, uppercase, lowercase, number, special character")
        with col2:
            confirm_password = st.text_input("Confirm Password *", type="password")
        
        # Security Question
        st.markdown("### 🔒 Security Question (For password recovery)")
        security_question = st.selectbox(
            "Select a security question *",
            [
                "What is your mother's maiden name?",
                "What was your first pet's name?",
                "What elementary school did you attend?",
                "What city were you born in?",
                "What is your favorite book?",
                "What was your childhood nickname?"
            ]
        )
        security_answer = st.text_input("Your answer *", type="password")
        
        # Hobbies & Interests
        st.markdown("### 🎨 Additional Information")
        hobbies = st.text_area("Hobbies & Interests *", 
                              placeholder="Describe your hobbies, interests, and extracurricular activities...",
                              height=100)
        
        # Submit button
        if st.form_submit_button("🎯 Create Account", use_container_width=True):
            # Validation
            errors = []
            
            # Required fields
            required_fields = {
                "First Name": first_name,
                "Last Name": last_name,
                "Email": email,
                "ID Card Number": id_card_number,
                "Contact Number": contact_number,
                "Login ID": login_id,
                "Password": password,
                "Security Answer": security_answer,
                "Hobbies": hobbies
            }
            
            for field, value in required_fields.items():
                if not value or not str(value).strip():
                    errors.append(f"{field} is required")
            
            # Password validation
            if password != confirm_password:
                errors.append("Passwords do not match")
            
            if len(password) < 8:
                errors.append("Password must be at least 8 characters")
            
            if not re.search(r"[A-Z]", password):
                errors.append("Password must contain at least one uppercase letter")
            
            if not re.search(r"[a-z]", password):
                errors.append("Password must contain at least one lowercase letter")
            
            if not re.search(r"\d", password):
                errors.append("Password must contain at least one number")
            
            if not re.search(r"[@$!%*?&]", password):
                errors.append("Password must contain at least one special character (@$!%*?&)")
            
            # Email validation
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                errors.append("Invalid email format")
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Prepare user data
                user_data = {
                    'login_id': login_id,
                    'email': email,
                    'password': password,
                    'first_name': first_name,
                    'last_name': last_name,
                    'role': 'student',
                    'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
                    'id_card_number': id_card_number,
                    'year': year,
                    'stream': stream,
                    'section': section,
                    'contact_number': contact_number,
                    'security_question': security_question,
                    'security_answer': security_answer,
                    'hobbies': hobbies,
                    'status': 'pending'
                }
                
                # Create user
                user_id = db.create_user(user_data)
                
                if user_id:
                    st.success("""
                    🎉 **Registration Successful!** 
                    
                    Your account has been created and is pending verification by the administration.
                    You will receive an email once your account is approved.
                    """)
                    
                    # Show success message
                    st.markdown("""
                    <div class="success-box">
                    <strong>Next Steps:</strong><br>
                    1. Wait for admin approval (usually 24-48 hours)<br>
                    2. Check your email for verification<br>
                    3. Login with your credentials once approved
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Option to go back to login
                    if st.button("← Back to Login", use_container_width=True):
                        st.session_state.page = "Login"
                        st.rerun()
                else:
                    st.error("Registration failed. Login ID or Email might already be registered.")
    
    # Back button
    if st.button("← Back to Login", key="back_button"):
        st.session_state.page = "Login"
        st.rerun()
