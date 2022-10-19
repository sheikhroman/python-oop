numbers = [12,45,65,23,89,78,11]
try:
    numbers_iter= iter(numbers)
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("Explor iter")
    print(next(numbers_iter))
    print("Hello")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("world")
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print("iter stop")