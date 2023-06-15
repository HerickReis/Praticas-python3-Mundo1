'''Faça um programa que recebe a idade de uma pessoa e verifica se ela pode dirigir ou não.'''
from time import sleep
idade = int(input('Quantos Anos você tem? '))
print('Analisando...')
sleep(0.8)
if idade >= 18 :
    print(f'Ok você tem {idade} anos e pode dirigir :D')
else :
    print(f'Você tem {idade} anos e ainda não pode dirigir :(')