'''Escreva um programa que solicite ao usuário que digite dois números e exiba qual é o maior número.'''
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if not numero_2 or not  numero_1:
    numero_1 = 0
    numero_2 = 0

if numero_1 >= numero_2 :
    print(f'{numero_1} é maior que {numero_2}.')

else :
    if numero_2 >= numero_2 :
        print(f'{numero_2} é maior que {numero_1}.')

    else :
        print('Os dois valores são iguais.')

if not numero_2 and not numero_1 :
    print('Não há vlaores para comparação.')


    
else:
    if not numero_1 :
        print('Não há valores suficientes para comparação.')

    else:
        if not numero_2 :
            print('Não há valores suficientes para comparação.')