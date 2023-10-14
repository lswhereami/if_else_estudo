#!/usr/bin/python3
import math

a = float(input('digite o valor de a na equação de bhaskara:'))
b= float(input('digite o valor de b na equação de bhaskara:'))
c = float(input('digite o valor de c na equação de bhaskara:'))

d = (b ** 2 - 4 * a * c)


if d >=0:
    y_bhas = (-b + math.sqrt(d)) / (2 * a)
    x_bhas = (-b - math.sqrt(d)) / (2 * a)
    if d == 0:
        print('a raiz desta equação é',y_bhas)
    if y_bhas > x_bhas:
        print('as raízes da equação são',y_bhas, 'e', x_bhas)
    if x_bhas > y_bhas:
        print('as raizes da equação são',x_bhas,'e',y_bhas)
else:
    if d <0:
        print('esta equação não possui raízes reais')
