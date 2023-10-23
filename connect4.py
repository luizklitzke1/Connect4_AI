from defines import *
from tabuleiro import Tabuleiro
from jogador import Jogador
from agenteIA import AgenteIA
import pygame as pg

vitoria = False
tabuleiroReal = Tabuleiro(LINHAS, COLUNAS)

agentes = [Jogador(AGENTE_1), AgenteIA(AGENTE_2)]

pg.init()
tela = pg.display.set_mode((LARGURA_DISPLAY, ALTURA_DISPLAY))
pg.display.set_caption("Connect 4 - Inteligência Artificial")

if __name__ == "__main__":

    tabuleiroReal.printMatriz(tela)
    while not vitoria:

        for agente in agentes:

            agente.jogar(tabuleiroReal, tela)
            vitoria = tabuleiroReal.verificarVitoria(agente.getId())    

            if vitoria:
                tabuleiroReal.anunciaVitoria(tela, agente.getId())

                hold = input("") #Segurar a tela aberta
                break