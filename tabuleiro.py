import numpy as np

LINHA_INVALIDA = -1

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

    #Primeira linha livre de baixo para cima na coluna. Caso nenhuma, retorna LINHA_INVALIDA
    def getPosicaoLivreColuna(self, coluna):
        for linha in range(self.getLinhas()):
            if (self.getMatriz()[self.getLinhas() - 1 - linha][coluna] == 0):
                return linha
            
        return LINHA_INVALIDA #Coluna completamente preenchida
    
    #Retorna todas as colunas ainda válidas
    def getListaColunasLivres(self):
        colunasLivres = []

        for coluna in range(self.getColunas()):
            if (self.getPosicaoLivreColuna(coluna) != LINHA_INVALIDA):
                colunasLivres.insert(coluna)

    #Posiciona uma peça do agente no primeiro espaço livre, de baixo para cima, da coluna
    def posiciona(self, coluna, agente):
        linhaPosicionar = self.getPosicaoLivreColuna(coluna)

        if linhaPosicionar == LINHA_INVALIDA:
            return False #Coluna inválida
        
        self.getMatriz()[linhaPosicionar][coluna] = agente.getId()
            

    #Retorna true caso o agente tenha vencido com o ultimo movimento
    def verificarVitoria(self, agente):

        #Quatro peças na horizontal
        for linha in range(self.getLinhas()):
            for coluna in range(self.getColunas() - 3):
                if (self.getMatriz()[linha][coluna] == agente and self.getMatriz()[linha][coluna + 1] == agente and self.getMatriz()[linha][coluna + 2] == agente and self.getMatriz()[linha][coluna + 3] == agente):
                    return True

        #Quatro peças na vertical
        for coluna in range(self.getColunas()):
            for linha in range(self.getLinhas() - 3):
                if (self.getMatriz()[linha][coluna] == agente and self.getMatriz()[linha + 1][coluna] == agente and self.getMatriz()[linha + 2][coluna] == agente and self.getMatriz()[linha + 3][coluna] == agente):
                    return True
                
        #Quatro peças em uma diagonal
        for coluna in range(self.getColunas() - 3):
            for linha in range(self.getLinhas() - 3):
                
                #Superior esquerdo para inferior direito
                if (self.getMatriz()[linha][coluna] == agente and self.getMatriz()[linha + 1][coluna +1] == agente and self.getMatriz()[linha + 2][coluna + 2] == agente and self.getMatriz()[linha + 3][coluna + 3] == agente):
                    return True
                
                #Inferior esquerdo para superior direito
                if (self.getMatriz()[self.getLinhas() - linha - 1][self.getColunas() - coluna - 1] == agente and self.getMatriz()[self.getLinhas() - linha - 2][self.getColunas() - coluna - 2] == agente and self.getMatriz()[self.getLinhas() - linha - 3][self.getColunas() - coluna - 3] == agente and self.getMatriz()[self.getLinhas() - linha - 4][self.getColunas() - coluna - 4] == agente):
                    return True
                
        return False