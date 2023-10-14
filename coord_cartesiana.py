#!/usr/bin/python3

import math
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))

c1 = (math.sqrt(((a - b)**2) + ((c - d)**2)))
print(c1)

if c1 >= 10:
    print('longe')
elif c1 <=10:
    print('perto')
