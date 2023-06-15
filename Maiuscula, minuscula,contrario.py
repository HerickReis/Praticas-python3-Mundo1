'''Crie um programa em Python que receba uma palavra do usuário e realize as seguintes tarefas:

--> Imprima a palavra em letras maiúsculas;
--> Imprima a palavra em letras minúsculas;
--> Imprima o número de caracteres da palavra;
--> Imprima a palavra invertida.'''
palavra = str(input('Digite uma frase qualquer: ')).strip().capitalize()
print(f'Sua frase em letra maiúsculas\n{palavra.upper()}')
print(f'Sua frase em letras minúsculas\n{palavra . lower()}')
print(f'Sua frase possui {len(palavra)} caracters contando espaços')
print(f'Sua frase possui {len(palavra)} caracters sem contar espaços')
print(f'{palavra[::-1]}')