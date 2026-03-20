from sqlalchemy.orm import Session
from app.models import User

# ===============================
# BAD WORD LIST (extendable)
# ===============================
BAD_WORDS = [
    "idiot",
    "stupid",
    "hate",
    "fool",
    "damn",
    "shit"
]


# ===============================
# CHECK BAD WORD
# ===============================
def contains_bad_word(message: str) -> bool:
    message = message.lower()
    for word in BAD_WORDS:
        if word in message:
            return True
    return False


# ===============================
# HANDLE WARNING & BLOCK LOGIC
# ===============================
def handle_bad_word(
    user: User,
    message: str,
    db: Session
):
    """
    Returns:
    - None → clean message
    - dict → warning or block response
    """

    if not contains_bad_word(message):
        return None

    # increment warning count safely; cast to int to avoid ColumnElement issues
    current = int(user.warning_count or 0)  # type: ignore
    user.warning_count = current + 1  # type: ignore

    # 🚫 3rd violation → BLOCK
    if int(user.warning_count) >= 3:  # type: ignore
        user.is_blocked = True  # type: ignore
        db.commit()
        return {
            "type": "block",
            "message": "🚫 You are blocked due to repeated policy violations."
        }

    db.commit()

    return {
        "type": "warning",
        "message": f"⚠ Warning {user.warning_count}/2: Bad language detected."
    }
