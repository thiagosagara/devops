
import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    #adicionado o upper na palabra secreta
    #palavra_secreta = "one".upper()
    #usando o list comprehension
    #letras_acertadas = ["_" for letra in palavra_secreta]

    #outro jeito é fazer do modo tradicional
    #for letra in palavra_secreta:
    #    letras_acertadas.append("_")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        #adiciona tudo no txt para uma lista
        palavras.append(linha)

    arquivo.close()

    # com base no tamano da lista (len(palavras)), ele escolhe randomicamente a palavra
    numero = random.randrange(0, len(palavras))

    #com base no numero (index), ele cria a instancia ja com a letra em maiuscula
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]


    #usando a variavel do tipo bool
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Digite a letra: ")
        #o strip remove os espaços em branco e caracteres especiais (como o \n)
        #alteramos o chute do usuario para tudo em maiusculas
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
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

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

    Na list comphension tb é possivel usar o if, como em:
    
    inteiros = [1,3,4,5,7,8,9]
    pares = [x for x in inteiros if x % 2 == 0]
    As linhas acima adicionariam apenas os pares na lista 'pares', da maneira tradicional ficaria:
    
    inteiros = [1,3,4,5,7,8,9]
    pares = []
    for numero in inteiros:
        if numero % 2 == 0:
            pares.append(numero)
    
    Arquivos:
        open("arquivo",tipo) | open("arquivo.txt", "w")
        sendo que:
            a - ele vai adicionar coisas no arquivo
            w - ele vai sobreescrever o conteudo no arquivo
            r - ele vai apenas ler o arquivo
            b - ele vai usar binario para abrir o arquivo (para uma imagem por exemplo)
                
        também é possivel adicionar o \n para dar um newline.
        exemplo:
            arquivo = open("palavras.txt", "a")
            arquivo.write("morango\n")
            arquivo.write("manga\n")
        Para fechar:
            arquivo.close()
    
'''