import emoji
import random
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

#Jogador vence
if escolha_jogador == "Pedra" and escolha_computador == "Tesoura":
    print(emoji.emojize(f'{escolha_dialogos_computador_perder}:angry_face_with_horns::OK_hand:'))

elif escolha_jogador =="Papel" and escolha_computador == "Pedra":
    print(emoji.emojize(f'{escolha_dialogos_computador_perder}:angry_face_with_horns::OK_hand:'))

elif escolha_jogador == "Tesoura" and escolha_computador == "Papel":
    print(emoji.emojize(f'{escolha_dialogos_computador_perder}:angry_face_with_horns::OK_hand:'))

# Jogador perde
elif escolha_computador == "Papel" and escolha_jogador == "Pedra":
    print(emoji.emojize(f'{escolha_dialogos_computador_vencer}:smiling_face_with_horns::sign_of_the_horns:'))

elif escolha_computador == "Tesoura" and escolha_jogador == "Papel":
    print(emoji.emojize(f'{escolha_dialogos_computador_vencer}:smiling_face_with_horns::sign_of_the_horns:'))

elif escolha_computador == "Pedra" and escolha_jogador == "Tesoura":
    print(emoji.emojize(f'{escolha_dialogos_computador_vencer}:smiling_face_with_horns::sign_of_the_horns:'))

# Empate
else:
    print(emoji.emojize('UoU! Nós empatamos kk :balloon::balloon:'))
