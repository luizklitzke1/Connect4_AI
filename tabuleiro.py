import numpy as np
import pygame as pg
import math
from defines import *

class Tabuleiro():
    
    def __init__(self, linhas, colunas, matriz = None):
        self.setLinhas (linhas )
        self.setColunas(colunas)

        if matriz is None: #Matriz limpa, preenchida por zeros
            self.matriz = np.zeros((self.getLinhas(), self.getColunas()))
        else:
            self.matriz = matriz

    def getCorAgente(self, agente):
        if agente == AGENTE_1:
            return COR_AGENTE_1
        elif agente == AGENTE_2:
            return COR_AGENTE_2
        
        return COR_VAZIO

    def printMatriz(self, tela):
        pg.draw.rect(tela, COR_TABULEIRO, pg.Rect(X_INICIO_TABULEIRO - OFFSET_TABULEIRO, Y_INICIO_TABULEIRO, self.getColunas() * TAMANHO_ESPACO + OFFSET_TABULEIRO * 2, self.getLinhas() * TAMANHO_ESPACO + OFFSET_TABULEIRO / 2))

        matriz = self.getMatriz()

        for linha in range(self.getLinhas()):
            print(matriz[linha])
            for coluna in range(self.getColunas()):
                pg.draw.circle(tela, self.getCorAgente(matriz[linha][coluna]), (X_INICIO_TABULEIRO + TAMANHO_ESPACO / 2 + coluna * TAMANHO_ESPACO, Y_INICIO_TABULEIRO + TAMANHO_ESPACO / 2 + linha * TAMANHO_ESPACO), RAIO_PECA)

        pg.display.flip()

    #Primeira linha livre de baixo para cima na coluna. Caso nenhuma, retorna LINHA_INVALIDA
    def getPosicaoLivreColuna(self, coluna):
        for linha in range(self.getLinhas()):
            linhaBaixoParaCima = self.getLinhas() - 1 - linha
            if (self.getMatriz()[linhaBaixoParaCima][coluna] == 0):
                return linhaBaixoParaCima
            
        return LINHA_INVALIDA #Coluna completamente preenchida
    
    #Retorna todas as colunas ainda válidas
    def getListaColunasLivres(self):
        colunasLivres = []

        for coluna in range(self.getColunas()):
            if (self.getPosicaoLivreColuna(coluna) != LINHA_INVALIDA):
                colunasLivres.append(coluna)

        return colunasLivres

    #Posiciona uma peça do agente no primeiro espaço livre, de baixo para cima, da coluna
    def posiciona(self, coluna, IdAgente):
        linhaPosicionar = self.getPosicaoLivreColuna(coluna)

        if linhaPosicionar == LINHA_INVALIDA:
            return False #Coluna completamente preenchida
        
        self.getMatriz()[linhaPosicionar][coluna] = IdAgente
        return True
            

    #Retorna true caso o agente tenha vencido com o ultimo movimento
    def verificaEstado(self, agente):
        #Quatro peças na horizontal
        for linha in range(self.getLinhas()):
            for coluna in range(self.getColunas() - 3):
                if (self.getMatriz()[linha][coluna] == agente and self.getMatriz()[linha][coluna + 1] == agente and self.getMatriz()[linha][coluna + 2] == agente and self.getMatriz()[linha][coluna + 3] == agente):
                    return VITORIA

        #Quatro peças na vertical
        for coluna in range(self.getColunas()):
            for linha in range(self.getLinhas() - 3):
                if (self.getMatriz()[linha][coluna] == agente and self.getMatriz()[linha + 1][coluna] == agente and self.getMatriz()[linha + 2][coluna] == agente and self.getMatriz()[linha + 3][coluna] == agente):
                    return VITORIA
            
        #Quatro peças em uma diagonal
        for coluna in range(self.getColunas() - 3):
            for linha in range(self.getLinhas() - 3):
                if (self.getMatriz()[linha][coluna] == agente and self.getMatriz()[linha + 1][coluna + 1] == agente and self.getMatriz()[linha + 2][coluna + 2] == agente and self.getMatriz()[linha + 3][coluna + 3] == agente):
                    return VITORIA
                elif (self.getMatriz()[linha][coluna + 3] == agente and self.getMatriz()[linha + 1][coluna + 2] == agente and self.getMatriz()[linha + 2][coluna + 1] == agente and self.getMatriz()[linha + 3][coluna] == agente):
                    return VITORIA

        if len(self.getListaColunasLivres()) == 0:
            return EMPATE
        
        return ANDAMENTO
    
    #Retorna coluna corespondente à uma posição X na tela
    def getColunaX(self, x):
        if (x < X_INICIO_TABULEIRO or x >= X_INICIO_TABULEIRO + self.getColunas() * TAMANHO_ESPACO):
            return COLUNA_NAO_SELECIONADA
        
        return int(math.floor((x - X_INICIO_TABULEIRO ) / TAMANHO_ESPACO))
    
    #Mostra texto da vitória de algum agente
    def anunciaEstado(self, tela, estado, idAgente):
        mensagem = ""

        if estado == VITORIA:
            mensagem = "Vitória do agente: " + str(idAgente)
        elif estado == EMPATE:
            mensagem == "O jogo acabou em empate!"

        print(mensagem)
        self.printMatriz(tela)

        pg.font.init()
        pg.draw.rect(tela, COR_VAZIO, (0, TAMANHO_ESPACO / 2, LARGURA_DISPLAY , TAMANHO_ESPACO))

        font = pg.font.SysFont("Comic Sans MS", int(TAMANHO_ESPACO / 2))
        text_surface = font.render(mensagem, False, COR_AMARELO)
        tela.blit(text_surface, (X_INICIO_TABULEIRO, TAMANHO_ESPACO / 2))
        pg.display.flip()
    
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
