
from datetime import datetime


def initials(email):
    return email.strip()[0].upper() if email else "M"


def format_date(value):
    if not value:
        return "A moment ago"

    try:
        return datetime.fromisoformat(
            value.replace("Z", "+00:00")
        ).strftime("%b %d, %Y")

    except (ValueError, TypeError, AttributeError):
        return str(value)[:10]