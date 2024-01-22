import math, os

file = open('rosalind_ini5.txt', 'r')
file_evens = open('file_evens.txt', 'w+')

for num, line in enumerate(file, 1):
    if num % 2 == 0:
        print(line)
        
        file_evens.write(line)
