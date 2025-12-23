import streamlit as st

def alumni_chat_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">💬 Alumni Chat</h1>', unsafe_allow_html=True)
    
    # Note about professional networking
    st.info("💼 **Professional Networking Chat:** Connect with fellow alumni for career discussions, mentorship, and collaborations")
    
    # Two-column layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Connections list
        st.markdown("### 👥 Connections")
        
        connections = [
            {"name": "Dr. Robert Brown", "company": "Google", "status": "🟢 Online", "unread": 2},
            {"name": "Lisa Taylor", "company": "Microsoft", "status": "🟢 Online", "unread": 0},
            {"name": "David Wilson", "company": "Amazon", "status": "⚫ Offline", "unread": 0},
            {"name": "Priya Sharma", "company": "Infosys", "status": "🟢 Online", "unread": 1}
        ]
        
        selected_connection = st.selectbox(
            "Select connection",
            [c["name"] for c in connections],
            format_func=lambda x: f"{x} ({next((c for c in connections if c['name'] == x), {}).get('company', '')})"
        )
        
        # Professional groups
        st.markdown("### 👥 Professional Groups")
        groups = [
            {"name": "Tech Alumni Network", "members": 45, "unread": 5},
            {"name": "Entrepreneurs Forum", "members": 28, "unread": 2},
            {"name": "Mentorship Circle", "members": 32, "unread": 0}
        ]
        
        selected_group = st.selectbox(
            "Select group",
            [g["name"] for g in groups]
        )
        
        # New professional chat
        if st.button("💼 Start Professional Chat", use_container_width=True):
            st.info("Select alumni to start professional discussion")
    
    with col2:
        if selected_connection:
            # Chat header
            connection_info = next((c for c in connections if c['name'] == selected_connection), {})
            
            col_header1, col_header2 = st.columns([3, 1])
            with col_header1:
                st.markdown(f"### 💼 Chat with {selected_connection}")
                st.caption(f"{connection_info.get('company', '')} • {connection_info.get('status', '')}")
            with col_header2:
                if st.button("📋 Profile", use_container_width=True):
                    st.info(f"Viewing {selected_connection}'s professional profile")
            
            # Professional chat messages
            chat_container = st.container(height=400)
            
            with chat_container:
                messages = [
                    {"sender": selected_connection, "text": "Hi! Thanks for connecting. I saw your profile at Google - impressive work!", 
                     "time": "10:30 AM", "is_me": False},
                    {"sender": "You", "text": "Thank you! I've been following your work at Microsoft too. The product launch was great!", 
                     "time": "10:32 AM", "is_me": True},
                    {"sender": selected_connection, "text": "Appreciate it! I noticed you're working on AI projects. Would love to discuss potential collaborations.", 
                     "time": "10:33 AM", "is_me": False},
                    {"sender": "You", "text": "Absolutely! We're exploring some new ML applications. Could schedule a call next week?", 
                     "time": "10:35 AM", "is_me": True},
                    {"sender": selected_connection, "text": "Perfect! How about Tuesday at 3 PM? I can share some insights from our recent projects.", 
                     "time": "10:36 AM", "is_me": False},
                ]
                
                for msg in messages:
                    if msg["is_me"]:
                        st.markdown(f"""
                        <div style="display: flex; justify-content: flex-end; margin: 10px 0;">
                            <div style="background: #10b981; color: white; padding: 10px 15px; 
                                      border-radius: 15px 15px 5px 15px; max-width: 70%;">
                                <div>{msg['text']}</div>
                                <div style="text-align: right; font-size: 0.8em; opacity: 0.8;">
                                    {msg['time']}
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="display: flex; justify-content: flex-start; margin: 10px 0;">
                            <div style="background: #f1f1f1; color: black; padding: 10px 15px; 
                                      border-radius: 15px 15px 15px 5px; max-width: 70%;">
                                <div><strong>{msg['sender']}</strong></div>
                                <div>{msg['text']}</div>
                                <div style="font-size: 0.8em; opacity: 0.6;">{msg['time']}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Professional chat input
            st.markdown("---")
            
            col_input1, col_input2 = st.columns([5, 1])
            with col_input1:
                new_message = st.text_input(
                    "Type professional message...", 
                    placeholder=f"Message {selected_connection} about collaboration",
                    label_visibility="collapsed"
                )
            with col_input2:
                if st.button("Send", disabled=not new_message.strip(), use_container_width=True):
                    st.success("Professional message sent!")
                    st.rerun()
            
            # Professional chat features
            st.markdown("### 💼 Professional Features")
            
            feature_col1, feature_col2, feature_col3 = st.columns(3)
            with feature_col1:
                if st.button("📅 Schedule Call", use_container_width=True):
                    st.info("Schedule a professional call")
            with feature_col2:
                if st.button("📎 Share File", use_container_width=True):
                    st.info("Share professional document")
            with feature_col3:
                if st.button("🤝 Collaboration", use_container_width=True):
                    st.info("Start collaboration project")
        
        elif selected_group:
            st.markdown(f"### 👥 {selected_group}")
            st.info("Professional group chat for networking and collaboration")
