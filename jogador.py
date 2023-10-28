from defines import *
from agente import Agente
import pygame as pg

class Jogador(Agente):

    def onJogar(self, tabuleiro, tela):

        posicionado = False

        while not posicionado:

            coluna = COLUNA_NAO_SELECIONADA

            for event in pg.event.get():
                
                if event.type == pg.MOUSEMOTION:
                    #Limpa o fundo
                    pg.draw.rect(tela, COR_VAZIO, (0, TAMANHO_ESPACO / 2, LARGURA_DISPLAY , TAMANHO_ESPACO))

                    xMouse, yMouse = event.pos
                    pg.draw.circle(tela, tabuleiro.getCorAgente(self.getId()), (xMouse, TAMANHO_ESPACO), RAIO_PECA)

                if event.type == pg.MOUSEBUTTONDOWN:
                   xMouse, yMouse = event.pos
                   coluna = tabuleiro.getColunaX(xMouse)

                pg.display.update()

            if coluna != COLUNA_NAO_SELECIONADA:
                posicionado = tabuleiro.posiciona(coluna, self.getId())

                if not posicionado:
                    print("Coluna selecionada inválida!")