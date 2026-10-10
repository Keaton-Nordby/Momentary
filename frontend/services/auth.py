
import streamlit as st

# Verify this route against your running FastAPI backend.
PROFILE_PATH = "/auth/me"


def initialize_session():
    st.session_state.setdefault("token", None)
    st.session_state.setdefault("user", None)
    st.session_state.setdefault("page", "Feed")


def logout():
    st.session_state.token = None
    st.session_state.user = None
    st.session_state.page = "Feed"
    st.rerun()