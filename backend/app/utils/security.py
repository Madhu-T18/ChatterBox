from passlib.context import CryptContext

# ===============================
# PASSWORD HASH CONFIG
# ===============================
# include pbkdf2_sha256 as primary scheme to avoid bcrypt initialization bug
# on some platforms; bcrypt remains for backwards-compatibility when
# verifying older hashes.
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256", "bcrypt"],
    deprecated="auto"
)

# ===============================
# HASH PASSWORD
# ===============================
def hash_password(password: str) -> str:
    """Hash a plaintext password.

    We wrap pwd_context.hash in a try/except so that if the bcrypt backend
    initialization ever throws (as it did on Windows with certain
    ``bcrypt`` versions), we can fall back to pbkdf2_sha256 directly instead
    of crashing the entire request stack.
    """
    try:
        return pwd_context.hash(password)
    except ValueError:
        # Likely a bcrypt backend bug; fall back to a fresh context using
        # pbkdf2_sha256 only. This should be rare and only occur during
        # startup/first-hash calls.
        return CryptContext(schemes=["pbkdf2_sha256"]).hash(password)

# ===============================
# VERIFY PASSWORD
# ===============================
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
