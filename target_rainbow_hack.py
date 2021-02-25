# do not forget to get the list of noob password
# this hack with target admin

# Load the NIST list of 10,000 most commonly used passwords
with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')
    

# The following data is a normalized simplified user table
# Imagine this information was stolen or leaked
leaked_users_table = {
    'jamie': {
        'username': 'jamie',
        'role': 'subscriber',
        'md5': '203ad5ffa1d7c650ad681fdff3965cd2'
    }, 
    'amanda': {
        'username': 'amanda',
        'role': 'administrator',
        'md5': '315eb115d98fcbad39ffc5edebd669c9'
    }, 
    'chiaki': {
        'username': 'chiaki',
        'role': 'subscriber',
        'md5': '941c76b34f8687e46af0d94c167d1403'
    }, 
    'viraj': {
        'username': 'viraj',
        'role': 'employee',
        'md5': '319f4d26e3c536b5dd871bb2c52e3178'
    },
}

# import the hashlib
import hashlib
import time
# example hash
list_of_rainbow = []
valid_users = []
# sample = {'hashed':'password'}
word = 'blueberry'
# hashlib.md5(word.encode()).hexdigest()
counter = 0
def hack():
    for easy_pass in nist_bad:
        hashed = hashlib.md5(easy_pass.encode()).hexdigest()
        list_of_rainbow.append({'role':'','user':'','hashed':hashed,'pass':easy_pass})
    print('hashed complete')
    print('next step')
    for i in leaked_users_table:
        hashed_hacked = leaked_users_table[i]['md5']
        noobuser = leaked_users_table[i]['username']
        target_admin = leaked_users_table[i]['role']
        for checker in list_of_rainbow:
            if target_admin != 'administrator':
                continue
            if checker['hashed'] == hashed_hacked:
                checker['user'] = noobuser
                checker['role'] = target_admin
                print('i hacked admin user HHHH %s ' % checker['user'])
                valid_users.append(checker)
    print(valid_users)
    if len(valid_users) == 0:
        print('we did nothing')
hack()
