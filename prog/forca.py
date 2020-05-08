
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    #usando a variavel do tipo bool
    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Digite a letra: ")
        #o strip remove os espaços em branco
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            #upper serve para coloca todas as letras em maiuscula
            if(chute.upper() == letra.upper()):
                print("encontrei {} a letra {} na posição {}".format(letra,chute,index))
            index = index + 1
        print("jogando...")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
