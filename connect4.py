from tabuleiro import Tabuleiro
from jogador import Jogador
from agenteIA import AgenteIA

LINHAS = 6
COLUNAS = 7

PLAYER_1 = 1
PLAYER_2 = 2

vitoria = False
tabuleiroReal = Tabuleiro(LINHAS, COLUNAS)

agentes = [Jogador(PLAYER_1), Jogador(PLAYER_2)]

if __name__ == "__main__":

    while not vitoria:

        for agente in agentes:
            tabuleiroReal.printMatriz()
            
            agente.jogar(tabuleiroReal)
            vitoria = tabuleiroReal.verificarVitoria(agente.getId())    

            if vitoria:
                print("Vitória do agente: ", agente.getId())
                tabuleiroReal.printMatriz()
                break