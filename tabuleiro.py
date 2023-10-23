import numpy as np

class Tabuleiro():
    
    def __init__(self, linhas, colunas):
        self.setLinhas(linhas)
        self.setColunas(colunas)

        self.matriz = np.zeros((self.getLinhas(), self.getColunas()))

    def getLinhas(self):
        return self.linhas
    
    def setLinhas(self, linhas):
        self.linhas = linhas

    def getColunas(self):
        return self.colunas
    
    def setColunas(self, colunas):
        self.colunas = colunas

    def getMatriz(self):
        return self.matriz
    
    def setMatiz(self, matriz):
        self.matriz = matriz

    def printMatriz(self):
        for linha in range(self.getLinhas()):
            print(self.getMatriz()[linha])

    #Posiciona uma peça do player no primeiro espaço livre, de baixo para cima, da coluna
    def posiciona(self, coluna, player):
        for linha in range(self.getLinhas()):
            if (self.getMatriz()[self.getLinhas() - 1 - linha][coluna] == 0):
                self.getMatriz()[self.getLinhas() - 1 - linha][coluna] = player
                return True
            
        return False #Coluna inválida

    #Retorna true caso o player tenha vencido com o ultimo movimento
    def verificarVitoria(self, player):

        #Quatro peças na horizontal
        for linha in range(self.getLinhas()):
            for coluna in range(self.getColunas() - 3):
                if (self.getMatriz()[linha][coluna] == player and self.getMatriz()[linha][coluna + 1] == player and self.getMatriz()[linha][coluna + 2] == player and self.getMatriz()[linha][coluna + 3] == player):
                    return True

        #Quatro peças na vertical
        for coluna in range(self.getColunas()):
            for linha in range(self.getLinhas() - 3):
                if (self.getMatriz()[linha][coluna] == player and self.getMatriz()[linha + 1][coluna] == player and self.getMatriz()[linha + 2][coluna] == player and self.getMatriz()[linha + 3][coluna] == player):
                    return True
                
        #Quatro peças em uma diagonal
        for coluna in range(self.getColunas() - 3):
            for linha in range(self.getLinhas() - 3):
                
                #Superior esquerdo para inferior direito
                if (self.getMatriz()[linha][coluna] == player and self.getMatriz()[linha + 1][coluna +1] == player and self.getMatriz()[linha + 2][coluna + 2] == player and self.getMatriz()[linha + 3][coluna + 3] == player):
                    return True
                
                #Inferior esquerdo para superior direito
                if (self.getMatriz()[self.getLinhas() - linha - 1][self.getColunas() - coluna - 1] == player and self.getMatriz()[self.getLinhas() - linha - 2][self.getColunas() - coluna - 2] == player and self.getMatriz()[self.getLinhas() - linha - 3][self.getColunas() - coluna - 3] == player and self.getMatriz()[self.getLinhas() - linha - 4][self.getColunas() - coluna - 4] == player):
                    return True
                
        return False