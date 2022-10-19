""" 
 Encrypt and Decrypt
"""

data ="firebaby"
shift = 5
output=''
for character in data:
    output+=  chr((ord(character)+shift-97)% 26+97)
print(output)