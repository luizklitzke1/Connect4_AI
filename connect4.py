import numpy as np

LINHAS = 6
COLUNAS = 7

PLAYER_1 = 1
PLAYER_2 = 2

#Iniciliar matriz de tabuleiro com todas posições zeradas
def iniciar_tabuleiro():
    return np.zeros((LINHAS, COLUNAS))

def mostrar_tabuleiro(tabuleiroPrint):
    for linha in range(LINHAS):
        print(tabuleiroPrint[linha])

def posicionar(tabuleiroAux, linha, coluna, player):
    tabuleiroAux[linha][coluna] = player

#Retorna true caso o player tenha vencido com o ultimo movimento
def verificar_vitoria(tabuleiroAux, player):

    #Quatro peças na horizontal
    for linha in range(LINHAS):
        for coluna in range(COLUNAS - 3):
            if (tabuleiroAux[linha][coluna] == player and tabuleiroAux[linha][coluna + 1] == player and tabuleiroAux[linha][coluna + 2] == player and tabuleiroAux[linha][coluna + 3] == player):
                return True

    #Quatro peças na vertical
    for coluna in range(COLUNAS):
        for linha in range(LINHAS - 3):
            if (tabuleiroAux[linha][coluna] == player and tabuleiroAux[linha + 1][coluna] == player and tabuleiroAux[linha + 2][coluna] == player and tabuleiroAux[linha + 3][coluna] == player):
                return True
            
    #Quatro peças em uma diagonal
    for coluna in range(COLUNAS - 3):
        for linha in range(LINHAS - 3):
               
            #Superior esquerdo para inferior direito
            if (tabuleiroAux[linha][coluna] == player and tabuleiroAux[linha + 1][coluna +1] == player and tabuleiroAux[linha + 2][coluna + 2] == player and tabuleiroAux[linha + 3][coluna + 3] == player):
                return True
            
            #Inferior esquerdo para superior direito
            if (tabuleiroAux[LINHAS - linha - 1][COLUNAS - coluna - 1] == player and tabuleiroAux[LINHAS - linha - 2][COLUNAS - coluna - 2] == player and tabuleiroAux[LINHAS - linha - 3][COLUNAS - coluna - 3] == player and tabuleiroAux[LINHAS - linha - 4][COLUNAS - coluna - 4] == player):
                return True
            
    return False

parar = False

tabuleiroReal = iniciar_tabuleiro()

mostrar_tabuleiro(tabuleiroReal)

while not parar:
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))

    posicionar(tabuleiroReal, linha, coluna, PLAYER_1)
    mostrar_tabuleiro(tabuleiroReal)

    parar = verificar_vitoria(tabuleiroReal, PLAYER_1)    