import re

def clean_string(text):
    new=""
    text = re.split(r"[:|,|-|.|;|-]", text)
    for word in text:
        if word != '':
            new += word
            # print(word,end='')
    return new
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"    

output = clean_string(s)
print(output)