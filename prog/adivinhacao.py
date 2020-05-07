#advinhacao.py
import random

def jogar():


    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    # O random é um modulo pseudo-randomico, onde ele pega a hora como semente.
    # é possivel ainda usarmos a função seed dele para fixar uma semente, como em:
    # randon.seed(100)f


    #Variaveis globais
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000

    #Validação do nivel
    print("Qual o nível de dificuldade?")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    nivel = int(input("Define o nível: "))
    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    #For para o bloco de testes
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
            print("Parabéns! Você acertou com {} pontos!!".format(pontos))
            #com o break ele sai do laco
            break

        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            # racional da pontuação perdida:
            #  - é a subtração do numero secreto - o seu chute
            #  para não gerar numeros negativos vamos usar a função abs (absoluto)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do jogo")

    '''
    Anotações interessantes:
        
        A função round (que serve para arredondar) é diferente no python2 e 3.
        no 3, ela usa o banker's routing, que basicamente sempre arredonda para um numero par, e volta um int
        no 2, ela arredonda para o mais proximo procurando 0, e volta um float
        
        Ex:
            python3: round(3.5) | resultado: 4
            python2: round(3.5) | resultado: 4.0
            
            python3: round(4.5) | resultado: 4
            python2: round(4.5) | resultado: 5.0   
    
    '''

