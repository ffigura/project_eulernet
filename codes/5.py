# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
 numbers from 1 to 20?

"""

'''
# this is the brute forcing, go horse
flag = False
n = 2520
while n > 0:
    cont = 0
    for i in range(1,21):
        if n % i == 0:
            cont = cont + 1
            if cont == 20:
                print('smallest positive number =',n)
                flag = True
                break
        else:
            break
    if flag: break
    n = n + 1
'''

'''
This is super fast!

1 - there is no need to start from 1 since it divides every number
2 - there is no need to use 2, 4, 5 and 10 if we use 20
3 - there is no need to use 3, 6 and 9 if we use 18
4 - there is no need to use 8 if we use 16, and 7 if we use 14
5 - start with 2520 because this is in the title
6 - increment every 20 because the answer must be divisible by 20
'''

numbers = [11,12,13,14,15,16,17,18,19,20]

for num in range(2520, 999999999, 20):
        if all(num % n == 0 for n in numbers):
            break

print('smallest positive number =',num)