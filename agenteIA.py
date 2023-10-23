import math

from agente import Agente
from tabuleiro import Tabuleiro

INFINITO_POSITIVO =  math.inf
INFINITO_NEGATIVO = -math.inf

PLAYER_1 = 1
PLAYER_2 = 2

class AgenteIA(Agente):
    #Define o valor de um determinado estado do tabuleiro
    def calculaHeuristica(self, tabuleiro, agente):
        matriz = tabuleiro.getMatriz()

        return 99        

    #"Algorithms Explained – minimax and alpha-beta pruning" - https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    def buscaColunaMinMax(self, tabuleiro, profundidade, alpha, beta, playerMaximizar):
        colunasLivres = tabuleiro.getListaColunasLivres()

        idAdversario = PLAYER_2 if self.getId() ==  PLAYER_1 else PLAYER_1 

        vitoriaAgente = tabuleiro.verificarVitoria(self.getId())
        vitoriaAdversario = tabuleiro.verificarVitoria(idAdversario)

        posicaoTerminal = len(colunasLivres) == 0 or vitoriaAgente or vitoriaAdversario

        if (profundidade == 0 or posicaoTerminal):

            if posicaoTerminal:
                if vitoriaAgente:
                    return (None, INFINITO_POSITIVO)
                elif vitoriaAdversario:
                    return (None, INFINITO_NEGATIVO)
                else:
                    return (None, 0) #Nenhuma jogada válida
                
            else: #Profundidade zero == ultimo nó possivel de expandir
                return (None, self.calculaHeuristica(tabuleiro, self.getId()))
            
        if playerMaximizar == idAdversario:
            valorHeuristica = INFINITO_NEGATIVO
            coluna = None

            for coluna in colunasLivres:
                #Copia auxilia do tabuleiro para avaliar as variações em recursivo
                tabuleiroAux = tabuleiro.copy()
                tabuleiroAux.posiciona(coluna, idAdversario)

                colunaAux, heuristicaFilho = self.buscaColunaMinMax(tabuleiroAux, profundidade - 1, alpha, beta, self.getId())
                if heuristicaFilho > valorHeuristica:
                    valorHeuristica = heuristicaFilho
                    coluna = colunaAux

                alpha = max(alpha, valorHeuristica)

                if beta <= alpha:
                    break

            return coluna, valorHeuristica

        elif playerMaximizar == self.getId():
            valorHeuristica = INFINITO_POSITIVO
            coluna = None

            for coluna in colunasLivres:
                #Copia auxilia do tabuleiro para avaliar as variações em recursivo
                tabuleiroAux = tabuleiro.copy()
                tabuleiroAux.posiciona(coluna, self.getId())

                colunaAux, heuristicaFilho = self.buscaColunaMinMax(tabuleiroAux, profundidade - 1, alpha, beta, idAdversario)
                if heuristicaFilho > valorHeuristica:
                    valorHeuristica = heuristicaFilho
                    coluna = colunaAux

                beta = min(beta, valorHeuristica)

                if beta <= alpha:
                    break

            return coluna, valorHeuristica
        
    def jogar(self, tabuleiro):
        coluna, valorMinMax = self.buscaColunaMinMax(tabuleiro, tabuleiro.getLinhas() - 1, INFINITO_NEGATIVO, INFINITO_POSITIVO, self.getId())

        tabuleiro.posiciona(coluna, self.getId())