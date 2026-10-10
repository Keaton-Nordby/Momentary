
import streamlit as st

from components.upload_form import render_upload_form
from services.api import api_request, error_message


def upload_page():
    _, content, _ = st.columns([1, 2, 1], gap="small")

    with content:
        st.markdown(
            "<div class='eyebrow'>SAVE A LITTLE OF TODAY</div>"
            "<div class='feed-title'>Share a moment.</div>"
            "<div class='feed-subtitle'>"
            "No big caption needed. Just post what you're up to."
            "</div>",
            unsafe_allow_html=True,
        )

        uploaded_file, caption = render_upload_form()

        if uploaded_file is not None:
            if uploaded_file.type.startswith("image/"):
                st.image(uploaded_file, use_container_width=True)
            elif uploaded_file.type.startswith("video/"):
                st.video(uploaded_file)

            if caption.strip():
                st.caption(caption.strip())

        share, cancel = st.columns([2, 1])

        with share:
            if st.button(
                "Share moment",
                type="primary",
                use_container_width=True,
            ):
                if uploaded_file is None:
                    st.warning("Choose a photo or video first.")
                else:
                    with st.spinner("Posting your moment…"):
                        response = api_request(
                            "POST",
                            "/upload",
                            files={
                                "file": (
                                    uploaded_file.name,
                                    uploaded_file.getvalue(),
                                    uploaded_file.type,
                                )
                            },
                            data={"caption": caption},
                        )

                    if response is not None:
                        if response.status_code in (200, 201):
                            st.session_state.page = "Feed"
                            st.rerun()
                        else:
                            st.error(
                                error_message(response, "Upload failed.")
                            )

        with cancel:
            if st.button("Cancel", use_container_width=True):
                st.session_state.page = "Feed"
                st.rerun()