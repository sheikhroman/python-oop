import pyjokes
from random import randrange

def tell_some_jokes():
    ques = input("Do you want to hear a joke? (y/n)\n>> ")
    ques = ques.lower()
    word = ["I hope you like this joke.", "Was not it great?", "This was hilarious!"]
    count = 0
    while ques == "y":
        print('\n"',pyjokes.get_joke(),'"\n')
        rand = randrange(0,3)

        if rand == count:
            print("-> hahaha Even the system is laughing at this joke!")

        while rand != count:
            print("->",word[rand])
            count = rand
        

        ques = input("Do you want to hear another jokes? (y/n)\n>> ")
        ques = ques.lower()

        if ques == "n":
            break

tell_some_jokes()

# pip install pyjokes