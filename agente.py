from abc import ABC, abstractmethod

#Classe base para ser usada de herança
class Agente():

    def __init__(self, id):
        self.id = id

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def posicionar(self, tabuleiroAux, linha, coluna):
        tabuleiroAux[linha][coluna] = self.id

    @abstractmethod
    def jogar(self, tabuleiro):
        pass
