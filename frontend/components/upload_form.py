
import streamlit as st


def render_upload_form():
    uploaded_file = st.file_uploader(
        "Photo or video",
        type=[
            "png", "jpg", "jpeg", "webp", "gif",
            "mp4", "avi", "mov", "mkv", "webm",
        ],
        help="Your backend currently limits uploads to 10 MB.",
    )

    caption = st.text_area(
        "Caption",
        placeholder="What are you up to?",
        max_chars=500,
        height=100,
    )

    return uploaded_file, caption