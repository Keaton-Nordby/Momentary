
import streamlit as st


def apply_theme():
    st.markdown(
        """
        <style>
        @import url(
          'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap'
        );

        :root {
            --bg: #0d1420;
            --surface: #141e2c;
            --surface-raised: #1b2839;
            --border: #2b3a4e;
            --text: #edf2f8;
            --muted: #9aa9bc;
            --accent: #8fb5e8;
        }

        .stApp {
            background:
                radial-gradient(
                    ellipse at 50% -20%,
                    rgba(75, 112, 160, .15),
                    transparent 48%
                ),
                var(--bg);
            color: var(--text);
            font-family: 'DM Sans', sans-serif;
        }

        [data-testid="stHeader"] {
            background: rgba(13, 20, 32, .85);
            backdrop-filter: blur(14px);
        }

        [data-testid="stSidebar"] {
            background: #101a28;
            border-right: 1px solid var(--border);
        }

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3, h4 {
            font-family: 'Manrope', sans-serif !important;
            color: var(--text);
            letter-spacing: -.5px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 11px;
            margin-bottom: 28px;
        }

        .brand-icon {
            width: 40px;
            height: 40px;
            border-radius: 13px;
            background: #263c56;
            color: #d9e7f8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }

        .brand-title {
            font-family: 'Manrope', sans-serif;
            font-size: 19px;
            font-weight: 800;
            color: var(--text);
        }

        .brand-subtitle {
            font-size: 10px;
            color: var(--muted);
        }

        .user-card {
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 13px;
            border: 1px solid var(--border);
            border-radius: 14px;
            background: rgba(255,255,255,.025);
            margin: 14px 0 24px;
            overflow-wrap: anywhere;
        }

        .avatar {
            flex: 0 0 38px;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: #2d425c;
            color: #e1ecfa;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
        }

        .user-card-email {
            color: var(--muted);
            font-size: 11px;
            overflow-wrap: anywhere;
        }

        .sidebar-footnote {
            color: #8293a9;
            font-size: 12px;
            line-height: 1.8;
            padding: 15px 8px;
        }

        .eyebrow {
            color: var(--accent);
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.7px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .feed-title {
            font-family: 'Manrope', sans-serif;
            font-size: clamp(28px, 4vw, 38px);
            line-height: 1.12;
            font-weight: 800;
            letter-spacing: -1.3px;
            margin-bottom: 7px;
        }

        .feed-subtitle {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.65;
            margin-bottom: 22px;
        }

        .post-shell {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 17px;
            padding: 15px;
            margin-bottom: 18px;
            overflow: hidden;
        }

        .post-header {
            display: flex;
            align-items: center;
            gap: 10px;
            padding-bottom: 13px;
        }

        .post-name {
            font-size: 13px;
            font-weight: 700;
            overflow-wrap: anywhere;
        }

        .post-date {
            color: var(--muted);
            font-size: 11px;
            margin-top: 3px;
        }

        .post-caption {
            color: #e0e7f0;
            font-size: 14px;
            line-height: 1.7;
            padding: 12px 2px 3px;
            overflow-wrap: anywhere;
        }

        .empty-state {
            text-align: center;
            padding: 45px 20px;
            border: 1px solid var(--border);
            border-radius: 17px;
            background: var(--surface);
            margin: 10px 0 15px;
        }

        .empty-title {
            font-family: 'Manrope', sans-serif;
            font-weight: 800;
            font-size: 21px;
        }

        .empty-copy {
            color: var(--muted);
            font-size: 13px;
            margin-top: 7px;
        }

        .auth-panel {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 28px;
        }

        .auth-heading {
            font-family: 'Manrope', sans-serif;
            font-size: 27px;
            font-weight: 800;
        }

        .auth-subheading {
            color: var(--muted);
            font-size: 13px;
            margin: 7px 0 22px;
        }

        .login-title {
            font-family: 'Manrope', sans-serif;
            font-size: clamp(34px, 4.5vw, 55px);
            font-weight: 800;
            line-height: 1.08;
            letter-spacing: -2px;
        }

        .login-title span {
            color: var(--accent);
        }

        .login-copy {
            max-width: 420px;
            color: var(--muted);
            font-size: 15px;
            line-height: 1.8;
            margin-top: 15px;
        }

        .stTextInput input,
        .stTextArea textarea {
            background: #101a28 !important;
            color: var(--text) !important;
            border: 1px solid #314258 !important;
            border-radius: 11px !important;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus {
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 1px var(--accent) !important;
        }

        .stButton > button {
            min-height: 42px;
            border-radius: 11px;
            border: 1px solid #34465d;
            background: #1b293a;
            color: var(--text);
            font-weight: 600;
        }

        .stButton > button:hover {
            border-color: var(--accent);
            color: #b0cdf2;
            background: #22344a;
        }

        .stButton > button[kind="primary"] {
            background: #8fb5e8 !important;
            color: #101a28 !important;
            border-color: #8fb5e8 !important;
            font-weight: 700 !important;
        }

        [data-testid="stFileUploader"] {
            background: var(--surface);
            border: 1px dashed #425671;
            border-radius: 14px;
            padding: 9px;
        }

        [data-testid="stImage"] img,
        [data-testid="stVideo"] video {
            border-radius: 12px;
        }

        [data-testid="stAlert"] {
            border-radius: 11px;
        }

        #MainMenu, footer {
            visibility: hidden;
        }

        @media (max-width: 700px) {
            .block-container {
                padding: 1rem 1rem 2rem;
            }

            .post-shell {
                padding: 10px;
                border-radius: 14px;
            }

            .auth-panel {
                padding: 20px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )