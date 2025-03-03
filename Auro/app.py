import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

# Custom CSS for UI Enhancements
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stApp {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .stSidebar {
            background-color: #2E3B4E;
            color: white;
        }
        .stButton>button {
            background-color: #007BFF !important;
            color: white !important;
            border-radius: 5px;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            border: 1px solid #007BFF !important;
            border-radius: 5px;
        }
        .stSelectbox>div>div>select {
            border: 1px solid #007BFF !important;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("Auro.edu Backend Developer Recruitment Task Tracker")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Community Engagement", "Course Completion", "Certificate Upload"])

# Task 1: Community Engagement Activities
if menu == "Community Engagement":
    st.header("Community Engagement Tracker")
    st.write("Log your engagement activities below.")

    # Create a Poll
    st.subheader("Create a Poll")
    poll_question = st.text_input("Enter your poll question:")
    poll_options = st.text_area("Enter poll options (comma-separated):")
    poll_data = None
    if st.button("Submit Poll"):
        if poll_question and poll_options:
            options_list = poll_options.split(',')
            poll_data = {option.strip(): 0 for option in options_list}
            st.session_state["poll"] = {"question": poll_question, "options": poll_data}
            st.success("Poll Created Successfully!")
        else:
            st.error("Please provide a question and at least one option.")
    
    # Display Poll if created
    if "poll" in st.session_state:
        st.subheader("Current Poll")
        st.write(st.session_state["poll"]["question"])
        for option in st.session_state["poll"]["options"].keys():
            if st.button(f"Vote for {option}"):
                st.session_state["poll"]["options"][option] += 1
        
        st.subheader("Poll Results")
        for option, votes in st.session_state["poll"]["options"].items():
            st.write(f"{option}: {votes} votes")
    
    # Post Your Thoughts
    st.subheader("Post Your Thoughts")
    thought_content = st.text_area("Share your thoughts:")
    if st.button("Submit Thought"):
        if thought_content:
            st.success("Your thought has been posted successfully!")
        else:
            st.error("Please write something before submitting.")
    
    # Ask a Question
    st.subheader("Ask a Question")
    question_content = st.text_area("Ask a relevant question:")
    if st.button("Submit Question"):
        if question_content:
            st.success("Your question has been posted successfully!")
        else:
            st.error("Please write a question before submitting.")
    
    # Engage with the Community
    st.subheader("Engage with the Community")
    engagement_activities = ["Upvote", "Downvote", "Comment"]
    engagement_selection = st.multiselect("Select your engagement activities:", engagement_activities)
    if engagement_selection:
        st.success(f"You have engaged in: {', '.join(engagement_selection)}")
    
# Task 2: Course Completion
elif menu == "Course Completion":
    st.header("Course Completion Progress")
    
    courses = [
        "Advanced Python Programming", "Mastering Django", "Mastering Flask", "Mastering Node.js & Express.js",
        "Advanced PHP", "Advanced Laravel", "Mastering Ruby on Rails", "DevOps Practices and CI/CD"
    ]
    
    selected_course = st.selectbox("Select your course:", courses)
    quiz_score = st.slider("Final Exam Score (%)", 0, 100, 70)
    
    if quiz_score >= 70:
        st.success(f"Congratulations! You have completed {selected_course} with {quiz_score}%.")
    else:
        st.error("You need at least 70% to pass and receive the certificate.")
    
# Task 3: Certificate Upload
elif menu == "Certificate Upload":
    st.header("Upload Your Accreditation Certificate")
    uploaded_file = st.file_uploader("Upload your certificate (PDF or Image)", type=["pdf", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.success("Certificate uploaded successfully!")
        st.image(uploaded_file, caption="Your Accreditation Certificate", use_column_width=True)
        
# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed with ❤️ using Streamlit")