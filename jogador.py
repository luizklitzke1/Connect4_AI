from agente import Agente

class Jogador(Agente):

    def jogar(self, tabuleiro):

        posicionado = False

        while not posicionado:
            coluna = int(input("Coluna: "))
            posicionado = tabuleiro.posiciona(coluna, self.getId())

            if not posicionado:
                print("Coluna selecionada inválida!")