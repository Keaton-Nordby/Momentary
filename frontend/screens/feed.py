
import streamlit as st

from components.post_card import render_post
from services.api import api_request, error_message


def feed_page():
    _, feed, _ = st.columns([1, 2, 1], gap="small")

    with feed:
        heading, action = st.columns(
            [3, 1],
            vertical_alignment="center",
        )

        with heading:
            st.markdown(
                "<div class='eyebrow'>YOUR CORNER OF THE INTERNET</div>"
                "<div class='feed-title'>Today, lately.</div>",
                unsafe_allow_html=True,
            )

        with action:
            if st.button("＋ Post", type="primary", use_container_width=True):
                st.session_state.page = "Share a moment"
                st.rerun()

        st.markdown(
            "<div class='feed-subtitle'>"
            "A few things from your day, all in one place."
            "</div>",
            unsafe_allow_html=True,
        )

        response = api_request("GET", "/feed")

        if response is None:
            return

        if response.status_code != 200:
            st.error(error_message(response, "Couldn't load the feed."))
            return

        posts = response.json().get("posts", [])

        if not posts:
            st.markdown(
                "<div class='empty-state'>"
                "<div class='empty-title'>Nothing here just yet.</div>"
                "<div class='empty-copy'>"
                "Post a little moment from your day to get things going."
                "</div></div>",
                unsafe_allow_html=True,
            )

            if st.button(
                "Share your first moment",
                type="primary",
                use_container_width=True,
            ):
                st.session_state.page = "Share a moment"
                st.rerun()

            return

        for index, post in enumerate(posts):
            render_post(post, index)