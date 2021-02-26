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
1. hash password + dynamic salat
2. store salat in diffrent table make the forgien key userid + number (best select number from hashed password to add it) make it the first number in hashed as index)
3. store the salat in diffrent database , and best is to store the forgein key in another table even the developer may not get the correct pass :D
4. only problem if it read the server file itself 
5. as i said to protect submiting the hash valdaite first if submited password == hashed password before hash(post.password) == stored password
6. this make it check if password submited was hashed which should not known by user
7. hash with key  + the salt + encrypted forigen for salat + 3 database tables  in 3 diffrent servers are most secured way


# get user info

https://auth0.com/docs/flows/add-login-auth-code-flow

1.  get the code not token
2.  send request to get the token with that code it will include the data
