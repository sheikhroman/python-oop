""" 
Chat Bot 
steps:
1 -> input/lisent
2 -> process/decide
3 -> output/talkback

"""
greet_words = ['hi','hello','yo','hey']
bye_words=['bye','tata','get out']
bad_words=['dog','pocha']

def lisent():
    return input('Say somthing: ')

def decide(command):
    # print(command)
    command=command.lower()
    broken_words=command.split(" ")
    # print(broken_words)
    for word in broken_words:
        if word in greet_words:
            talkback("Hey bro")
            return

        elif word in bye_words:
            talkback("Ok bye")
            return
        elif word in bad_words:
            talkback("you too")
            return

def talkback(response):
    print(response)



while True:
    command = lisent()
    decide(command)