# Import the Python Library
import sys
# !{sys.executable} -m pip install bcrypt
import bcrypt
password = b"studyhard"
salt = bcrypt.gensalt(14)
hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)
bcrypt.checkpw(password, hashed)
