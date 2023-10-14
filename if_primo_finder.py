#!/usr/bin/python3
primo = int(input('digite um numero:'))

if primo == 1:
    print('primo')
elif primo == 2:
    print('primo')
elif primo == 3:
    print('primo')
elif primo == 5:
    print('primo')
elif primo == 7:
    print('primo')
elif primo % 2 == 0:
    print('não primo')
elif primo % 3 == 0:
    print('não primo')
elif primo % 5 == 0:
    print('não primo')
elif primo % 7 == 0:
    print('não primo')
else:
    print('primo')
