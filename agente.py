from abc import abstractmethod

#Classe base para ser usada de herança
class Agente():

    def __init__(self, id):
        self.id = id

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    @abstractmethod
    def onJogar(self, tabuleiro, tela):
        pass

    def jogar(self, tabuleiro, tela):
        print("\nJogada do agente: ", self.getId(), "\n")
        self.onJogar(tabuleiro, tela)
        tabuleiro.printMatriz(tela)
