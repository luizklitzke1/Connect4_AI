from tabuleiro import Tabuleiro, AGENTE_1, AGENTE_2
from jogador import Jogador
from agenteIA import AgenteIA
import pygame as pg

LINHAS = 6
COLUNAS = 7

LARGURA_DISPLAY = 800
ALTURA_DISPLAY = 600

vitoria = False
tabuleiroReal = Tabuleiro(LINHAS, COLUNAS)

agentes = [Jogador(AGENTE_1), AgenteIA(AGENTE_2)]

pg.init()
tela = pg.display.set_mode((LARGURA_DISPLAY, ALTURA_DISPLAY))

if __name__ == "__main__":

    while not vitoria:

        for agente in agentes:

            tabuleiroReal.printMatriz(tela)

            print("\nJogada do agente: ", agente.getId(), "\n")
            agente.jogar(tabuleiroReal)
            vitoria = tabuleiroReal.verificarVitoria(agente.getId())    

            if vitoria:
                print("Vitória do agente: ", agente.getId())
                tabuleiroReal.printMatriz(tela)
                break