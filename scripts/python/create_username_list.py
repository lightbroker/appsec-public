"""
    Usage: python create_username_list.py "sampleUser" 200

    Appends incrementing numeric values to a given base username.
    Writes one username per line, ideal for use in Burp Intruder.
"""

import sys


base_username = sys.argv[1]
lines = int(sys.argv[2])
i = 0
payload = f'{base_username}'

while i < lines:
    next_username = f'{base_username}{i}'
    payload = f'{payload}{next_username}\n'
    i = i + 1

with open(f'username_list_{base_username}_{lines}.txt', 'w+', encoding='utf-8') as f:
    print(payload)
    f.write(f'{payload}')
    
print(f'done')
