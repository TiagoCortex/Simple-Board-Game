from math import *
from matplotlib.pyplot import *
from matplotlib.colors import *

# O objetivo deste programa e simular um jogo de tabuleiro com dimensoes indefinidas.
# Cada casa tem uma cor e um numero, este ultimo representa o valor da casa.
# Ao contrario dos jogos de tabuleiro habituais, em que o desenvolvimento do mesmo depende
# do lancamento de um dado, por exemplo, neste jogo uma vez escolhida a casa de partida,
# o resultado do jogo fica automaticamente determinado.

# A matriz marcas representa um exemplo de um tabuleiro 4x4 com os valores de cada posicao
Marcas = [ [3,9,8,3],
           [5,5,6,1],
           [4,6,4,3],
           [1,2,7,2]  ]
# A matriz cores representa um exemplo de um tabuleiro 4x4 com as cores de cada posicao
Cores = [  [1,2,3,1],
           [2,3,2,3],
           [1,3,1,2],
           [3,1,2,3]  ]

#Vermelho = 1 ; Verde = 2 ; Azul = 3
RGB = [[1,0,0], [0,1,0], [0,0,1]]
my_cmap = ListedColormap(RGB)
imshow(Cores, cmap = my_cmap)
#show()

#Funcao 1 -------------------------------------------------
def distancia_casas(P1, P2):
    """Dados dois pontos, P1 e P2, a funcao retorna a distancia entre os dois.
       Em cada um dos parametros colocam-se as coordenadas dos respetivos pontos dos quais
       se quer descobrir a distancia. Se quiser-mos calcular a distancia entre P1=(1,2) e
       P2=(3,1) escrevemos "distancia_casas((1,2),(3,1))"."""
    return sqrt( ((P1[0] - P2[0])**2) + ((P1[1] - P2[1])**2) )

#Funcao 2 -------------------------------------------------
def mesma_cor(cor, Cores):
    """Dada uma cor, presente no tabuleiro, a funcao retoma todas as posicoes com essa cor.
       Imaginando que queremos saber quais sao as casas com a cor vermelha, cujo numero correspondente
       e 1, escrevemos "mesma_cor(1, Cores)" e a funcao dara uma lista com as coordenadas de todos os
       pontos com cor vermelha na matriz das cores"""
    lista = []
    for linha in range(len(Cores)) :
        for coluna in range(len(Cores[linha])) :
            if Cores[linha][coluna] == cor :
                lista.append((linha, coluna))
    return lista

#Funcao 3 -------------------------------------------------
def casa_mais_proxima(P, Casas):
    """Dados um ponto e um conjunto de casas, a funcao indica qual e a casa desse conjunto
       que esta mais proxima do ponto de interesse. Se quisermos saber qual e a casa mais
       proxima do ponto (1,2) dentro das casas pertencentes ao conjunto (0,0), (1,1) e (3,3) fariamos:
       "casa_mais_proxima((1,2), [(0,0),(1,1),(3,3)])" """
    casa_comparacao = Casas[0]
    distancia = distancia_casas(P, Casas[0])
    for vetor in range(len(Casas)):
        if (distancia_casas(P, Casas[vetor]) < distancia):
            distancia = distancia_casas(P, Casas[vetor])
            casa_comparacao = Casas[vetor]
        elif ((distancia_casas(P, Casas[vetor]) == distancia)):
            if (Casas[vetor][0] > casa_comparacao[0]):
                distancia = distancia_casas(P, Casas[vetor])
                casa_comparacao = Casas[vetor]
            elif ((Casas[vetor][0] == casa_comparacao[0]) and (Casas[vetor][1] > casa_comparacao[1])):
                distancia = distancia_casas(P, Casas[vetor])
                casa_comparacao = Casas[vetor]
    casa_final = casa_comparacao
    return casa_final

#Funcao 4 ------------------------------------------------------------------
def percurso(Inicial,Casas) :
    """Dada uma casa inicial e um conjunto de casas que vao constituir o nosso percurso,
       a funcao retribui a ordem do percurso tendo em conta que os saltos sao sempre para a casa
       mais proxima da atual e que ainda nao esteja incluida neste percurso, ou seja, nao ha repeticao de casas.
       Por exemplo, se quisermos saber qual e o percurso que comeca na posicao (0,0) e passa pelas casas (3,3),
       (1,1) e (1,0) fariamos "percurso((0,0),[(3,3),(1,1),(1,0)])" """
    temp = 0
    aux = Casas         #O professor aconselhou a fazer alteracoes numa matriz auxiliar
    casa_anterior = tuple(Inicial)
    percurso = [tuple(Inicial)]
    for i in range(len(aux)) :
        percurso.append(casa_mais_proxima(casa_anterior,aux))
        temp = casa_mais_proxima(casa_anterior,aux)
        aux.remove(tuple(casa_mais_proxima(casa_anterior, aux)))
        casa_anterior = temp
    return percurso

#Funcao 5 ------------------------------------------------------------------
#Primeiramente foi definida uma funcao auxiliar que nos diz qual e o valor duma casa
def valor_casa(Ponto, Marcas):
    """Dada uma posicao no tabuleiro, a funcao mostra-nos qual e o valor dessa casa.
       Se quisermos saber qual e o valor da casa na posicao (1,2) num tabuleiro cujos valores
       das casas estao descritos segundo uma matriz, por exemplo, a matriz "Marcas", fariamos
       "valor_casa((1,2), Marcas)" """
    return Marcas[Ponto[0]][Ponto[1]]

def valor_salto(P1, P2, Marcas):
    """Dadas duas posicoes, a funcao calcula qual e o valor de salto tendo em conta
       os valores de cada uma das casas. Este calculo e feito na forma :
       (valor da segunda casa - valor da primeira casa)^2
       Se quisermos saber o valor do salto entre as casas (2,2) e (3,2), tendo em conta
       os valores para cada posicao descritos pela matriz "Marcas", fazemos
       "valor_salto((2,2),(3,2), Marcas)"""
    valor_1 = valor_casa(P1, Marcas)
    valor_2 = valor_casa(P2, Marcas)
    valor_salto = (valor_2 - valor_1)**2
    return valor_salto

#Funcao 6 ------------------------------------------------------------------
def valor_percurso(Percurso, Marcas):
    """Dado um percurso, a funcao calcula o valor do percurso atraves da soma dos valores de
       cada salto. Nesse caso, se quisermos calcular o valor do percurso : (2,2),(3,1),(2,0),(0,0),(0,3),
       tendo em conta os valores de cada posicao descritos pela matriz "Marcas", fariamos:
       valor_percurso([(2,2),(3,1),(2,0),(0,0),(0,3)], Marcas)"""
    sum = 0
    for vetor in range(len(Percurso) - 1) :
        sum += valor_salto(Percurso[vetor], Percurso[vetor + 1], Marcas)
    return sum

#Funcao 7 -------------------------------------------------------------------
#Primeiramente fizemos uma funcao auxiliar que nos indica o premio de cada casa
def premio_casa(Casa, Cores, Marcas):
    """Dada uma casa, a funcao mostra qual e o premio correspondente a essa casa.
       Por exemplo, se quisermos saber qual e o premio destinado a casa (1,1) tendo em conta
       as cores das casas descritas pela matriz "Cores" e valores das mesmas descritas
       pela matriz "Marcas" fariamos:
       "premio_casa((1,1), Cores, Marcas)" """
    cor = Cores[Casa[0]][Casa[1]]
    Casas = mesma_cor(cor, Cores)
    Percurso = percurso(Casa, Casas)
    premio = valor_percurso(Percurso, Marcas)
    return premio

def casa_mais_valiosa(Cores,Marcas):
    """Dadas duas matrizes capazes de caracterizar por completo o tabuleiro do jogo, ou seja,
       uma matriz para as cores de cada casa e outra para o valor de cada casa, a funcao retribui
       a melhor pontuacao possivel no jogo e todas as casas a que esta pontuacao corresponde.
       Usando como exemplos de matrizes que caracterizam o tabuleiro a matriz "Cores" para as cores
       de cada casa e a matriz "Marcas" para o valor de cada casa, fariamos:
       "casa_mais_valiosa(Cores,Marcas)" """
    premios = []
    for linha in range(len(Marcas)):   #Primeiramente, a funcao cria uma matriz com os premios de todas as casas
        for coluna in range(len(Marcas[linha])):
            premio = premio_casa((linha,coluna), Cores, Marcas)
            premios.append(premio)

    comparacao = premios[0]
    for premio in range(len(premios) - 1):   #Agora, a funcao vai procurar o maior premio possivel
        if comparacao < premios[premio + 1]:
            comparacao = premios[premio + 1]

    maior_premio = comparacao
    casas_mais_valiosas = []
    for linha in range(len(Marcas)):   #Finalmente, a funcao procura quais sao os pontos cujo premio e o maior possivel
        for coluna in range(len(Marcas[linha])):
            premio = premio_casa((linha, coluna), Cores, Marcas)
            if premio == maior_premio:
                casas_mais_valiosas.append((linha, coluna))

    return casas_mais_valiosas, maior_premio







