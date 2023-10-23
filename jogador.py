from agente import Agente

class Jogador(Agente):

    def jogar(self, tabuleiro):
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        super().posicionar(tabuleiro, linha, coluna)