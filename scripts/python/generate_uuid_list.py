import sys
import uuid


count = int(sys.argv[1])
i = 0 
payload = ''

while i < count:
    guid = uuid.uuid4()
    # uncomment to eliminate hyphens
    # guid = guid.hex
    payload = f'{payload}{guid}\n'
    print(i)
    i = i + 1

with open('guid_list.txt', 'w+', encoding='utf-8') as guid_file:
    guid_file.write(payload)
    
