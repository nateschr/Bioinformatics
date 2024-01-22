import math

a = 4621
b = 9586
total = 0

for i in range(a, b):
    if not i % 2 == 0:
        print(i)
        total += i

print('\n', 'Sum of all odd integers is:', total)
