# print odd numbers 13 -> 39
start, end = 13, 39
 
for num in range(start, end + 1):
     
    if num % 2 != 0:
        print(num, end = " ")