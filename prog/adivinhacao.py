import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
# O random é um modulo pseudo-randomico, onde ele pega a hora como semente.
# é possivel ainda usarmos a função seed dele para fixar uma semente, como em:
# randon.seed(100)f
#
numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

print("Qual o nível de dificuldade?")
print("(1) Fácil | (2) Médio | (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um numero de 1 a 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        #O continue volta para uma identação para cima (nesse caso o for)
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        #com o break ele sai do laco
        break

    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")