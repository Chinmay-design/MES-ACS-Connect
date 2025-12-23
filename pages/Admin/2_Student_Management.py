import streamlit as st
import pandas as pd
from utils.database import db
from datetime import datetime

def admin_student_management_page():
    st.markdown('<h1 class="main-header">👨‍🎓 Student Management</h1>', unsafe_allow_html=True)
    
    # Tabs for different management sections
    tab1, tab2, tab3, tab4 = st.tabs(["📋 All Students", "🎓 Promote to Alumni", "✅ Pending Approvals", "📊 Statistics"])
    
    with tab1:
        st.markdown("### All Students")
        
        # Search and filters
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            search = st.text_input("Search students", placeholder="Name, ID, or email")
        with col2:
            year_filter = st.selectbox("Year", ["All", "1st Year PUC", "2nd Year PUC"])
        with col3:
            stream_filter = st.selectbox("Stream", ["All", "Science", "Commerce", "Arts"])
        with col4:
            status_filter = st.selectbox("Status", ["All", "Active", "Pending", "Suspended"])
        
        # Student data table
        students = [
            {"id": 1, "name": "John Doe", "id_card": "MES20240001", "year": "1st Year PUC", 
             "stream": "Science", "section": "A", "email": "john@mes.edu", "status": "Active", "joined": "2024-01-15"},
            {"id": 2, "name": "Sarah Smith", "id_card": "MES20240002", "year": "2nd Year PUC", 
             "stream": "Commerce", "section": "B", "email": "sarah@mes.edu", "status": "Active", "joined": "2023-08-20"},
            {"id": 3, "name": "Mike Chen", "id_card": "MES20240003", "year": "1st Year PUC", 
             "stream": "Arts", "section": "C", "email": "mike@mes.edu", "status": "Pending", "joined": "2024-02-10"},
            {"id": 4, "name": "Emma Wilson", "id_card": "MES20240004", "year": "2nd Year PUC", 
             "stream": "Science", "section": "A", "email": "emma@mes.edu", "status": "Active", "joined": "2023-07-05"},
            {"id": 5, "name": "Raj Patel", "id_card": "MES20240005", "year": "2nd Year PUC", 
             "stream": "Commerce", "section": "B", "email": "raj@mes.edu", "status": "Active", "joined": "2023-09-12"},
            {"id": 6, "name": "Priya Sharma", "id_card": "MES20240006", "year": "1st Year PUC", 
             "stream": "Science", "section": "D", "email": "priya@mes.edu", "status": "Suspended", "joined": "2024-01-08"}
        ]
        
        # Apply filters
        if year_filter != "All":
            students = [s for s in students if s['year'] == year_filter]
        if stream_filter != "All":
            students = [s for s in students if s['stream'] == stream_filter]
        if status_filter != "All":
            students = [s for s in students if s['status'] == status_filter]
        if search:
            students = [s for s in students if search.lower() in s['name'].lower() or search.lower() in s['id_card'].lower()]
        
        # Convert to DataFrame for display
        df = pd.DataFrame(students)
        
        if not df.empty:
            # Display with checkboxes for selection
            st.dataframe(df[['name', 'id_card', 'year', 'stream', 'section', 'email', 'status', 'joined']], 
                        use_container_width=True)
            
            # Selected students for bulk actions
            selected_ids = st.multiselect(
                "Select students for bulk actions",
                options=[f"{s['name']} ({s['id_card']})" for s in students],
                placeholder="Choose students..."
            )
            
            # Bulk actions
            if selected_ids:
                st.markdown("### ⚡ Bulk Actions")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    if st.button("📧 Send Email", use_container_width=True):
                        st.success(f"Email sent to {len(selected_ids)} students")
                with col2:
                    if st.button("✅ Approve All", use_container_width=True):
                        st.success(f"Approved {len(selected_ids)} students")
                with col3:
                    if st.button("⚠️ Suspend", use_container_width=True):
                        st.warning(f"Suspended {len(selected_ids)} students")
                with col4:
                    if st.button("🎓 Promote", use_container_width=True):
                        st.session_state.selected_for_promotion = selected_ids
                        st.session_state.page = "Admin/2_Student_Management"
                        st.rerun()
        else:
            st.info("No students found matching the criteria.")
        
        # Individual student actions
        st.markdown("### 🔧 Individual Student Actions")
        selected_id = st.number_input("Enter Student ID", min_value=1, max_value=1000, value=1, step=1)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("View Full Profile", use_container_width=True):
                st.info(f"Viewing full profile of Student ID: {selected_id}")
        with col2:
            if st.button("Edit Details", use_container_width=True):
                st.info(f"Editing Student ID: {selected_id}")
        with col3:
            if st.button("Activate/Suspend", use_container_width=True):
                st.warning(f"Toggling status for Student ID: {selected_id}")
        with col4:
            if st.button("Send Message", use_container_width=True):
                st.info(f"Sending message to Student ID: {selected_id}")
    
    with tab2:
        st.markdown("### 🎓 Promote Students to Alumni")
        
        st.warning("""
        ⚠️ **Important Promotion Rules:**
        - Only 2nd Year PUC students are eligible
        - Graduation year is **required**
        - Promotion is **instant** and **cannot be reversed**
        - Students will receive automatic notifications
        - Consider adding alumni-specific information
        """)
        
        # Step 1: Select students for promotion
        st.markdown("#### Step 1: Select Students")
        
        # Eligible students (2nd Year PUC)
        eligible_students = [
            {"id": 2, "name": "Sarah Smith", "id_card": "MES20240002", "year": "2nd Year PUC", 
             "stream": "Commerce", "section": "B", "status": "Active"},
            {"id": 4, "name": "Emma Wilson", "id_card": "MES20240004", "year": "2nd Year PUC", 
             "stream": "Science", "section": "A", "status": "Active"},
            {"id": 5, "name": "Raj Patel", "id_card": "MES20240005", "year": "2nd Year PUC", 
             "stream": "Commerce", "section": "B", "status": "Active"}
        ]
        
        # Multi-select for bulk promotion
        selected_students = st.multiselect(
            "Select students for promotion *",
            options=[f"{s['name']} ({s['id_card']} - {s['stream']})" for s in eligible_students],
            default=getattr(st.session_state, 'selected_for_promotion', []),
            format_func=lambda x: x,
            help="Select multiple students for bulk promotion"
        )
        
        if selected_students:
            # Display selected students
            st.markdown("##### Selected Students:")
            for student_str in selected_students:
                st.info(f"✅ {student_str}")
        
        # Step 2: Graduation year
        st.markdown("#### Step 2: Graduation Details")
        
        current_year = datetime.now().year
        graduation_year = st.number_input(
            "Graduation Year *",
            min_value=2000,
            max_value=current_year,
            value=current_year,
            help="Year when students completed their PUC"
        )
        
        # Step 3: Additional alumni information (optional)
        st.markdown("#### Step 3: Additional Information (Optional)")
        
        col1, col2 = st.columns(2)
        with col1:
            default_company = st.text_input("Default Company", placeholder="If students have jobs")
            default_position = st.text_input("Default Position", placeholder="Job title")
        with col2:
            collect_later = st.checkbox("Collect details later", value=True)
            send_welcome = st.checkbox("Send welcome email", value=True)
        
        # Step 4: Confirmation and promotion
        st.markdown("#### Step 4: Confirm Promotion")
        
        if selected_students and graduation_year:
            # Get selected student IDs
            selected_ids = []
            selected_names = []
            for student_str in selected_students:
                for s in eligible_students:
                    if f"{s['name']} ({s['id_card']} - {s['stream']})" == student_str:
                        selected_ids.append(s['id'])
                        selected_names.append(s['name'])
            
            # Show promotion summary
            st.markdown("##### 📋 Promotion Summary")
            summary_df = pd.DataFrame([
                {
                    "Student": s['name'],
                    "ID Card": s['id_card'],
                    "Stream": s['stream'],
                    "Graduation Year": graduation_year,
                    "New Role": "Alumni"
                }
                for s in eligible_students if s['id'] in selected_ids
            ])
            st.dataframe(summary_df, use_container_width=True)
            
            # Confirmation
            confirm = st.checkbox("I confirm that these students have completed their PUC and are eligible for alumni status")
            
            # Promotion button
            if st.button("🚀 Promote Selected Students", type="primary", use_container_width=True, disabled=not confirm):
                # In real app, call: db.promote_students_to_alumni(selected_ids, graduation_year, admin_id)
                promotion_success = True  # Simulated success
                
                if promotion_success:
                    st.success(f"✅ Successfully promoted {len(selected_ids)} students to alumni!")
                    st.balloons()
                    
                    # Show success details
                    st.markdown("""
                    <div class="success-box">
                    <strong>Promotion Completed Successfully!</strong><br>
                    • Students have been moved to alumni database<br>
                    • Alumni profiles have been created<br>
                    • Welcome emails have been sent<br>
                    • Access permissions have been updated
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Clear selection
                    if hasattr(st.session_state, 'selected_for_promotion'):
                        del st.session_state.selected_for_promotion
                    
                    # Refresh button
                    if st.button("🔄 Refresh Page", use_container_width=True):
                        st.rerun()
                else:
                    st.error("Failed to promote students. Please try again.")
        else:
            st.error("Please select at least one student and enter graduation year")
    
    with tab3:
        st.markdown("### ✅ Pending Student Approvals")
        
        pending_students = [
            {"id": 3, "name": "Mike Chen", "id_card": "MES20240003", "email": "mike@mes.edu",
             "stream": "Arts", "year": "1st Year PUC", "applied": "2024-02-10", "documents": "Submitted"},
            {"id": 7, "name": "Anjali Gupta", "id_card": "MES20240007", "email": "anjali@mes.edu",
             "stream": "Science", "year": "2nd Year PUC", "applied": "2024-02-12", "documents": "Pending"},
            {"id": 8, "name": "Rahul Verma", "id_card": "MES20240008", "email": "rahul@mes.edu",
             "stream": "Commerce", "year": "1st Year PUC", "applied": "2024-02-14", "documents": "Submitted"}
        ]
        
        for student in pending_students:
            with st.expander(f"{student['name']} - {student['id_card']}"):
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**Email:** {student['email']}")
                    st.write(f"**Stream:** {student['stream']} • **Year:** {student['year']}")
                    st.write(f"**Applied:** {student['applied']}")
                    st.write(f"**Documents:** {student['documents']}")
                with col2:
                    if st.button("✅ Approve", key=f"app_pend_{student['id']}", use_container_width=True):
                        st.success(f"Approved {student['name']}")
                with col3:
                    if st.button("❌ Reject", key=f"rej_pend_{student['id']}", use_container_width=True):
                        st.error(f"Rejected {student['name']}")
    
    with tab4:
        st.markdown("### 📊 Student Statistics")
        
        # Statistics cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Students", "245", "+15")
        with col2:
            st.metric("1st Year PUC", "120", "+8")
        with col3:
            st.metric("2nd Year PUC", "125", "+7")
        with col4:
            st.metric("Pending Verification", "15", "-3")
        
        # Stream distribution chart
        st.markdown("#### 📚 Stream Distribution")
        
        stream_data = pd.DataFrame({
            'Stream': ['Science', 'Commerce', 'Arts'],
            'Count': [120, 85, 40]
        })
        
        fig = px.bar(stream_data, x='Stream', y='Count', 
                    color='Stream', title='Students by Stream',
                    color_discrete_sequence=['#3b82f6', '#10b981', '#8b5cf6'])
        st.plotly_chart(fig, use_container_width=True)
        
        # Monthly registrations
        st.markdown("#### 📈 Monthly Registrations")
        
        month_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Registrations': [45, 38, 52, 48, 42, 35]
        })
        
        fig2 = px.line(month_data, x='Month', y='Registrations', 
                      title='New Student Registrations',
                      markers=True)
        st.plotly_chart(fig2, use_container_width=True)
