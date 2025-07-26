from passlib.context import CryptContext

# bcrypt with automatic salts
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)
