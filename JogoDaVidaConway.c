#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int** criar_matriz(int altura, int largura);
int** ler_arq(const char* nome, int* altura, int* largura);
void liberar_matriz(int** m, int altura);
int contar_vivas(int** m, int altura, int largura);
void imprimir_geracao(int** m, int altura, int largura, int geracao, int vivas);
int contar_vizinhos(int** m, int altura, int largura, int i, int j);
int** proxima_geracao(int** m_atual, int altura, int largura);

// FUNÇÃO PRINCIPAL
int main() {
    char nome_arq[100];
    int altura = 0;
    int largura = 0;
    int** matrizA = NULL;
    int num_geracoes = 0;
    int jogar_novamente;
    int velocidade = 0;

    do { 
        printf("Insira o nome do arquivo: ");
        scanf("%s", nome_arq);

        matrizA = ler_arq(nome_arq, &altura, &largura);

        if (matrizA == NULL) {
            printf("Deseja tentar novamente? (1-Sim / 0-Nao): ");
            scanf("%d", &jogar_novamente);
            continue; // volta pro inicio do loop
        }

        printf("Arquivo '%s' aberto com sucesso!\n", nome_arq);
        printf("Altura = %d, Largura = %d\n", altura, largura);

        printf("Quantas geracoes deseja simular? ");
        scanf("%d", &num_geracoes);

        printf("Qual a velocidade entre as geracoes? (ex: 100ms-rapido / 300ms-medio / 500ms-lento): ");
        scanf("%d", &velocidade);

        int vivas = contar_vivas(matrizA, altura, largura);  // imprime geração inicial (g=0)
        imprimir_geracao(matrizA, altura, largura, 0, vivas);
        Sleep(velocidade); // espera antes de entrar no loop

        for (int g = 1; g <= num_geracoes; g++) {
            int** nova = proxima_geracao(matrizA, altura, largura);
            liberar_matriz(matrizA, altura);
            matrizA = nova;

            system("cls");  // apaga tela depois de esperar
            vivas = contar_vivas(matrizA, altura, largura);
            imprimir_geracao(matrizA, altura, largura, g, vivas);
            Sleep(velocidade); // espera depois de imprimir
        }

        printf("Jogo encerrado! %d geracoes executadas.\n", num_geracoes);
        liberar_matriz(matrizA, altura); // libera a memória

        printf("\nDeseja jogar novamente? (1-Sim / 0-Nao): ");
        scanf("%d", &jogar_novamente);
        system("cls");

    } while (jogar_novamente == 1);
    
    return 0;
}

// FUNÇÕES AUXILIARES
int** criar_matriz(int altura, int largura) {
    int** m = calloc(altura, sizeof(int*)); //linhas zeradas
    for (int i = 0; i < altura; i++) { //colunas zeradas
        m[i] = calloc(largura, sizeof(int)); 
    }
    return m;
}

int** ler_arq(const char* nome, int* altura, int* largura) {
    FILE* f = fopen(nome, "r");
    if (f == NULL) {
        printf("Arquivo '%s' nao encontrado.\n", nome);
        return NULL;
    }

    fscanf(f, "%d", altura);
    fscanf(f, "%d", largura); 

    int** m = criar_matriz(*altura, *largura);

    for (int i = 0; i < *altura; i++) {
        for (int j = 0; j < *largura; j++) {
            char c;
            fscanf(f, " %c", &c); // lê caractere por caractere ignorando \n
            m[i][j] = c - '0';    // converte '0' ou '1' para inteiro 0 ou 1
        }
    }

    fclose(f);
    return m;
}

void liberar_matriz(int** m, int altura) {
    for (int i = 0; i < altura; i++)
        free(m[i]); // libera cada linha
    free(m);        // libera o array de ponteiros
}

int contar_vivas(int** m, int altura, int largura) {
    int count = 0;
    for (int i = 0; i < altura; i++)
        for (int j = 0; j < largura; j++)
            if (m[i][j] == 1) //significa que a celula está viva
                count++;
    return count;
}

void imprimir_geracao(int** m, int altura, int largura, int geracao, int vivas) {
    printf("Geracao: %d | Celulas vivas: %d\n\n", geracao, vivas);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (m[i][j] == 1)
                printf("\xDB "); // célula viva
            else //se encontrar zero
                printf(". "); // célula morta
        }
        printf("\n");
    }
}

int contar_vizinhos(int** m, int altura, int largura, int i, int j) {
    int count = 0;
    for (int desi = -1; desi <= 1; desi++) {       // desloca linha: -1, 0, +1
        for (int desj = -1; desj <= 1; desj++) {   // desloca coluna: -1, 0, +1
            if (desi == 0 && desj == 0) continue; // ignora a própria célula

            int newi = i + desi; // linha do vizinho
            int newj = j + desj; // coluna do vizinho

            if (newi >= 0 && newi < altura && newj >= 0 && newj < largura) // só conta se estiver dentro dos limites
                count += m[newi][newj]; // soma 1 se viva, 0 se morta
        }
    }
    return count;
}

int** proxima_geracao(int** m_atual, int altura, int largura) {
    int** m_new = criar_matriz(altura, largura); // cria matriz nova zerada

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            int v = contar_vizinhos(m_atual, altura, largura, i, j);

            //aplica as regras do jogo
            if (m_atual[i][j] == 1) { // célula VIVA
                if (v == 2 || v == 3)
                    m_new[i][j] = 1;     // tem 2 ou 3 vizinhos, sobrevive
                else
                    m_new[i][j] = 0;     // morre
            } else {  // célula MORTA
                if (v == 3)
                    m_new[i][j] = 1;    // célula com exatamente 3 vizinhos, nasce
                else
                    m_new[i][j] = 0;    // continua morta
            }
        }
    }
    return m_new; // retorna a nova geração
}