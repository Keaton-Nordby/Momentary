
import streamlit as st

from services.api import api_request, error_message
from services.auth import PROFILE_PATH


def login_page():
    left, right = st.columns([1, 1], gap="large")

    with left:
        st.markdown(
            "<div class='eyebrow'>A SMALL SPACE FOR REAL LIFE</div>"
            "<div class='login-title'>Life happens.<br>"
            "<span>Keep a little of it.</span></div>"
            "<div class='login-copy'>"
            "A photo, a quick thought, a moment from your day. "
            "Nothing to perfect. Just something to remember."
            "</div>",
            unsafe_allow_html=True,
        )

    with right:
        st.markdown("<div class='auth-panel'>", unsafe_allow_html=True)
        st.markdown(
            "<div class='auth-heading'>Welcome back</div>"
            "<div class='auth-subheading'>"
            "Sign in, then get back to your day."
            "</div>",
            unsafe_allow_html=True,
        )

        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Your password",
        )

        sign_in, create_account = st.columns(2)

        with sign_in:
            if st.button("Sign in", type="primary", use_container_width=True):
                if not email.strip() or not password:
                    st.warning("Enter your email and password.")
                else:
                    response = api_request(
                        "POST",
                        "/auth/jwt/login",
                        data={
                            "username": email.strip(),
                            "password": password,
                        },
                    )

                    if response is not None:
                        if response.status_code == 200:
                            st.session_state.token = response.json()["access_token"]

                            profile = api_request("GET", PROFILE_PATH)

                            if profile is not None and profile.status_code == 200:
                                st.session_state.user = profile.json()
                                st.rerun()
                            else:
                                st.session_state.token = None
                                st.error(
                                    "Login worked, but the profile couldn't load. "
                                    "Check PROFILE_PATH in services/auth.py."
                                )
                        else:
                            st.error(
                                "That email and password combination didn't work."
                            )

        with create_account:
            if st.button("Create account", use_container_width=True):
                if not email.strip() or not password:
                    st.warning("Enter an email and password first.")
                else:
                    response = api_request(
                        "POST",
                        "/auth/register",
                        json={
                            "email": email.strip(),
                            "password": password,
                        },
                    )

                    if response is not None:
                        if response.status_code in (200, 201):
                            st.success("Account created. You can sign in now.")
                        else:
                            st.error(
                                error_message(response, "Registration failed.")
                            )

        st.markdown("</div>", unsafe_allow_html=True)