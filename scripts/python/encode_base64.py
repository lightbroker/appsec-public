import base64


user_input = input('enter value to base64 encode: ')
print(base64.b64encode(str.encode(user_input)))
