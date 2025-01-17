# streamlit_app.py
import streamlit as st
from utils.transcription import transcribe_video
from utils.search import search_moments_in_transcription
from utils.story_creation import create_story_from_video

st.title('AI Video Editing & Storytelling Tool')

uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "mov"])

if uploaded_file is not None:
    # Save uploaded file
    with open("uploads/" + uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File successfully uploaded")
    
    # Transcribe the video and show transcription
    transcription = transcribe_video("uploads/" + uploaded_file.name)
    st.text_area("Transcription", transcription, height=200)

    # Search for specific moments
    keyword = st.text_input("Search for a moment (e.g., 'vacation')", "")
    if keyword:
        moments = search_moments_in_transcription(transcription, keyword)
        st.write("Found Moments:", moments)
    
    # Create a story from the video
    if st.button("Create Story"):
        story = create_story_from_video("uploads/" + uploaded_file.name, keyword)
        st.text_area("Generated Story", story, height=200)
