import streamlit as st

def admin_confession_moderation_page():
    st.markdown('<h1 class="main-header">🤫 Confession Moderation</h1>', unsafe_allow_html=True)
    
    st.warning("""
    ⚠️ **ADMIN PRIVILEGES - CONFIDENTIAL**  
    • You can see real identities of confession posters  
    • Regular users see only "Anonymous User"  
    • Use this power responsibly for community safety
    """)
    
    # Tabs for moderation sections
    tab1, tab2, tab3, tab4 = st.tabs(["⏳ Pending Approval", "🚨 Reported Content", "✅ Approved", "📊 Moderation Stats"])
    
    with tab1:
        st.markdown("### Confessions Awaiting Approval")
        
        # Pending confessions with real user info
        pending_confessions = [
            {
                "confession_id": 101,
                "content": "I think the cafeteria food quality has really improved this semester. The new menu options are great!",
                "category": "Campus Life",
                "user_info": {
                    "name": "John Doe",
                    "id_card": "MES20240001",
                    "email": "john@mes.edu",
                    "year": "1st Year PUC",
                    "stream": "Science"
                },
                "posted_time": "10 minutes ago",
                "sensitive": False
            },
            {
                "confession_id": 102,
                "content": "Looking for study partner for Physics finals. I'm struggling with electromagnetism concepts.",
                "category": "Academic",
                "user_info": {
                    "name": "Sarah Smith",
                    "id_card": "MES20240002",
                    "email": "sarah@mes.edu",
                    "year": "2nd Year PUC",
                    "stream": "Commerce"
                },
                "posted_time": "25 minutes ago",
                "sensitive": False
            },
            {
                "confession_id": 103,
                "content": "I have some suggestions for improving library hours during exam season. Can we extend closing time?",
                "category": "Suggestion",
                "user_info": {
                    "name": "Mike Chen",
                    "id_card": "MES20240003",
                    "email": "mike@mes.edu",
                    "year": "1st Year PUC",
                    "stream": "Arts"
                },
                "posted_time": "1 hour ago",
                "sensitive": False
            }
        ]
        
        for conf in pending_confessions:
            # Confession card
            st.markdown(f"""
            <div style="background: #fff3cd; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem; border: 2px solid #ffc107;">
                <div style="color: #856404; font-weight: bold; margin-bottom: 0.5rem;">
                    ⏳ PENDING APPROVAL • {conf['category']}
                </div>
                <p style="margin: 0.5rem 0; font-size: 1.1rem; line-height: 1.5;">"{conf['content']}"</p>
                <div style="color: #6c757d; font-size: 0.9rem;">
                    <div><strong>Posted:</strong> {conf['posted_time']}</div>
                    <div style="background: #e9ecef; padding: 0.5rem; border-radius: 5px; margin-top: 0.5rem;">
                        <strong>👤 ADMIN VIEW (Real Identity):</strong><br>
                        • <strong>{conf['user_info']['name']}</strong><br>
                        • ID: {conf['user_info']['id_card']}<br>
                        • Email: {conf['user_info']['email']}<br>
                        • {conf['user_info']['year']} • {conf['user_info']['stream']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Moderation actions
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("✅ Approve", key=f"app_{conf['confession_id']}", use_container_width=True):
                    st.success(f"Approved confession #{conf['confession_id']}")
            with col2:
                if st.button("❌ Reject", key=f"rej_{conf['confession_id']}", use_container_width=True):
                    st.error(f"Rejected confession #{conf['confession_id']}")
            with col3:
                if st.button("✏️ Edit", key=f"edit_{conf['confession_id']}", use_container_width=True):
                    st.info(f"Editing confession #{conf['confession_id']}")
            with col4:
                if st.button("📧 Contact User", key=f"contact_{conf['confession_id']}", use_container_width=True):
                    st.info(f"Contacting {conf['user_info']['name']}")
            
            st.markdown("---")
    
    with tab2:
        st.markdown("### 🚨 Reported Confessions")
        
        # Reported confessions
        reported_confessions = [
            {
                "confession_id": 201,
                "content": "Some inappropriate content that violates community guidelines...",
                "category": "Inappropriate",
                "reports": 5,
                "report_reasons": ["Harassment", "Hate speech", "Bullying"],
                "posted_time": "2 days ago",
                "priority": "High"
            }
        ]
        
        for conf in reported_confessions:
            with st.expander(f"🚨 CONFESSION #{conf['confession_id']} - {conf['reports']} REPORTS ({conf['priority']})", expanded=True):
                st.write(f"**Content:** {conf['content']}")
                st.write(f"**Category:** {conf['category']}")
                st.write(f"**Report Reasons:** {', '.join(conf['report_reasons'])}")
                st.write(f"**Posted:** {conf['posted_time']}")
                
                # Admin warning about identity
                st.warning("""
                👤 **Admin Identity Access:**  
                User identity would be visible here for moderation purposes only.
                """)
                
                # Report details
                st.markdown("#### 📋 Report Details")
                reports = [
                    {"reporter": "User A", "reason": "Harassment", "time": "1 day ago"},
                    {"reporter": "User B", "reason": "Hate speech", "time": "2 days ago"}
                ]
                
                for report in reports:
                    st.write(f"**{report['reporter']}:** {report['reason']} ({report['time']})")
                
                # Moderation actions
                st.markdown("#### ⚖️ Moderation Actions")
                
                action_col1, action_col2, action_col3, action_col4 = st.columns(4)
                with action_col1:
                    if st.button("Remove Content", key=f"remove_{conf['confession_id']}", use_container_width=True):
                        st.error("Confession removed permanently")
                with action_col2:
                    if st.button("Warn User", key=f"warn_{conf['confession_id']}", use_container_width=True):
                        st.warning("Warning sent to user")
                with action_col3:
                    if st.button("Keep Visible", key=f"keep_{conf['confession_id']}", use_container_width=True):
                        st.success("Confession kept visible")
                with action_col4:
                    if st.button("View User", key=f"view_user_{conf['confession_id']}", use_container_width=True):
                        st.info("User details would show here")
    
    with tab3:
        st.markdown("### ✅ Approved Confessions")
        
        # Approved confessions
        approved_confessions = [
            {
                "confession_id": 301,
                "content": "The new library system is amazing! So much easier to find books now.",
                "category": "Campus Life",
                "likes": 42,
                "comments": 8,
                "approved_by": "Admin",
                "approved_time": "1 day ago",
                "user_info": "Anonymous User (to public)"
            }
        ]
        
        for conf in approved_confessions:
            st.markdown(f"""
            <div style="background: #d1e7dd; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <p style="margin: 0.5rem 0;">{conf['content']}</p>
                <div style="color: #0f5132; font-size: 0.9rem;">
                    {conf['category']} • ❤️ {conf['likes']} • 💬 {conf['comments']}<br>
                    ✅ Approved by {conf['approved_by']} • {conf['approved_time']}<br>
                    👤 Public View: {conf['user_info']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Edit", key=f"edit_app_{conf['confession_id']}"):
                    st.info("Editing approved confession")
            with col2:
                if st.button("Unpublish", key=f"unpub_{conf['confession_id']}"):
                    st.warning("Unpublish this confession?")
    
    with tab4:
        st.markdown("### 📊 Moderation Statistics")
        
        # Stats cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Confessions", "1,245", "+23")
        with col2:
            st.metric("Pending Review", "15", "-3")
        with col3:
            st.metric("Reported", "8", "+1")
        with col4:
            st.metric("Approval Rate", "92%", "+2%")
        
        # Category distribution
        st.markdown("#### 📈 Category Distribution")
        
        categories = {
            "Love & Relationships": 35,
            "Academic Stress": 28,
            "Campus Life": 20,
            "Funny Moments": 10,
            "Rants/Vents": 5,
            "Other": 2
        }
        
        for category, percentage in categories.items():
            st.write(f"**{category}**")
            st.progress(percentage / 100)
            st.caption(f"{percentage}% of total confessions")
        
        # Moderation activity
        st.markdown("#### ⏱️ Your Moderation Activity")
        
        activity = {
            "Approved Today": 12,
            "Rejected Today": 3,
            "Average Review Time": "2.5 min",
            "Accuracy Rate": "98%"
        }
        
        for stat, value in activity.items():
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.write(stat)
            with col_b:
                st.write(f"**{value}**")
