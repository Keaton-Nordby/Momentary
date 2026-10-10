
import streamlit as st

from services.auth import logout
from utils.formatting import initials


def render_sidebar():
    st.sidebar.markdown(
        """
        <div class="brand">
            <div class="brand-icon">◉</div>
            <div>
                <div class="brand-title">momentary</div>
                <div class="brand-subtitle">little moments, as they happen</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    user = st.session_state.user or {}
    email = user.get("email", "Your account")

    st.sidebar.markdown(
        f"""
        <div class="user-card">
            <div class="avatar">{initials(email)}</div>
            <div>
                <strong>You're in.</strong>
                <div class="user-card-email">{email}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    page = st.sidebar.radio(
        "Navigate",
        ["Feed", "Share a moment"],
        format_func=lambda value: (
            "◫   Feed" if value == "Feed"
            else "＋   Share a moment"
        ),
        label_visibility="collapsed",
        index=0 if st.session_state.page == "Feed" else 1,
    )

    st.session_state.page = page

    st.sidebar.markdown(
        "<div class='sidebar-footnote'>"
        "A little less scrolling.<br>A little more living."
        "</div>",
        unsafe_allow_html=True,
    )

    if st.sidebar.button("Sign out", use_container_width=True):
        logout()