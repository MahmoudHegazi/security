
from cryptography.fernet import Fernet
key = Fernet.generate_key()
# pass key to class
f = Fernet(key)
# encrypt
plaintext = b"my week password"
encrptedmessage = f.encrypt(plaintext)
# print(encrptedmessage)

# decrypt the encrypted message
decrptyedmessage = f.decrypt(encrptedmessage)
password_tovalidate = decrptyedmessage.decode("utf-8")
print(password_tovalidate)
