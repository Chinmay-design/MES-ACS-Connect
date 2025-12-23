import streamlit as st
import hashlib
import uuid
from datetime import datetime

def student_confessions_page():
    user = st.session_state.user
    
    st.markdown('<h1 class="main-header">🤫 Confessions</h1>', unsafe_allow_html=True)
    
    # Anonymity notice
    st.warning("""
    🔒 **Complete Anonymity Guaranteed:**
    - Your identity is hidden from everyone
    - Posts appear as "Anonymous User"
    - Only administrators can see who posted (for moderation)
    - Be respectful and follow community guidelines
    """)
    
    # Tabs for different sections
    tab1, tab2, tab3 = st.tabs(["📝 Post Confession", "🔥 Recent Confessions", "📊 Confession Stats"])
    
    with tab1:
        st.markdown("### Post a Confession")
        
        with st.form("post_confession_form"):
            # Confession content
            content = st.text_area(
                "Your confession *", 
                height=150,
                placeholder="Share your thoughts, feelings, or experiences anonymously...",
                help="Remember: Be kind, respectful, and considerate of others"
            )
            
            # Category selection
            category = st.selectbox(
                "Category",
                ["💖 Love & Relationships", "📚 Academic Stress", "🏫 Campus Life", 
                 "😤 Rant/Vent", "😂 Funny Moments", "🤔 Advice Needed", "🎉 Celebrations", 
                 "🤷 Other"]
            )
            
            # Content warnings
            st.markdown("#### ⚠️ Content Warnings")
            col1, col2, col3 = st.columns(3)
            with col1:
                sensitive = st.checkbox("Sensitive Content")
            with col2:
                trigger_warning = st.checkbox("Trigger Warning")
            with col3:
                nsfw = st.checkbox("NSFW (18+)")
            
            # Terms and conditions
            agree = st.checkbox(
                "✅ I agree to follow community guidelines and understand that: "
                "1. My post is anonymous but moderated\n"
                "2. Inappropriate content will be removed\n"
                "3. I am responsible for my words\n"
                "4. I can report problematic confessions"
            )
            
            # Submit button
            if st.form_submit_button("🚀 Post Anonymously", use_container_width=True):
                if not content.strip():
                    st.error("Please write something before posting")
                elif not agree:
                    st.error("You must agree to the guidelines")
                elif sensitive or trigger_warning or nsfw:
                    st.warning("Your confession contains warnings. Admins will review it before publishing.")
                    st.success("Confession submitted for review!")
                else:
                    # In a real app, this would save to database
                    # Generate anonymous ID
                    anonymous_id = f"anon_{hashlib.sha256(f'{user['id']}{uuid.uuid4()}'.encode()).hexdigest()[:12]}"
                    
                    st.success("✅ Confession posted anonymously!")
                    st.balloons()
                    
                    # Show what users see
                    st.markdown("""
                    <div class="info-box">
                    <strong>👤 What others see:</strong><br>
                    "Anonymous User" posted • Just now<br>
                    Your real identity is completely hidden
                    </div>
                    """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Recent Confessions")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            filter_category = st.selectbox("Filter by category", 
                                         ["All", "Love", "Academic", "Campus Life", "Funny", "Rant"])
        with col2:
            sort_by = st.selectbox("Sort by", ["Newest", "Most Liked", "Most Comments"])
        with col3:
            show_only = st.selectbox("Show", ["All", "Trending", "Unread"])
        
        # Confessions feed
        confessions = [
            {
                "id": 1,
                "content": "I have a huge crush on someone in my Chemistry class but I'm too shy to say anything 💖",
                "category": "Love",
                "likes": 42,
                "comments": 8,
                "time": "2 hours ago",
                "reactions": {"❤️": 42, "😂": 5, "😮": 3, "😢": 1}
            },
            {
                "id": 2,
                "content": "Anyone else struggling with Physics practicals? The experiments are so hard and the lab reports take forever! 📚",
                "category": "Academic",
                "likes": 28,
                "comments": 15,
                "time": "5 hours ago",
                "reactions": {"👍": 28, "💪": 12, "😩": 8}
            },
            {
                "id": 3,
                "content": "The new cafeteria food is actually pretty good! Big shoutout to the staff for trying new recipes 👏",
                "category": "Campus Life",
                "likes": 65,
                "comments": 12,
                "time": "1 day ago",
                "reactions": {"👏": 65, "😋": 20, "🎉": 15}
            },
            {
                "id": 4,
                "content": "Looking for study partners for the upcoming Math exam. DM if interested! We can create a study schedule together 🤝",
                "category": "Academic",
                "likes": 18,
                "comments": 7,
                "time": "2 days ago",
                "reactions": {"🤝": 18, "📚": 10, "💡": 5}
            }
        ]
        
        # Apply filters
        if filter_category != "All":
            confessions = [c for c in confessions if c['category'] == filter_category]
        
        # Display confessions
        for confession in confessions:
            with st.container():
                st.markdown(f"""
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem; 
                          border-left: 4px solid {'#ec4899' if confession['category'] == 'Love' else 
                                                 '#3b82f6' if confession['category'] == 'Academic' else 
                                                 '#10b981' if confession['category'] == 'Campus Life' else 
                                                 '#9333ea'};">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: bold; color: {'#ec4899' if confession['category'] == 'Love' else 
                                                               '#3b82f6' if confession['category'] == 'Academic' else 
                                                               '#10b981' if confession['category'] == 'Campus Life' else 
                                                               '#9333ea'};">{confession['category']}</span>
                        <small style="color: #6b7280;">{confession['time']}</small>
                    </div>
                    <p style="margin: 1rem 0; font-size: 1.1rem; line-height: 1.5;">{confession['content']}</p>
                    <div style="display: flex; justify-content: space-between; align-items: center; color: #6b7280;">
                        <div>
                            <span>👤 Anonymous User</span>
                            <span style="margin-left: 1rem;">❤️ {confession['likes']}</span>
                            <span style="margin-left: 0.5rem;">💬 {confession['comments']}</span>
                        </div>
                        <div>
                            <small>💭 Be kind in comments</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Interaction buttons
                col1, col2, col3, col4 = st.columns([1, 1, 1, 7])
                with col1:
                    if st.button("❤️", key=f"like_{confession['id']}"):
                        st.success("Liked!")
                with col2:
                    if st.button("💬", key=f"comment_{confession['id']}"):
                        comment = st.text_input("Add a comment", 
                                              placeholder="Add a supportive comment...",
                                              key=f"com_input_{confession['id']}")
                        if comment:
                            st.success("Comment added!")
                with col3:
                    if st.button("⚠️", key=f"report_{confession['id']}"):
                        st.warning("Report sent to moderators")
                with col4:
                    # Reactions
                    reactions = ["👍", "❤️", "😂", "😮", "😢", "🎉"]
                    selected = st.selectbox("React", reactions, 
                                          key=f"react_{confession['id']}", 
                                          label_visibility="collapsed")
                
                # Show reactions summary
                if confession.get('reactions'):
                    st.caption("Reactions: " + " ".join([f"{emoji} {count}" 
                                                       for emoji, count in confession['reactions'].items()]))
                
                st.markdown("---")
    
    with tab3:
        st.markdown("### 📊 Confession Statistics")
        
        # Stats cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Confessions", "1,245", "+23%")
        with col2:
            st.metric("Your Posts", "12", "+3")
        with col3:
            st.metric("Total Likes", "5,678", "+124")
        with col4:
            st.metric("Active Today", "342", "+18%")
        
        # Category distribution
        st.markdown("#### 📈 Category Distribution")
        
        categories = {
            "Love": 35,
            "Academic": 28,
            "Campus Life": 20,
            "Funny": 10,
            "Rant": 5,
            "Other": 2
        }
        
        for category, percentage in categories.items():
            st.write(f"**{category}**")
            st.progress(percentage / 100)
            st.caption(f"{percentage}% of all confessions")
        
        # Your activity
        st.markdown("#### 📊 Your Activity")
        
        your_stats = {
            "Posts Made": 12,
            "Total Likes Received": 156,
            "Comments Made": 24,
            "Confessions Saved": 8
        }
        
        for stat, value in your_stats.items():
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.write(stat)
            with col_b:
                st.write(f"**{value}**")
