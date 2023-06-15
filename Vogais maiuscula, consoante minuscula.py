'''Crie uma função que receba uma string como entrada e retorne a mesma string, mas com todas as vogais maiúsculas e todas as consoantes minúsculas.'''
'''palavra= input('Digite uma frase: ')
vogais = "AEIOUaeiou"
if vogais in palavra:
    resultado = vogais.upper()
    print(resultado)'''
string = input('Digite uma frase')
vogais = "AEIOUaeiou"

resultado = ""
for letra in string:
    if letra in vogais:
        resultado += letra.upper()
    else:
        resultado += letra.lower()

print(resultado)
