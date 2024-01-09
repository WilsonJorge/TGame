import random
from os import system,name
#Funcao para limpar a tela para cada execucao
def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')