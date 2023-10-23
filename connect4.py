from tabuleiro import Tabuleiro
from agente import Agente
from jogador import Jogador

LINHAS = 6
COLUNAS = 7

PLAYER_1 = 1
PLAYER_2 = 2

parar = False
tabuleiroReal = Tabuleiro(LINHAS, COLUNAS)

agentes = [Jogador(PLAYER_1), Jogador(PLAYER_2)]

if __name__ == "__main__":

    while not parar:

        for agente in agentes:
            tabuleiroReal.printMatriz()
            
            agente.jogar(tabuleiroReal)
            parar = tabuleiroReal.verificarVitoria(agente.getId())    

            if parar:
                print("Vitória do agente: ", agente.getId())
                tabuleiroReal.printMatriz()
                break