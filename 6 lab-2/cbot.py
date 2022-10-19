""" 
Chat Bot 
steps:
1 -> input/lisent
2 -> process/decide
3 -> output/talkback

"""
greet_words = ['hi','hello','yo']
bye_words=['bye','tata','get out']

def lisent():
    return input('Say somthing: ')

def decide(command):
    print(command)
    broken_words=command.split(" ")
    print(broken_words)
def talkback():
    pass
