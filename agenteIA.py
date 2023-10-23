from agente import Agente
from tabuleiro import Tabuleiro

class AgenteIA(Agente):

    def jogar(self, tabuleiro):
        return super().jogar(tabuleiro)
    

    #"Algorithms Explained – minimax and alpha-beta pruning" - https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
    def buscaColunaMinMax(self, tabuleiro, profundidade, playerMaximizar):
        pass