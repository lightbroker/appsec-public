# Usage: ./create_bruteforce_credentials_lists.py source_usernames.txt source_passwds.txt valid_username valid_password

import re
import sys

source_usernames_file = sys.argv[1]
source_passwords_file = sys.argv[2]
valid_username = sys.argv[3]
valid_password = sys.argv[4]
target_usernames_filename = 'brute_force_usernames.txt'
target_passwords_filename = 'brute_force_passwords.txt'

# init
source_usernames_list = []
source_passwords_list = []
count = 0 
total_usernames_written = 0
total_passwords_written = 0

# get and assign existing usernames wordlist
with open(source_usernames_file, 'r') as source_usernames:
    source_usernames_list = source_usernames.readlines()

# get and assign existing passwords wordlist
with open(source_passwords_file, 'r') as source_passwords:
    source_passwords_list = source_passwords.readlines()

source_usernames_length = len(source_usernames_list)
source_passwords_length = len(source_passwords_list)
loop_limit = min(source_usernames_length, source_passwords_length)

# create username file, if doesn't exist
# (w+: Create the file if it does not exist and then open it in write mode.)
with open(target_usernames_filename, 'w+', encoding='utf-8') as target_usernames_file:
    for username in source_usernames_list:
        if total_usernames_written == loop_limit:
            break
        count += 1
        if count % 2 == 1:
            username = re.sub('\s+', '', username)
            target_usernames_file.write(f'{username}\n')
        else:
            valid_username = re.sub('\s+', '', valid_username)
            target_usernames_file.write(f'{valid_username}\n')
        total_usernames_written += 1

# reset counter
count = 0

# create passwords file, if doesn't exist
with open(target_passwords_filename, 'w+', encoding='utf-8') as target_passwords_file:
    for password in source_passwords_list:
        if total_passwords_written == loop_limit:
            break
        count += 1
        if count % 2 == 1:
            password = re.sub('\s+', '', password)
            target_passwords_file.write(f'{password}\n')
        else:
            valid_password = re.sub('\s+', '', valid_password)
            target_passwords_file.write(f'{valid_password}\n')
        total_passwords_written += 1

# args: valid creds every x rotation
# define valid credentials
# pull from username wordlist
# while dictionary has entries, insert into list and alternate between text files: 1.) usernames, 2.) passwords
