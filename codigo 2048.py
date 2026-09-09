# FUNÇÕES

def criar_matriz(l, c):
    m = l * [0]  # criando as linhas - lista de fora
    for i in range(l):
        m[i] = c * [0]  # criando as colunas para a i-ésima linha
    return m  # retorna a matriz criada cheia de zeros

import random

def add_novo_numero(tab):
    cont = 0  # conta quantas posições vazias existem

    for i in range(4):
        for j in range(4):
            if tab[i][j] == 0:
                cont = cont + 1

    if cont > 0:
        sorteio = random.randint(1, cont)  # escolhe uma das posições vazias
        pos = 0  # contador das posições vazias encontradas

        for i in range(4):
            for j in range(4):
                if tab[i][j] == 0:
                    pos = pos + 1

                    if pos == sorteio:
                        if random.random() < 0.9: # probabilidade 90%/10%
                            tab[i][j] = 2
                        else:
                            tab[i][j] = 4
                        return tab

    return tab

def imprimir_matriz(m):
    for i in range(len(m)):  # comprimento da lista = total de linhas
        for j in range(len(m[i])):  # comprimento da i-ésima linha = total de colunas
            print(f"{m[i][j]:3}", end=" ")
        print()

def ler_movimento():
    mov=input("Digite o movimento desejado (w/a/s/d): ")
    return mov

#FUNÇÕES CORINGA (para todos os movimentos)

def compactar_linha(linha):
    nova_linha = [0, 0, 0, 0]  # cria uma nova linha vazia
    pos = 0  # posição onde vai colocar os números

    for i in range(4):
        if linha[i] != 0:  # se o número for diferente de zero
            nova_linha[pos] = linha[i]  # coloca na próxima posição livre
            pos = pos + 1  # avança para a próxima posição

    return nova_linha  # retorna a linha compactada


def somar_linha(linha):
    pontos = 0

    for i in range(3):  # vai até a posição 2, comparando com a próxima
        if linha[i] == linha[i + 1] and linha[i] != 0:  # se forem iguais e diferentes de zero
            linha[i] = linha[i] * 2  # dobra o valor da esquerda
            pontos = pontos + linha[i] # atualiza o score após soma
            linha[i + 1] = 0  # zera o valor da direita

    return linha, pontos   # retorna a linha e o score após as somas


def mover_linha_esquerda(linha):
    linha = compactar_linha(linha)  # primeiro empurra tudo para a esquerda
    linha, pontos = somar_linha(linha)  # depois soma os iguais
    linha = compactar_linha(linha)  # compacta de novo para tirar os zeros do meio

    return linha, pontos # retorna a linha final

#FUNÇÕES MOVIMENTO para TABULEIRO

def mover_esquerda(tab):
    total = 0 # acumula os pontos da jogada

    for i in range(4):
        tab[i], pontos = mover_linha_esquerda(tab[i])
        total = total + pontos # soma os pontos

    return tab, total

def mover_direita(tab):
    total = 0 # acumula os pontos da jogada

    for i in range(4):
        linha = tab[i]

        linha = list(reversed(linha))  # inverte
        linha, pontos = mover_linha_esquerda(linha)
        linha = list(reversed(linha))  # inverte de volta

        tab[i] = linha

        total = total + pontos # soma os pontos

    return tab, total

def mover_cima(tab):
    total = 0 # acumula os pontos da jogada

    for j in range(4):  # percorre colunas

        coluna = [0, 0, 0, 0]  # cria coluna vazia

        for i in range(4):
            coluna[i] = tab[i][j]  # copia valores

        coluna, pontos = mover_linha_esquerda(coluna)  # aplica a lógica

        for i in range(4):
            tab[i][j] = coluna[i]  # devolve pro tabuleiro

        total = total + pontos # soma os pontos

    return tab, total

def mover_baixo(tab):
    total = 0 # acumula os pontos da jogada

    for j in range(4):

        coluna = [0, 0, 0, 0]  # cria coluna

        for i in range(4):
            coluna[i] = tab[i][j]  # copia valores

        coluna = list(reversed(coluna))  # inverte
        coluna, pontos = mover_linha_esquerda(coluna)
        coluna = list(reversed(coluna))  # inverte de volta

        for i in range(4):
            tab[i][j] = coluna[i]  # devolve

        total = total + pontos  # soma os pontos

    return tab, total

# VITÓRIA / DERROTA
def verificar_vitoria(tab):
    venceu = False

    for i in range(4):
        for j in range(4):
            if tab[i][j] == 2048:
                venceu = True

    return venceu

def verificar_derrota(tab):
    derrota = True

    for i in range(4): # ainda tem espaço vazio → NÃO perdeu
        for j in range(4):
            if tab[i][j] == 0:
                derrota = False

    for i in range(4): # ainda pode juntar na horizontal → NÃO perdeu
        for j in range(3):
            if tab[i][j] == tab[i][j+1] and tab[i][j] != 0:
                derrota = False

    for i in range(3): # ainda pode juntar na vertical → NÃO perdeu
        for j in range(4):
            if tab[i][j] == tab[i+1][j] and tab[i][j] != 0:
                derrota = False

    return derrota

# AQUI começa o programa principal
score = 0  # guarda a pontuação

tab = criar_matriz(4, 4)  # cria o tabuleiro 4x4

tab = add_novo_numero(tab)  # adiciona o primeiro número
tab = add_novo_numero(tab)  # adiciona o segundo número

jogo_ativo = True
ganhou = False # o jogador AINDA NÃO ganhou

while jogo_ativo:

    print("\nTABULEIRO:")
    imprimir_matriz(tab)
    print("Score:", score)

    movimento = ler_movimento()

    if movimento in ["a", "d", "w", "s"]:

        tab_antes = [linha[:] for linha in tab]
        pontos = 0

        if movimento == "a":
            tab, pontos = mover_esquerda(tab)
        elif movimento == "d":
            tab, pontos = mover_direita(tab)
        elif movimento == "w":
            tab, pontos = mover_cima(tab)
        elif movimento == "s":
            tab, pontos = mover_baixo(tab)

        if tab != tab_antes: # só adiciona se o tabuleiro mudou

            score = score + pontos # atualiza o score

            if verificar_vitoria(tab):
                if ganhou == False:
                    print("\nVOCÊ GANHOU!")
                    ganhou = True

                    continuar_pergunta = True

                    while continuar_pergunta:
                        opcao = input("Deseja continuar jogando? (s/n): ")

                        if opcao == "s" or opcao == "S":
                            continuar_pergunta = False

                        elif opcao == "n" or opcao == "N":
                            print("Parabéns pelo score:", score)
                            jogo_ativo = False
                            continuar_pergunta = False

                        else:
                            print("Digite apenas 's' ou 'n'")

            tab = add_novo_numero(tab)  # add novo numero se não perdeu

            if verificar_derrota(tab): # 💀: verificar derrota DEPOIS de gerar número
                print("\nTABULEIRO FINAL:")
                imprimir_matriz(tab)
                print("GAME OVER!")
                print("Score final:", score)
                jogo_ativo = False

        else:
            print("Movimento não alterou o tabuleiro")

    else:
        print("Movimento inválido")