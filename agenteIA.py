from defines import *
from agente import Agente
from tabuleiro import Tabuleiro
import random

class AgenteIA(Agente):

    #Valor para um determinado grupo de 4 espaços - Jonathan C.T. Kuo
    def calculaHeuristicaGrupo(self, grupo, idAgente):
        idAdversario = AGENTE_2 if self.getId() ==  AGENTE_1 else AGENTE_1

        valorHeuristicaGrupo = 0

        if (grupo.count(idAgente) == 3 and grupo.count(AGENTE_VAZIO) == 1):
            valorHeuristicaGrupo += 100

        if (grupo.count(idAgente) == 2 and grupo.count(AGENTE_VAZIO) == 2):
            valorHeuristicaGrupo += 45

        #Descontar apenas em casos que já quase da ruim, senão fica muito protetivo e não ataca
        if (grupo.count(idAdversario) == 3 and grupo.count(AGENTE_VAZIO) == 1):
            valorHeuristicaGrupo -= 90

        return valorHeuristicaGrupo

    #Define o valor de um determinado estado do tabuleiro
    def calculaHeuristicaTabuleiro(self, tabuleiro, idAgente):
        matriz = tabuleiro.getMatriz()

        valorHeuristica = 0

        #Dar pontos para coluna central - Isso da muito controle de campo
        for linha in range (tabuleiro.getLinhas()):
           if (matriz[linha][tabuleiro.getColunas() // 2] == idAgente):
               valorHeuristica += 50

        #Linhas horizontais
        for linha in range(tabuleiro.getLinhas()):
            for coluna in range(tabuleiro.getColunas() - 3):
                horizontal = [ matriz[linha][coluna], matriz[linha][coluna + 1], matriz[linha][coluna + 2], matriz[linha][coluna + 3] ]
                valorHeuristica += self.calculaHeuristicaGrupo(horizontal, idAgente)

        #Linhas verticais
        for coluna in range(tabuleiro.getColunas()):
            for linha in range(tabuleiro.getLinhas() - 3):
                vertical = [ matriz[linha][coluna], matriz[linha + 1][coluna], matriz[linha + 2][coluna], matriz[linha + 3][coluna] ]
                valorHeuristica += self.calculaHeuristicaGrupo(vertical, idAgente)

        #Diagonais - Superior esquerdo para inferior direito
        for linha in range(tabuleiro.getLinhas() - 3):
            for coluna in range(tabuleiro.getColunas() - 3):
                diagonal = [ matriz[linha][coluna], matriz[linha + 1][coluna + 1], matriz[linha + 2][coluna + 2], matriz[linha + 3][coluna + 3] ]
                valorHeuristica += self.calculaHeuristicaGrupo(diagonal, idAgente)

        #Diagonais - Inferior esquerdo para superior direito
        for linha in range(tabuleiro.getLinhas() - 3):
            for coluna in range(tabuleiro.getColunas() - 3):
                diagonal = [ matriz[linha][coluna + 3], matriz[linha + 1][coluna + 2], matriz[linha + 2][coluna + 1], matriz[linha + 3][coluna] ]
                valorHeuristica += self.calculaHeuristicaGrupo(diagonal, idAgente)

        return valorHeuristica       

    #"Algorithms Explained – minimax and alpha-beta pruning" - https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    def buscaColunaMinMax(self, tabuleiro, profundidade, alpha, beta, maximizar):
        colunasLivres = tabuleiro.getListaColunasLivres()

        vitoriaAgente1 = tabuleiro.verificaEstado(AGENTE_1) == VITORIA
        vitoriaAgente2 = tabuleiro.verificaEstado(AGENTE_2) == VITORIA

        posicaoTerminal = len(colunasLivres) == 0 or vitoriaAgente1 or vitoriaAgente2

        if (profundidade == 0 or posicaoTerminal):

            if posicaoTerminal:
                if vitoriaAgente1:
                    return (None, INFINITO_NEGATIVO)
                elif vitoriaAgente2:
                    return (None, INFINITO_POSITIVO)
                else:
                    return (None, 0) #Nenhuma jogada válida
                
            else: #Profundidade zero == ultimo nó possivel de expandir
                return (None, self.calculaHeuristicaTabuleiro(tabuleiro, AGENTE_2))
            
        if maximizar:
            valorHeuristica = INFINITO_NEGATIVO
            colunaRet = random.choice(colunasLivres)

            for coluna in colunasLivres:
                #Copia auxiliar do tabuleiro para avaliar as variações em recursivo / Implementação de __copy__ não estava funcionando
                tabuleiroAux = Tabuleiro(tabuleiro.getLinhas(), tabuleiro.getColunas(), tabuleiro.getMatriz().copy())
                tabuleiroAux.posiciona(coluna, AGENTE_2)

                heuristicaFilho = self.buscaColunaMinMax(tabuleiroAux, profundidade - 1, alpha, beta, False)[1]
                if heuristicaFilho > valorHeuristica:
                    valorHeuristica = heuristicaFilho
                    colunaRet = coluna

                alpha = max(alpha, valorHeuristica)

                if beta <= alpha:
                    break

            return colunaRet, valorHeuristica

        else:
            valorHeuristica = INFINITO_POSITIVO
            colunaRet = random.choice(colunasLivres)

            for coluna in colunasLivres:
                #Copia auxiliar do tabuleiro para avaliar as variações em recursivo / Implementação de __copy__ não estava funcionando
                tabuleiroAux = Tabuleiro(tabuleiro.getLinhas(), tabuleiro.getColunas(), tabuleiro.getMatriz().copy())
                tabuleiroAux.posiciona(coluna, AGENTE_1)

                heuristicaFilho = self.buscaColunaMinMax(tabuleiroAux, profundidade - 1, alpha, beta, True)[1]
                if heuristicaFilho < valorHeuristica:
                    valorHeuristica = heuristicaFilho
                    colunaRet = coluna

                beta = min(beta, valorHeuristica)

                if beta <= alpha:
                    break

            return colunaRet, valorHeuristica
        
    def onJogar(self, tabuleiro, tela):
        coluna, valorMinMax = self.buscaColunaMinMax(tabuleiro, tabuleiro.getLinhas() - 1, INFINITO_NEGATIVO, INFINITO_POSITIVO, False if self.getId() ==  AGENTE_1 else True)

        tabuleiro.posiciona(coluna, self.getId())