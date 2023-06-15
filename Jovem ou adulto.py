'''Escreva um programa que peça ao usuário para digitar seu nome e idade. Em seguida, exiba uma mensagem de saudação que inclua o nome e idade do usuário. 
Se o usuário tiver menos de 18 anos, a mensagem deve incluir a palavra "jovem". Caso contrário, a mensagem deve incluir a palavra "adulto".'''
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
print (f'Olá {nome} você tem {idade} anos')
if idade <= 18 :
    print('Você é jovem ')
else :
    print('você é adulto') 