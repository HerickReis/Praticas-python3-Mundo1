'''Faça um programa que recebe dois números e verifica qual deles é o maior.'''
n = int(input('digite um numero: '))
n2 = int(input('Digite outro número: '))
if n > n2:
    print(f'{n} é maior que {n2}')
if n == n2:
    print('Os dois números são iguais')
if n2 > n :
    print(f'{n2} é maior que {n}')