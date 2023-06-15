'''Crie um jogo de Pedra, Papel, Tesoura.'''
import random
import emoji
from time import sleep

print(emoji.emojize('Seja bem-vindo ao jogo de pedra papel e tesoura\n Está preparado para disputar comigo? :smiling_face_with_horns: '))
sleep(1.0)

escolhas = ["Pedra", "Papel","Tesoura"]

dialogos_computador_vencer = ["KKKKKKKKKKKKK EU SOU MUITO BOMMMMM",
                              "VOCÊ JAMAIS IRÁ ME VENCER",
                              "EU SOU O MELHOR DO MUNDOOOOO",
                              "Ai ai muito facil",
                              "Esperava mais",
                              "VOCE NAO CANSA DE SER HORRIVEL ????",
                              "PREVISIVEL",
                              "TO CANSANDO DE GANHAR JÁ",
                              "NEM SEI O QUE DIZER, MUITO Fácil",
                              "PFF muito ruinzinho"]
escolha_dialogos_computador_vencer = random.choice(dialogos_computador_vencer)

dialogos_computador_perder = ["Você não é e nunca será pario para mim",
                              "Eu disse você só ganhou por sorte",
                              "HUM Acordei sem sorte hoje",
                              "Parece que temos um sortudo por aqui",
                              "COMO?? Jogo ladrão",
                              "PFF Até parece",
                              "AVA, sempre tem um mentiroso",
                              "Você nao passa de um sortudo",
                              "KKKKKKKK nunca,Nunca, NUNCAAAAAA",
                              "OK! Você ganhou"]
escolha_dialogos_computador_perder = random.choice(dialogos_computador_perder)

escolha_jogador = input('Escolha entre Pedra, Papel e Tesoura: ').capitalize()

escolha_computador = random.choice(escolhas)

#Empate
if escolha_jogador == escolha_computador :
    print(emoji.emojize('UoU! Nós empatamos kk :balloon::balloon:'))

# jogador vence

elif escolha_jogador == "Pedra":
    if escolha_computador == "Tesoura":
        print(emoji.emojize (f'{escolha_dialogos_computador_perder}:angry_face_with_horns::OK_hand:' ))

elif escolha_jogador =="Papel":
    if escolha_computador == "Pedra" :
        print(emoji.emojize(f'{escolha_dialogos_computador_perder}:angry_face_with_horns::OK_hand:'))

elif escolha_jogador == "Tesoura":
    if escolha_computador == "Papel":
        print(emoji.emojize(f'{escolha_dialogos_computador_perder}:angry_face_with_horns::OK_hand:'))

# Jogador perde
elif escolha_computador == "Papel":
    if escolha_jogador == "Pedra":
        print(emoji.emojize(f'{escolha_dialogos_computador_vencer}:smiling_face_with_horns::sign_of_the_horns:'))

elif escolha_computador == "Tesoura":
    if escolha_jogador == "Papel":
        print(emoji.emojize(f'{escolha_dialogos_computador_vencer}:smiling_face_with_horns::sign_of_the_horns:'))

elif escolha_computador == "Pedra":
    if escolha_jogador == "Tesoura":
        print(emoji.emojize(f'{escolha_dialogos_computador_vencer}:smiling_face_with_horns::sign_of_the_horns:'))

else:
    print('CARA Se você está com medo de perder nem abra o jogo, portanto escolha um opção válida. OBG')