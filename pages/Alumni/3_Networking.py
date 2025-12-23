import streamlit as st
import pandas as pd

def alumni_networking_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">🤝 Alumni Networking</h1>', unsafe_allow_html=True)
    
    # Tabs for networking features
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Find Alumni", "📨 Connection Requests", "👥 My Network", "💼 Job Board"])
    
    with tab1:
        st.markdown("### Find Alumni Professionals")
        
        # Advanced search
        col1, col2, col3 = st.columns(3)
        with col1:
            search_name = st.text_input("Search by name")
            search_company = st.text_input("Search by company")
        with col2:
            batch_year = st.multiselect("Batch Year", ["2015-2020", "2021-2023", "2024+"])
            industry = st.selectbox("Industry", ["All", "Technology", "Finance", "Healthcare", "Education", "Other"])
        with col3:
            location = st.selectbox("Location", ["All", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "International", "Remote"])
            skills = st.multiselect("Skills", ["Python", "Java", "Management", "Data Science", "Marketing"])
        
        # Alumni directory
        st.markdown("### 👥 Alumni Directory")
        
        alumni_list = [
            {"name": "Dr. Robert Brown", "company": "Google", "position": "Senior Engineer", 
             "batch": 2020, "location": "Bangalore", "skills": ["Python", "AI/ML", "Leadership"]},
            {"name": "Lisa Taylor", "company": "Microsoft", "position": "Product Manager", 
             "batch": 2021, "location": "Hyderabad", "skills": ["Product", "Management", "Strategy"]},
            {"name": "David Wilson", "company": "Amazon", "position": "Data Scientist", 
             "batch": 2022, "location": "Bangalore", "skills": ["Data Science", "Python", "SQL"]},
            {"name": "Priya Sharma", "company": "Infosys", "position": "Software Developer", 
             "batch": 2023, "location": "Mumbai", "skills": ["Java", "Spring", "Microservices"]}
        ]
        
        for alumni in alumni_list:
            with st.expander(f"{alumni['name']} - {alumni['position']} at {alumni['company']}"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Batch:** {alumni['batch']}")
                    st.write(f"**Location:** {alumni['location']}")
                    st.write(f"**Skills:** {', '.join(alumni['skills'])}")
                    st.write(f"**Connect for:** Career Advice, Technical Guidance, Networking")
                with col2:
                    if st.button("Connect", key=f"conn_{alumni['name']}", use_container_width=True):
                        st.success(f"Connection request sent to {alumni['name']}")
        
        # Alumni map visualization
        st.markdown("### 📍 Alumni Locations")
        st.info("Interactive alumni map would show here")
    
    with tab2:
        st.markdown("### Connection Requests")
        
        # Pending requests
        st.markdown("#### 📥 Pending Requests")
        pending = [
            {"name": "Alex Johnson", "company": "TCS", "position": "Developer", 
             "message": "Would like to connect for career guidance", "time": "2 days ago"},
            {"name": "Meera Nair", "company": "Wipro", "position": "Analyst", 
             "message": "Fellow alumni from 2021 batch", "time": "1 week ago"}
        ]
        
        for req in pending:
            col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
            with col1:
                st.write(f"**{req['name']}**")
                st.caption(f"{req['position']} at {req['company']}")
                st.caption(req['message'])
                st.caption(f"⏰ {req['time']}")
            with col2:
                if st.button("✅", key=f"acc_{req['name']}", help="Accept"):
                    st.success(f"Connected with {req['name']}")
            with col3:
                if st.button("❌", key=f"rej_{req['name']}", help="Reject"):
                    st.info(f"Declined {req['name']}")
            with col4:
                if st.button("💬", key=f"msg_{req['name']}", help="Message"):
                    st.info(f"Messaging {req['name']}")
        
        # Sent requests
        st.markdown("#### 📤 Sent Requests")
        sent = [
            {"name": "Raj Kumar", "company": "IBM", "status": "Pending", "sent": "3 days ago"},
            {"name": "Sneha Patel", "company": "Accenture", "status": "Accepted", "sent": "1 week ago"}
        ]
        
        for req in sent:
            st.write(f"**{req['name']}** ({req['company']}) - {req['status']} • Sent {req['sent']}")
    
    with tab3:
        st.markdown("### My Professional Network")
        
        # Network stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Connections", "156")
        with col2:
            st.metric("New This Month", "8")
        with col3:
            st.metric("Industry Leaders", "12")
        
        # Connection categories
        categories = {
            "Technology": 45,
            "Finance": 28,
            "Healthcare": 15,
            "Education": 22,
            "Entrepreneurs": 18,
            "Others": 28
        }
        
        st.markdown("#### 📊 Network by Industry")
        for category, count in categories.items():
            st.write(f"{category}: {count} connections")
            st.progress(count / 156)
        
        # Recent connections
        st.markdown("#### 🤝 Recent Connections")
        recent = [
            {"name": "John Mathew", "company": "TechCorp", "connected": "2 days ago"},
            {"name": "Anita Desai", "company": "FinancePlus", "connected": "1 week ago"},
            {"name": "Rohit Verma", "company": "HealthCare Inc", "connected": "2 weeks ago"}
        ]
        
        for conn in recent:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{conn['name']}**")
                st.caption(f"{conn['company']} • Connected {conn['connected']}")
            with col2:
                if st.button("Message", key=f"msg_conn_{conn['name']}"):
                    st.info(f"Messaging {conn['name']}")
    
    with tab4:
        st.markdown("### 💼 Alumni Job Board")
        
        # Post job button
        if st.button("➕ Post Job Opportunity", use_container_width=True):
            st.info("Job posting form")
        
        # Job listings
        jobs = [
            {"title": "Senior Python Developer", "company": "Alumni Startup", "type": "Full-time", 
             "location": "Remote", "posted_by": "Rajesh K (2018)", "salary": "$80k-$120k"},
            {"title": "Data Analyst", "company": "Finance Corp", "type": "Contract", 
             "location": "Mumbai", "posted_by": "Priya S (2020)", "salary": "Competitive"},
            {"title": "Product Manager", "company": "Tech Giant", "type": "Full-time", 
             "location": "Bangalore", "posted_by": "Alumni Association", "salary": "$100k-$150k"}
        ]
        
        for job in jobs:
            with st.expander(f"{job['title']} - {job['company']}"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Type:** {job['type']}")
                    st.write(f"**Location:** {job['location']}")
                    st.write(f"**Salary:** {job['salary']}")
                    st.write(f"**Posted by:** {job['posted_by']}")
                with col2:
                    if st.button("Apply", key=f"apply_job_{job['title']}"):
                        st.success("Application submitted!")
