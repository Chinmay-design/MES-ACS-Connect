import streamlit as st
from datetime import datetime

def student_chat_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">💬 Chat</h1>', unsafe_allow_html=True)
    
    st.info("💡 You can only chat with your confirmed friends")
    
    # Two-column layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Friends list for chat
        st.markdown("### 👥 Friends")
        
        # Search friends
        search_chat = st.text_input("Search friends...", placeholder="Type name to search")
        
        # Friends list with online status
        friends = [
            {"name": "Alex Johnson", "status": "🟢 Online", "last_seen": "Now", "unread": 3},
            {"name": "Mike Chen", "status": "🟢 Online", "last_seen": "2 min ago", "unread": 0},
            {"name": "David Brown", "status": "🟢 Online", "last_seen": "5 min ago", "unread": 1},
            {"name": "Sarah Miller", "status": "⚫ Offline", "last_seen": "1 hour ago", "unread": 0},
            {"name": "Emma Wilson", "status": "⚫ Offline", "last_seen": "3 hours ago", "unread": 0}
        ]
        
        # Filter friends based on search
        if search_chat:
            friends = [f for f in friends if search_chat.lower() in f['name'].lower()]
        
        # Display friends
        selected_friend = st.selectbox(
            "Select a friend to chat",
            [f["name"] for f in friends],
            format_func=lambda x: f"{x} {next((f for f in friends if f['name'] == x), {}).get('status', '')}"
        )
        
        # Group chats
        st.markdown("### 👥 Group Chats")
        groups = [
            {"name": "Science Study Group", "unread": 5},
            {"name": "Math Club", "unread": 2},
            {"name": "Class of 2024", "unread": 0}
        ]
        
        selected_group = st.selectbox(
            "Select a group",
            [g["name"] for g in groups],
            format_func=lambda x: f"{x} ({next((g for g in groups if g['name'] == x), {}).get('unread', 0)})"
        )
        
        # Create new chat
        if st.button("➕ New Chat", use_container_width=True):
            st.info("Select a friend to start new chat")
    
    with col2:
        if selected_friend:
            # Chat header
            col_header1, col_header2 = st.columns([3, 1])
            with col_header1:
                st.markdown(f"### 💬 Chat with {selected_friend}")
                st.caption("🟢 Online • Last seen: Just now")
            with col_header2:
                if st.button("ℹ️ Info", use_container_width=True):
                    st.info(f"Info about {selected_friend}")
            
            # Chat messages container
            chat_container = st.container(height=400)
            
            with chat_container:
                # Sample chat messages
                messages = [
                    {"sender": selected_friend, "text": "Hey! How's the assignment going?", 
                     "time": "10:30 AM", "is_me": False, "read": True},
                    {"sender": "You", "text": "Almost done! Just finishing the last section.", 
                     "time": "10:32 AM", "is_me": True, "read": True},
                    {"sender": selected_friend, "text": "Great! Can you share your notes for chapter 5?", 
                     "time": "10:33 AM", "is_me": False, "read": True},
                    {"sender": "You", "text": "Sure, I'll send them after class. They're pretty comprehensive!", 
                     "time": "10:35 AM", "is_me": True, "read": True},
                    {"sender": selected_friend, "text": "Thanks! 🎉 That would be really helpful.", 
                     "time": "10:36 AM", "is_me": False, "read": True},
                    {"sender": selected_friend, "text": "By the way, are you coming to the study group tomorrow?", 
                     "time": "10:37 AM", "is_me": False, "read": False},
                ]
                
                for msg in messages:
                    if msg["is_me"]:
                        # My message (right aligned)
                        st.markdown(f"""
                        <div style="display: flex; justify-content: flex-end; margin: 10px 0;">
                            <div style="background: #3b82f6; color: white; padding: 10px 15px; 
                                      border-radius: 15px 15px 5px 15px; max-width: 70%;">
                                <div>{msg['text']}</div>
                                <div style="text-align: right; font-size: 0.8em; opacity: 0.8;">
                                    {msg['time']} {'✓✓' if msg['read'] else '✓'}
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        # Friend's message (left aligned)
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
            
            # Message input area
            st.markdown("---")
            
            col_input1, col_input2, col_input3 = st.columns([6, 1, 1])
            with col_input1:
                new_message = st.text_input(
                    "Type a message...", 
                    placeholder=f"Message {selected_friend}",
                    label_visibility="collapsed",
                    key="message_input"
                )
            with col_input2:
                # Emoji picker
                if st.button("😊", use_container_width=True):
                    st.info("Emoji picker would open here")
            with col_input3:
                send_disabled = not new_message.strip()
                if st.button("Send", disabled=send_disabled, use_container_width=True):
                    if new_message:
                        st.success("Message sent!")
                        st.rerun()
            
            # Chat features
            st.markdown("### 💬 Chat Features")
            
            feature_col1, feature_col2, feature_col3 = st.columns(3)
            with feature_col1:
                if st.button("📎 Attach File", use_container_width=True):
                    st.info("File attachment feature")
            with feature_col2:
                if st.button("🎤 Voice Message", use_container_width=True):
                    st.info("Voice message feature")
            with feature_col3:
                if st.button("📞 Call", use_container_width=True):
                    st.info("Voice call feature")
            
            # Typing indicator (simulated)
            st.caption("✍️ Alex is typing...")
        
        elif selected_group:
            st.markdown(f"### 👥 {selected_group} Chat")
            st.info("Group chat feature coming soon!")
