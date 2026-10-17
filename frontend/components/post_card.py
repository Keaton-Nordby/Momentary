
import streamlit as st

from services.api import api_request, error_message
from utils.formatting import initials, format_date
from utils.images import create_transformed_url


def render_post(post, index):
    post_id = post.get("id", f"post-{index}")
    caption = post.get("caption") or ""
    email = post.get("email") or "Momentary member"
    media_url = post.get("url", "")
    file_type = (post.get("file_type") or "image").lower()

    st.markdown("<div class='post-shell'>", unsafe_allow_html=True)

    header, action = st.columns([6, 1], vertical_alignment="center")

    with header:
        st.markdown(
            f"""
            <div class="post-header">
                <div class="avatar">{initials(email)}</div>
                <div>
                    <div class="post-name">{email}</div>
                    <div class="post-date">
                        {format_date(post.get("created_at"))}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with action:
        if post.get("is_owner", False):
            if st.button("Delete", key=f"delete_{post_id}"):
                response = api_request("DELETE", f"/posts/{post_id}")

                if response is not None:
                    if response.status_code == 200:
                        st.rerun()
                    else:
                        st.error(error_message(response, "Delete failed."))

    if media_url:
        if file_type in [
            "video", "mp4", "mov", "avi", "webm", "mkv"
        ]:
            video_url = create_transformed_url(
                media_url,
                "w-1200,h-1000,cm-pad_resize,bg-101722",
            )
            st.video(video_url)
        else:
            image_url = create_transformed_url(
                media_url,
                "",
                caption or None,
            )
            st.image(image_url, use_container_width=True)

    if caption:
        st.markdown("<div class='post-caption'>", unsafe_allow_html=True)
        st.write(caption)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)