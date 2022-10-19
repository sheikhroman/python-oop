largest = max(45,89,54,116,-12)
# print(largest)

nums = {2,5,56,78,34,67,90}
big_nums=max(nums)
# print(big_nums)

numbers = [12,45,65,23,89,78,11]
numbers_rev = reversed(numbers)
# print(list(numbers_rev))

# sorted_numbers= sorted(numbers)
sorted_numbers= sorted(numbers, reverse=True)
# print(sorted_numbers)

actors = [
    {'name': 'Sakib Khan', 'age': 38},
    {'name': 'Salman Khan', 'age': 54},
    {'name': 'Sharukh Khan', 'age': 52},
    {'name': 'Solaimon Khan', 'age': 23},
    {'name': 'Bappi Khan', 'age': 29},
]
sorted_actors= sorted(actors, key= lambda actor:actor['age'], reverse=True)
# sorted_actors= sorted(actors, key= lambda actor:actor['age'])
# print(sorted_actors)

friends = ['kabli','doubl','mosha', 'badol','noman']
sorted_friends= sorted(friends)
print(sorted_friends)
