"""
Create JWS in Python, based on claims derived from a valid token unpacked in jwt.io. 
Test JWT signature validation.
"""

import jwt


signing_algorithm = 'RS256' #'none'
key = bytes("", "utf-8"); 

# some claims in this payload represent those issued by Azure Active Directory
payload = {
  "aud": "",
  "iss": "",
  "iat": 1642440657,
  "nbf": 1642440657,
  "exp": 1642444557,
  "aio": "",
  "appid": "",
  "appidacr": "",
  "idp": "",
  "oid": "",
  "rh": "",
  "sub": "",
  "tid": "",
  "uti": "",
  "ver": "1.0"
}

# encode the payload as JSON Web Signature
jws = jwt.encode(payload, key, algorithm=signing_algorithm)
print(f'Encoded result:\r\n\n\t{jws}\r\n')

# try decoding the payload previously encoded
print(f'Decoding result:\r\n')
try: 
  decoded_jwt = jwt.decode(jws, key, algorithms=[signing_algorithm])
  print(f'Decoded payload: {decoded_jwt}\r\n')
except jwt.exceptions.InvalidSignatureError:
  print('\tSignature verification failed.\r\n')
