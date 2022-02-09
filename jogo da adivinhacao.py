import random


def jogar():

    print("********************************")
    print("Bem-vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade deseja?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 50: ")
        print("Voce digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 51):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!!!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O número foi maior do que o número secreto")
            elif(menor):
                print("Você errou! O número foi menor do que o número secreto")
            pontos_perdidos = numero_secreto - chute  # 40-20 = 20
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")


if(__name__ == "__main__"):
    jogar()
