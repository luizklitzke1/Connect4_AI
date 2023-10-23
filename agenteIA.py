import math

from agente import Agente
from tabuleiro import Tabuleiro

INFINITO_POSITIVO =  math.inf
INFINITO_NEGATIVO = -math.inf

VALOR_HEURISTICA_BAIXO = 10
VALOR_HEURISTICA_MEDIO = 100

PLAYER_1 = 1
PLAYER_2 = 2

class AgenteIA(Agente):
    #Define o valor de um determinado estado do tabuleiro
    def calculaHeuristica(self, tabuleiro):
        matriz = tabuleiro.getMatriz()

        valorHeuristica = 0

        for linha in range(tabuleiro.getLinhas()):
            for coluna in range(tabuleiro.getColunas()):

                try: #Linhas horizontais

                    #PLAYER_1 adiciona valor
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == matriz[linha + 2][coluna] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_MEDIO

                    #PLAYER_2 subtrai valor
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == PLAYER_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == matriz[linha + 2][coluna] == PLAYER_2:
                        valorHeuristica -= VALOR_HEURISTICA_MEDIO

                except IndexError:
                    pass

                try: #Linhas verticais

                    #PLAYER_1 adiciona valor
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == matriz[linha][coluna + 2] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_MEDIO

                    #PLAYER_2 subtrai valor
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == 1:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == matriz[linha][coluna + 2] == 1:
                        valorHeuristica -= VALOR_HEURISTICA_MEDIO

                except IndexError:
                    pass

                try: #Diagonais - Superior Esquerdo para Inferior Direito

                    #PLAYER_1 adiciona valor
                    if linha < tabuleiro.getLinhas() - 1 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if linha < tabuleiro.getLinhas() - 2 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == matriz[linha + 2][coluna + 2] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_MEDIO

                    #PLAYER_2 subtrai valor
                    if linha < tabuleiro.getLinhas() - 1 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == PLAYER_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if linha < tabuleiro.getLinhas() - 2 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == matriz[linha + 2][coluna + 2] == PLAYER_2:
                        valorHeuristica -= VALOR_HEURISTICA_MEDIO

                except IndexError:
                    pass

                try: #Diagonais - Inferior Esquerdo para Superior Direito

                    #PLAYER_1 adiciona valor
                    if linha > 0 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if linha > 1 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == matriz[linha - 2][coluna + 2] == PLAYER_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO

                    #PLAYER_2 subtrai valor
                    if linha > 0 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == PLAYER_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if linha > 1 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == matriz[linha - 2][coluna + 2] == PLAYER_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO

                except IndexError:
                    pass

        return valorHeuristica       

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
                return (None, self.calculaHeuristica(tabuleiro))
            
        if playerMaximizar == idAdversario:
            valorHeuristica = INFINITO_NEGATIVO
            coluna = None

            for coluna in colunasLivres:
                #Copia auxiliar do tabuleiro para avaliar as variações em recursivo / Implementação de __copy__ não estava funcionando
                tabuleiroAux = Tabuleiro(tabuleiro.getLinhas(), tabuleiro.getColunas(), tabuleiro.getMatriz().copy())
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
                #Copia auxiliar do tabuleiro para avaliar as variações em recursivo / Implementação de __copy__ não estava funcionando
                tabuleiroAux = Tabuleiro(tabuleiro.getLinhas(), tabuleiro.getColunas(), tabuleiro.getMatriz().copy())
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