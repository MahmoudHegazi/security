# security

# encode jwt

https://pyjwt.readthedocs.io/en/stable/


2- provide an encoded secret

``` 
d_string = 'secret'
data_bytes = d_string.encode("utf-8")
encoded_secret = base64.b64encode(data_bytes)  [c2VjcmV0]
code = jwt.encode({'sub':'AccountNUmber.QTVR','nbf':'1501594247','exp':'1501860089', 'iss': 'client_id', 'aud': 'https://login.google.com/oauth'},
                  base64.b64decode('c2VjcmV0'), algorithm='HS256')

```

```
# encode_jwt payload
encoded_jwt = jwt.encode({"school": "udacity"}, "learning", algorithm="HS256")
print(encoded_jwt)
```

```
encoded_jwt = jwt.encode({"school": "udacity"}, "learning", algorithm="HS256")
print(encoded_jwt)
decoded_jwt = jwt.decode(encoded_jwt, "learning", verify=True)
print(decoded_jwt)
decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
print(decoded_base64)
```

# layer of secuirty in hash
1- hash password + dynamic slat
