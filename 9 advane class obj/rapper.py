# def do_something(x,y):
#     print(f'x:{x} y:{y}')

# do_something(12,45)
# do_something('Tomato','Onion')

def do_something(work):
    print('start work')
    # print(type(work))
    work()
    print('done with work')

def practice_coding():
    print('I am practicing Python')

def learning_coding():
    print('Leaning Python Class')

do_something(practice_coding)
do_something(learning_coding)