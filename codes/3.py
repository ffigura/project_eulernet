# -*- coding: utf-8 -*-
"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
n = 600851475143  
n0 = n
list = []

while n % 2 == 0:
    n = n / 2
    list.append(2)
    
for i in range(3,n0,2):
    if n == 1:
        break
    while n % i == 0:
        n = n / i
        list.append(i)
    
print('prime factors =',list)
