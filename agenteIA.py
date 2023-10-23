import math

from agente import Agente
from tabuleiro import Tabuleiro, AGENTE_1, AGENTE_2

INFINITO_POSITIVO =  math.inf
INFINITO_NEGATIVO = -math.inf

VALOR_HEURISTICA_BAIXO = 10
VALOR_HEURISTICA_MEDIO = 100
VALOR_HEURISTICA_ALTO  = 100000


class AgenteIA(Agente):
    #Define o valor de um determinado estado do tabuleiro
    def calculaHeuristica(self, tabuleiro):
        matriz = tabuleiro.getMatriz()

        valorHeuristica = 0

        for linha in range(tabuleiro.getLinhas()):
            for coluna in range(tabuleiro.getColunas()):

                try: #Linhas verticais

                    #AGENTE_1 adiciona valor
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == matriz[linha + 2][coluna] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_MEDIO
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == matriz[linha + 2][coluna] == matriz[linha + 3][coluna] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_ALTO

                    #AGENTE_2 subtrai valor
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == matriz[linha + 2][coluna] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_MEDIO
                    if matriz[linha][coluna] == matriz[linha + 1][coluna] == matriz[linha + 2][coluna] == matriz[linha + 3][coluna] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_ALTO


                except IndexError:
                    pass

                try: #Linhas horizontais

                    #AGENTE_1 adiciona valor
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == matriz[linha][coluna + 2] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_MEDIO
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == matriz[linha][coluna + 2] == matriz[linha][coluna + 3] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_ALTO

                    #AGENTE_2 subtrai valor
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == matriz[linha][coluna + 2] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_MEDIO
                    if matriz[linha][coluna] == matriz[linha][coluna + 1] == matriz[linha][coluna + 2] == matriz[linha][coluna + 3] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_ALTO

                except IndexError:
                    pass

                try: #Diagonais - Superior Esquerdo para Inferior Direito

                    #AGENTE_1 adiciona valor
                    if linha < tabuleiro.getLinhas() - 1 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if linha < tabuleiro.getLinhas() - 2 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == matriz[linha + 2][coluna + 2] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_MEDIO
                    if linha < tabuleiro.getLinhas() - 3 and coluna < tabuleiro.getColunas() - 3 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == matriz[linha + 2][coluna + 2] == matriz[linha + 3][coluna + 3] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_ALTO

                    #AGENTE_2 subtrai valor
                    if linha < tabuleiro.getLinhas() - 1 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if linha < tabuleiro.getLinhas() - 2 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == matriz[linha + 2][coluna + 2] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_MEDIO
                    if linha < tabuleiro.getLinhas() - 3 and coluna < tabuleiro.getColunas() - 3 and matriz[linha][coluna] == matriz[linha + 1][coluna + 1] == matriz[linha + 2][coluna + 2] == matriz[linha + 3][coluna + 3] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_ALTO

                except IndexError:
                    pass

                try: #Diagonais - Inferior Esquerdo para Superior Direito

                    #AGENTE_1 adiciona valor
                    if linha > 0 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if linha > 1 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == matriz[linha - 2][coluna + 2] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_BAIXO
                    if linha > 2 and coluna < tabuleiro.getColunas() - 3 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == matriz[linha - 2][coluna + 2] == matriz[linha - 3][coluna + 3] == AGENTE_1:
                        valorHeuristica += VALOR_HEURISTICA_ALTO

                    #AGENTE_2 subtrai valor
                    if linha > 0 and coluna < tabuleiro.getColunas() - 1 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if linha > 1 and coluna < tabuleiro.getColunas() - 2 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == matriz[linha - 2][coluna + 2] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_BAIXO
                    if linha > 2 and coluna < tabuleiro.getColunas() - 3 and matriz[linha][coluna] == matriz[linha - 1][coluna + 1] == matriz[linha - 2][coluna + 2] == matriz[linha - 3][coluna + 3] == AGENTE_2:
                        valorHeuristica -= VALOR_HEURISTICA_ALTO

                except IndexError:
                    pass

        return valorHeuristica       

    #"Algorithms Explained – minimax and alpha-beta pruning" - https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    def buscaColunaMinMax(self, tabuleiro, profundidade, alpha, beta, idAgente):
        colunasLivres = tabuleiro.getListaColunasLivres()

        idAdversario = AGENTE_2 if self.getId() ==  AGENTE_1 else AGENTE_1

        vitoriaAgente     = tabuleiro.verificarVitoria(self.getId())
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
            
        if idAgente == AGENTE_1: #Maximiza o primeiro
            valorHeuristica = INFINITO_NEGATIVO
            colunaRet = None

            for coluna in colunasLivres:
                #Copia auxiliar do tabuleiro para avaliar as variações em recursivo / Implementação de __copy__ não estava funcionando
                tabuleiroAux = Tabuleiro(tabuleiro.getLinhas(), tabuleiro.getColunas(), tabuleiro.getMatriz().copy())
                tabuleiroAux.posiciona(coluna, AGENTE_2)

                heuristicaFilho = self.buscaColunaMinMax(tabuleiroAux, profundidade - 1, alpha, beta, AGENTE_2)[1]
                if heuristicaFilho > valorHeuristica:
                    valorHeuristica = heuristicaFilho
                    colunaRet = coluna

                alpha = max(alpha, valorHeuristica)

                if beta <= alpha:
                    break

            return colunaRet, valorHeuristica

        elif idAgente == AGENTE_2: #Minimiza o segundo
            valorHeuristica = INFINITO_POSITIVO
            colunaRet = None

            for coluna in colunasLivres:
                #Copia auxiliar do tabuleiro para avaliar as variações em recursivo / Implementação de __copy__ não estava funcionando
                tabuleiroAux = Tabuleiro(tabuleiro.getLinhas(), tabuleiro.getColunas(), tabuleiro.getMatriz().copy())
                tabuleiroAux.posiciona(coluna, AGENTE_1)

                heuristicaFilho = self.buscaColunaMinMax(tabuleiroAux, profundidade - 1, alpha, beta, AGENTE_1)[1]
                if heuristicaFilho < valorHeuristica:
                    valorHeuristica = heuristicaFilho
                    colunaRet = coluna

                beta = min(beta, valorHeuristica)

                if beta <= alpha:
                    break

            return colunaRet, valorHeuristica
        
    def jogar(self, tabuleiro):
        coluna, valorMinMax = self.buscaColunaMinMax(tabuleiro, tabuleiro.getLinhas() - 1, INFINITO_NEGATIVO, INFINITO_POSITIVO, AGENTE_2 if self.getId() ==  AGENTE_1 else AGENTE_1)

        tabuleiro.posiciona(coluna, self.getId())