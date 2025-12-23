import streamlit as st

def alumni_contributions_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">💰 Alumni Contributions</h1>', unsafe_allow_html=True)
    
    # Contribution stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Donated", "$2,500")
    with col2:
        st.metric("This Year", "$500")
    with col3:
        st.metric("Students Helped", "12")
    with col4:
        st.metric("Recurring", "Yes")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["💸 Make Contribution", "📋 Contribution History", "🎯 Impact Report"])
    
    with tab1:
        st.markdown("### Support Your Alma Mater")
        
        with st.form("contribution_form"):
            # Contribution type
            contribution_type = st.selectbox(
                "Contribution Type *",
                ["Scholarship Fund", "Infrastructure Development", "Library Enhancement", 
                 "Sports Facilities", "Computer Lab", "Research Grant", "General Fund"]
            )
            
            # Amount
            col1, col2 = st.columns(2)
            with col1:
                amount = st.number_input("Amount ($) *", min_value=10, value=100, step=10)
            with col2:
                preset_amounts = st.selectbox("Quick Select", [50, 100, 250, 500, 1000, 5000])
                if preset_amounts:
                    amount = preset_amounts
            
            # Payment options
            st.markdown("#### 💳 Payment Options")
            payment_method = st.radio(
                "Select payment method",
                ["Credit/Debit Card", "Net Banking", "UPI", "Bank Transfer"]
            )
            
            # Additional options
            col1, col2 = st.columns(2)
            with col1:
                recurring = st.checkbox("Make this recurring (Monthly)")
                anonymous = st.checkbox("Donate anonymously")
            with col2:
                if recurring:
                    duration = st.selectbox("Duration", ["3 months", "6 months", "1 year", "Ongoing"])
                dedication = st.text_input("Dedication (Optional)", placeholder="In memory of...")
            
            # Tax benefits
            st.info("""
            💡 **Tax Benefits:**  
            • 80G tax exemption available  
            • Receipt will be emailed within 24 hours  
            • Valid for income tax deduction
            """)
            
            if st.form_submit_button("🤝 Donate Now", use_container_width=True):
                st.success(f"Thank you for your ${amount} contribution to {contribution_type}!")
                st.balloons()
                st.info("Receipt will be emailed to you shortly.")
    
    with tab2:
        st.markdown("### Contribution History")
        
        history = [
            {"date": "2024-01-15", "amount": "$500", "type": "Scholarship", "status": "Completed", "receipt": "RCT20240115001"},
            {"date": "2023-11-20", "amount": "$1,000", "type": "Infrastructure", "status": "Completed", "receipt": "RCT20231120045"},
            {"date": "2023-08-05", "amount": "$1,000", "type": "General Fund", "status": "Completed", "receipt": "RCT20230805012"}
        ]
        
        for contrib in history:
            with st.expander(f"{contrib['date']} - {contrib['amount']} ({contrib['type']})"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Receipt:** {contrib['receipt']}")
                    st.write(f"**Status:** {contrib['status']}")
                with col2:
                    if st.button("📄 View Receipt", key=f"receipt_{contrib['receipt']}"):
                        st.info(f"Showing receipt {contrib['receipt']}")
                with col3:
                    if st.button("🔄 Repeat Donation", key=f"repeat_{contrib['receipt']}"):
                        st.success(f"Repeating {contrib['amount']} donation")
    
    with tab3:
        st.markdown("### 📊 Your Impact Report")
        
        st.markdown("""
        #### 🎓 Students Supported
        Your contributions have directly helped **12 students** continue their education through scholarships.
        
        #### 🏫 Infrastructure Developed
        Your donations contributed to:
        - New computer lab with 30 systems
        - Library book acquisition (50+ new books)
        - Sports equipment upgrade
        
        #### 📈 Overall Impact
        - **$2,500** total contribution
        - **3 years** of consistent support
        - **45+** alumni contributed alongside you
        
        #### 🏆 Recognition Level
        **Silver Donor** - Thank you for your continued support!
        """)
        
        if st.button("Download Impact Report", use_container_width=True):
            st.success("Impact report downloaded!")
