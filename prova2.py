import random

dados = [1, 2, 3, 4, 5, 6]
jogador1 = []
jogador2 = []
jogo = int(input("Aperte 1 para comecar"))

while jogo == 1:

    print("Bem vindo ao jogo.")
    print("Aperte 1 para jogar.")
    print("Aperte 2 para sair.")
iniciar = int(input("O que deseja fazer? "))
jogadas = 1


if iniciar == 1 and jogadas == 1:
    
        jogador1 = [[random.randint(0,5)]]
        jogadas += 1
        print(jogador1)

if iniciar == 1 and jogadas == 2:
        jogador2 = [random.randint(0,5)]
        jogadas -= 1
        print(jogador2)

if iniciar == 2:
        print("Obrigado por jogar")
        
else:
    print("Opcao invalida")
    break   