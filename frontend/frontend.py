
import streamlit as st

from services.auth import initialize_session
from styles.theme import apply_theme
from components.navbar import render_sidebar
from screens.auth import login_page
from screens.feed import feed_page
from screens.upload import upload_page

st.set_page_config(
    page_title="Momentary",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_session()
apply_theme()

if st.session_state.user is None:
    login_page()
else:
    render_sidebar()

    if st.session_state.page == "Feed":
        feed_page()
    else:
        upload_page()