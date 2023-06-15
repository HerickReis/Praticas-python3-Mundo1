'''Crie um programa que solicite ao usuário que insira uma frase e, em seguida, realize as seguintes tarefas:
Conte o número de caracteres na frase (incluindo espaços em branco).
Conte o número de palavras na frase.
Conte quantas vezes uma determinada letra ou conjunto de letras aparece na frase.
Substitua uma palavra na frase por outra palavra especificada pelo usuário.'''
frase = str(input('Digite uma frase qualquer: ')).strip().lower()

if not  frase :
    print('Você precisa digitar uma frase!')

    exit()

contagem = len(frase)

print(f'A frase ({frase}) contém {contagem} letras ao todo.')

palavras = frase.split()

print(f'a frase possui {len(palavras)} palavras')

letras = input('Digite a letra ou conjunto de letras que deseja contar: ').lower()

letrass = frase.count(letras)

print(f'A frase ({frase.capitalize()}) possuí {letrass} letras "{letras}".')

pala_ant = input('Digite a palavra que quer substituir: ')

pala_nova = input('Digite a palavra nova: ')

subs = frase.replace(pala_ant , pala_nova)

print(f'a frase com a palavra sbustituída ficou {subs}.')