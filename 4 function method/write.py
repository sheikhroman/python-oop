# with open('massage.txt','a') as fileWrite:
#     fileWrite.write('Python')

with open('massage.txt','r') as fileRead:
    text = fileRead.read()
    print(text)