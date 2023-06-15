'''Escreva um programa que peça ao usuário para digitar uma palavra. Em seguida, verifique se a palavra é um palíndromo (ou seja, se ela é igual quando lida de trás para frente). 
Se a palavra for um palíndromo, exiba uma mensagem informando que a palavra é um palíndromo. Caso contrário, exiba uma mensagem informando que a palavra não é um palíndromo.'''
from time import sleep
cores = { "limpa" : '\033[m',
         "vermelho" : '\033[34m',
        "verde" : '\033[33m',
        "ciano" : '\033[36m'
}
palavra = str(input('Escreva um palavra: '))
palindromo = palavra[::-1]
print(f'{cores["ciano"]}identificando...m {cores["limpa"]}') 
sleep(1.2)

if palindromo == palavra :
    print(f' {cores["verde"]}{palavra.capitalize()} é um palíndromo :D {cores["limpa"]}') 
else: 
    print(f'{cores["vermelho"]} {palavra.capitalize()}   Não é um palíndromo D: {cores["limpa"]}')