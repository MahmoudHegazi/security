# security

# encode jwt

https://pyjwt.readthedocs.io/en/stable/

1- when you provide a secret directly, not encoded example ('secret') will not work

2- provide an encoded secret

``` 
d_string = 'secret'
data_bytes = d_string.encode("utf-8")
encoded_secret = base64.b64encode(data_bytes)  [c2VjcmV0]
code = jwt.encode({'sub':'AccountNUmber.QTVR','nbf':'1501594247','exp':'1501860089', 'iss': 'client_id', 'aud': 'https://login.google.com/oauth'},
                  base64.b64decode('c2VjcmV0'), algorithm='HS256')

```
