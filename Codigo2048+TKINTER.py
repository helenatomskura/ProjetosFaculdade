import tkinter as tk
import random

# DICIONÁRIO CORES usando códigos hexadecimais
cores = {
    0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
    128: "#edcf72", 256: "#edcc61", 512: "#edc850",
    1024: "#edc53f", 2048: "#edc22e"
}

# FUNÇÕES

def criar_matriz(l, c):
    m = l * [0] # criando as linhas - lista de fora
    for i in range(l):
        m[i] = c * [0] # criando as colunas para a i-ésima linha
    return m # retorna a matriz criada cheia de zeros

def add_novo_numero(tab):
    cont = 0 # conta quantas posições vazias existem

    for i in range(4):
        for j in range(4):
            if tab[i][j] == 0:
                cont = cont + 1

    if cont > 0:
        sorteio = random.randint(1, cont) # escolhe uma das posições vazias
        pos = 0 # contador das posições vazias encontradas // encontrar a posição que foi sorteada

        for i in range(4):
            for j in range(4):
                if tab[i][j] == 0:
                    pos = pos + 1

                    if pos == sorteio:
                        if random.random() < 0.9:  # probabilidade 90%/10%
                            tab[i][j] = 2
                        else:
                            tab[i][j] = 4
                        return tab

        return tab

# FUNÇÕES CORINGA (para todos os movimentos)

def compactar_linha(linha):
    nova_linha = [0, 0, 0, 0] # cria uma nova linha vazia
    pos = 0 # posição onde vai colocar os números

    for i in range(4):
        if linha[i] != 0: # se o número for diferente de zero
            nova_linha[pos] = linha[i] # coloca na próxima posição livre
            pos = pos + 1  # avança para a próxima posição

    return nova_linha # retorna a linha compactada

def somar_linha(linha):
    pontos = 0

    for i in range(3):   # vai até a posição 2, comparando com a próxima
        if linha[i] == linha[i + 1] and linha[i] != 0:   # se forem iguais e diferentes de zero
            linha[i] *= 2  # dobra o valor da esquerda
            pontos = pontos + linha[i] # atualiza o score após soma
            linha[i + 1] = 0 # zera o valor da direita

    return linha, pontos # retorna a linha e o score após as somas

def mover_linha_esquerda(linha):
    linha = compactar_linha(linha) # empurra tudo para a esquerda
    linha, pontos = somar_linha(linha) # depois soma os iguais
    linha = compactar_linha(linha) # compacta de novo para tirar os zeros do meio

    return linha, pontos  # retorna a linha final

# FUNÇÕES MOVIMENTO para TABULEIRO

def mover_esquerda(tab):
    total = 0 # acumula os pontos da jogada

    for i in range(4):
        tab[i], pontos = mover_linha_esquerda(tab[i])
        total = total + pontos # soma os pontos
    return tab, total

def mover_direita(tab):
    total = 0 # acumula os pontos da jogada

    for i in range(4):
        linha = list(reversed(tab[i])) # inverte a linha do tabuleiro
        linha, pontos = mover_linha_esquerda(linha)
        tab[i] = list(reversed(linha)) # inverte de volta

        total = total + pontos # soma os pontos

    return tab, total

def mover_cima(tab):
    total = 0  # acumula os pontos da jogada

    for j in range(4): # percorre colunas

        coluna = [0, 0, 0, 0]  # cria coluna vazia

        for i in range(4):
            coluna[i] = tab[i][j]  # copia valores

        coluna, pontos = mover_linha_esquerda(coluna) # aplica a lógica
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

        coluna = list(reversed(coluna)) # inverte
        coluna, pontos = mover_linha_esquerda(coluna)
        coluna = list(reversed(coluna)) # inverte de volta

        for i in range(4):
            tab[i][j] = coluna[i] # devolve

        total = total + pontos  # soma os pontos

    return tab, total

# VITÓRIA / DERROTA
venceu = False
perdeu = False

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

# AQUI começa o programa principal + TKINTER

janela = tk.Tk()
janela.title("2048")

# MATRIZ DO JOGO
tab = criar_matriz(4, 4)
tab = add_novo_numero(tab)
tab = add_novo_numero(tab)

score = 0  # variável de pontuação

# SCORE
# Label que mostra a pontuação do jogador
score_label = tk.Label(janela, text="Score: 0", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=4)

# RESULTADO
# Label que mostra vitória ou derrota
resultado = tk.Label(janela, text="", font=("Arial", 16))
resultado.grid(row=5, column=0, columnspan=4)

# TABULEIRO
labels = []

for i in range(4):
    linha = []
    for j in range(4):

        lbl = tk.Label(
            janela,
            text="",
            width=6,
            height=3,
            font=("Arial", 20),
            bg="lightgray",
            relief="ridge",  # borda do quadrado
            bd=5             # espessura da borda
        )

        lbl.grid(row=i, column=j, padx=5, pady=5)
        linha.append(lbl)

    labels.append(linha)

# ATUALIZAR TELA
def atualizar_tela():
    for i in range(4):
        for j in range(4):

            valor = tab[i][j]  # pega valor da matriz

            cor = cores.get(valor, "#3c3a32") # pega cor correspondente ao valor (ou padrão se for grande)

            if valor == 0:
                labels[i][j].config(text="", bg=cor) # se for zero → não mostra número
            else:
                labels[i][j].config(text=str(valor), bg=cor) # mostra número e muda a cor do quadrado

    score_label.config(text="Score: " + str(score)) # atualiza o score na tela

# MOVIMENTO COM TECLADO
def tecla(event):
    global tab, score, venceu, perdeu

    if venceu or perdeu:
        return  # bloqueia jogadas após fim de jogo

    tecla = event.keysym.lower() # transforma tecla em minúscula (aceita W ou w)

    pontos = 0
    tab_antes = [linha[:] for linha in tab] # cópia do tabuleiro para comparar depois

    if tecla == "a":
        tab, pontos = mover_esquerda(tab)
    elif tecla == "d":
        tab, pontos = mover_direita(tab)
    elif tecla == "w":
        tab, pontos = mover_cima(tab)
    elif tecla == "s":
        tab, pontos = mover_baixo(tab)

    if tab != tab_antes: # só executa se o tabuleiro mudou
        score = score + pontos  # soma os pontos

        if verificar_vitoria(tab) and not venceu: # se ganhou e ainda não tinha sido marcado como vitória
            venceu = True
            resultado.config(text="🎉 VOCÊ GANHOU!")

        tab = add_novo_numero(tab)  # adiciona novo número

        if verificar_derrota(tab) and not perdeu: # se perdeu e ainda não tinha sido marcado como derrota
            perdeu = True
            resultado.config(text="💀 GAME OVER!")

        atualizar_tela()  # atualiza interface

janela.bind("<Key>", tecla) # conecta teclado ao jogo
atualizar_tela() # mostra estado inicial
janela.mainloop() # mantém a janela aberta