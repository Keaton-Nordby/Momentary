
import requests
import streamlit as st

import os

API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000"
).rstrip("/")


def get_headers():
    token = st.session_state.get("token")

    if token:
        return {"Authorization": f"Bearer {token}"}

    return {}


def api_request(method, path, **kwargs):
    try:
        extra_headers = kwargs.pop("headers", {})

        return requests.request(
            method,
            f"{API_URL}{path}",
            headers={**get_headers(), **extra_headers},
            timeout=20,
            **kwargs,
        )

    except requests.RequestException:
        st.error(
            "Couldn't connect to the backend. "
            "Make sure FastAPI is running at http://localhost:8000."
        )
        return None


def error_message(response, fallback):
    try:
        return str(response.json().get("detail", fallback))
    except (ValueError, AttributeError):
        return fallback