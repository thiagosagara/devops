
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    #usando a variavel do tipo bool
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Digite a letra: ")
        #o strip remove os espaços em branco
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                #upper serve para coloca todas as letras em maiuscula
                if(chute == letra):
                    # Nessa proxima linha ele vai substituir a letra (ou o chute (vai dar na mesma))
                    # pelo "_" correspondente
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

if (__name__ == "__main__"):
    jogar()

'''
Anotações:
    a função 'capitalize', retorna a primeira letra da palavra em maiuscula, como em:
    palavra = thiago
    palavra = palavra.capitalize()
    print(palavra) | resultado: Thiago

'''