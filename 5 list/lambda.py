# def squre(x):
#     return x * x

squre =lambda x:x*x

result = squre(6)
# print(result)

add =lambda x,y:x+y
sum=add(45,55)
# print(sum)

numbers = [12,45,65,23,89,78,11]
def double_it(x):
    return x*2

double_it2 = lambda x:x*2
# doubled_numbers = map(double_it, numbers)
doubled_numbers = map(lambda x: x*2, numbers)
# print(numbers)
# print(list(doubled_numbers))
squre_numbers = map(lambda x: x*x, numbers)
# print(list(doubled_numbers))



#    Filter
bigger_numbers = filter(lambda num:num>50, numbers)
# print(numbers)
# print(list(bigger_numbers))


actors = [
    {'name': 'sakib','age': 42},
    {'name': 'manna','age': 54},
    {'name': 'popy','age': 49},
    {'name': 'purnima','age': 60},
    ]
senior_artists= filter(lambda actor: actor['age']> 50, actors)
# print(list(senior_artists))
