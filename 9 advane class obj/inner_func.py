def do_something():
    print('Inside the function do_something')
    def inner_function():
        print('Inside the inner function')
    inner_function()
# do_something()

def first_function():
    print('Inside the first function')
    def second_function():
        print('Inside the inner function')
    return second_function    

first= first_function() 
first()