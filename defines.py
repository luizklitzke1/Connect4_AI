import math

#IDs de Agentes
AGENTE_VAZIO = 0
AGENTE_1     = 1
AGENTE_2     = 2

#Indicadores de erro
LINHA_INVALIDA         = -1
COLUNA_NAO_SELECIONADA = -1

#Cores para representação em tela
COR_VERMELHO = (255, 0 , 0  )
COR_AZUL     = (0  , 0 , 255)
COR_AMARELO  = (255,255, 0  )
COR_PRETO    = (0  , 0 , 0  )

COR_TABULEIRO = COR_AZUL
COR_AGENTE_1  = COR_AMARELO
COR_AGENTE_2  = COR_VERMELHO
COR_VAZIO     = COR_PRETO


#Tamanhos - em pixels - dos elementos na tela
LARGURA_DISPLAY = 800
ALTURA_DISPLAY  = 600

TAMANHO_ESPACO = 70
RAIO_PECA = TAMANHO_ESPACO / 2 - 3
X_INICIO_TABULEIRO = 150
Y_INICIO_TABULEIRO = 120
OFFSET_TABULEIRO   = 40

#Constantes matemáticas para min-max
INFINITO_POSITIVO =  math.inf
INFINITO_NEGATIVO = -math.inf

#Tamanho do tabuleiro
LINHAS  = 6
COLUNAS = 7

#Estados do jogo
ANDAMENTO = 0
VITORIA   = 1
EMPATE    = 2