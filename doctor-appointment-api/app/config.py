import os

# Secret key for JWT tokens
SECRET_KEY = os.getenv("SECRET_KEY", "abcdefghijklmnopq")

# Algorithm for JWT
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Token expiration time (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

