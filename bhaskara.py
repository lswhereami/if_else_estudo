#!/usr/bin/env python3
import math

a = float(input('digite o valor de A na equação de bhaskara:'))
b= float(input('digite o valor de B na equação de bhaskara:'))
c = float(input('digite o valor de C na equação de bhaskara:'))

d = (b ** 2 - 4 * a * c)


if d == 0:
    x_bhas = (-a + math.sqrt(d)) / (2 * a)
    print('a raiz desta equação é',x_bhas)
else:
    if d <0:
        print('esta equação não possui raízes reais')
    else:
        x_bhas = (-b + math.sqrt(d)) / (2 * a)
        y_bhas = (-b - math.sqrt(d)) / (2 * a)

print('raiz 1:', x_bhas, 'raiz 2:', y_bhas)
