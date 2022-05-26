"""
    Usage: 
        python ./generate_massive_strings.py 10 5

    Args:
        1. # of lines to write
        2. # of GUIDs to concatenate per line

    Ideal for creating a wordlist of massive random strings, 
        suitable for scenarios where large brute-force/fuzzing payloads are necessary.
"""

import sys
import uuid


lines = int(sys.argv[1])
linelength = int(sys.argv[2])
i = 0
payload = ''

while i < lines:
    j = 0
    while j < linelength:
        # .hex returns the uuid, formatted w/o hyphens
        randomstring = uuid.uuid4().hex 
        payload = f'{payload}{randomstring}'
        j = j + 1
    payload = f'{payload}\n'
    print(i)
    i = i + 1

with open('payload.txt', 'at', encoding='utf-8') as f:
    f.write(f'{payload}')
    
print(f'Wrote {i}/{lines} requested lines with {j}/{linelength} concatenated UUIDs each.')
