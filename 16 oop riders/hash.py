import hashlib
""" 
Rtrams
smart
Splkiyonar
lion
"""

email = 'jr@gmail.com'
pwd = 'Chairmainbeth'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = 'jr@gmail.com'
your_password = 'Chairmainbeth'

hased_your_password = hashlib.md5(your_password.encode()).hexdigest()
if email == your_email and pwd_hash == hased_your_password:
    print('Right user')
else:
    print('Wrong password')

hacker_email = 'jr@gmail.com'
hacker_password = '2af92a87e089115d757a816b118135a3'

print(pwd)
print(pwd_hash)