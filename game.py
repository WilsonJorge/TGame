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