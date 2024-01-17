import random
from os import system,name
#Funcao para limpar a tela para cada execucao
def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')



 #Funcao 
def game():

    limpa_tela()
    limpa_tela()
    print("\nBem-Vindo ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe a palavras
    palavra = random.choice(palavras)

    #List Comprehension
    letras_descobertas = ['_' for letra in palavra]

    #Numero de Chances 
    chances =6

    #Lista para letras erradas
    lestras_erradas = []  

    #Loop enquantp numero de chances for maior que zero

    while chances > 0:
        #print
        print("".join(letras_descobertas))
        print("\nChances restantes:",chances)
        print("Letras erradas:","".join(lestras_erradas))

        #Tentativa
        tentativa = input("n\Digite uma letra:").lower()      

        # Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index+= 1
        else:
            chances -= 1
            lestras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas :
            print("\n Voce Ganhou, a Palavra era:", palavra)
        break

if __name__  == "_main_" :
     game()
     print("\n Parabens. Voce esta apredendo programacao em Python com a DSA. :)\n") 

