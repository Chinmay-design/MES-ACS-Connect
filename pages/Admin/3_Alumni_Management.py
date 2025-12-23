import streamlit as st
import pandas as pd

def admin_alumni_management_page():
    st.markdown('<h1 class="main-header">👨‍🎓 Alumni Management</h1>', unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📋 All Alumni", "💰 Contributions", "🎯 Engagement"])
    
    with tab1:
        st.markdown("### Alumni Directory")
        
        # Search and filters
        col1, col2, col3 = st.columns(3)
        with col1:
            search = st.text_input("Search alumni", placeholder="Name, company, or batch")
        with col2:
            batch_filter = st.selectbox("Batch Year", ["All", "2020", "2021", "2022", "2023", "2024"])
        with col3:
            status_filter = st.selectbox("Status", ["All", "Active", "Inactive", "VIP"])
        
        # Alumni data
        alumni = [
            {"id": 101, "name": "Dr. Robert Brown", "grad_year": 2020, "company": "Google", 
             "position": "Senior Engineer", "email": "robert@google.com", "status": "Active", 
             "contributions": "$5,000", "last_active": "2024-01-15"},
            {"id": 102, "name": "Lisa Taylor", "grad_year": 2021, "company": "Microsoft", 
             "position": "Product Manager", "email": "lisa@microsoft.com", "status": "Active", 
             "contributions": "$2,500", "last_active": "2024-01-10"},
            {"id": 103, "name": "David Wilson", "grad_year": 2022, "company": "Amazon", 
             "position": "Data Scientist", "email": "david@amazon.com", "status": "Active", 
             "contributions": "$1,000", "last_active": "2024-01-05"},
            {"id": 104, "name": "Priya Sharma", "grad_year": 2023, "company": "Infosys", 
             "position": "Software Developer", "email": "priya@infosys.com", "status": "Inactive", 
             "contributions": "$500", "last_active": "2023-12-01"}
        ]
        
        # Display alumni
        df = pd.DataFrame(alumni)
        st.dataframe(df[['name', 'grad_year', 'company', 'position', 'status', 'contributions', 'last_active']], 
                    use_container_width=True)
        
        # Alumni actions
        st.markdown("### 🤝 Alumni Engagement")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📧 Send Newsletter", use_container_width=True):
                st.info("Newsletter composer opened")
        with col2:
            if st.button("📅 Event Invites", use_container_width=True):
                st.info("Event invitation manager")
        with col3:
            if st.button("💰 Contribution Ask", use_container_width=True):
                st.info("Contribution request composer")
    
    with tab2:
        st.markdown("### 💰 Alumni Contributions")
        
        # Contribution stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Raised", "$50,000", "+$5,000")
        with col2:
            st.metric("This Year", "$15,000", "+$2,000")
        with col3:
            st.metric("Active Donors", "156", "+12")
        
        # Recent contributions
        st.markdown("#### Recent Contributions")
        
        contributions = [
            {"donor": "Dr. Robert Brown", "amount": "$1,000", "date": "2024-01-15", "purpose": "Scholarship"},
            {"donor": "Lisa Taylor", "amount": "$500", "date": "2024-01-10", "purpose": "Infrastructure"},
            {"donor": "David Wilson", "amount": "$250", "date": "2024-01-05", "purpose": "General Fund"}
        ]
        
        for contrib in contributions:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{contrib['donor']}**")
                st.caption(f"Date: {contrib['date']} • Purpose: {contrib['purpose']}")
            with col2:
                st.write(f"**{contrib['amount']}**")
            with col3:
                if st.button("Thank", key=f"thank_{contrib['donor']}"):
                    st.success(f"Thank you note sent to {contrib['donor']}")
    
    with tab3:
        st.markdown("### 🎯 Alumni Engagement")
        
        # Engagement metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Event Attendance", "65%", "+5%")
        with col2:
            st.metric("Mentorship", "45 alumni", "+8")
        with col3:
            st.metric("Response Rate", "78%", "+3%")
        
        # Engagement initiatives
        st.markdown("#### 📋 Engagement Initiatives")
        
        initiatives = [
            {"name": "Mentorship Program", "participants": "45", "status": "Active", "rating": "4.8/5"},
            {"name": "Alumni Talks", "participants": "120", "status": "Active", "rating": "4.5/5"},
            {"name": "Career Guidance", "participants": "85", "status": "Active", "rating": "4.7/5"}
        ]
        
        for initiative in initiatives:
            with st.expander(f"{initiative['name']} - {initiative['participants']} participants"):
                st.write(f"**Status:** {initiative['status']}")
                st.write(f"**Rating:** {initiative['rating']}")
                if st.button("Manage", key=f"manage_{initiative['name']}"):
                    st.info(f"Managing {initiative['name']}")
