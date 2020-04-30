# -*- coding: utf-8 -*-
"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

import numpy as np

a=1
b=2
aux=a+b
even=[2]

while (aux<=4000000):
    aux=a+b
    if np.mod(aux,2)==0:
        even.append(aux)
    a=b
    b=aux

print (np.sum(even))