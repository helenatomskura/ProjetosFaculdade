#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// VARIAVEIS GLOBAIS - Intensidade dos pixels
const char PALETA[] = "@#S%?*+;:,. "; // escuro para mais claro
const int TAM_PALETA = 12;

// PROTÓTIPOS DAS FUNÇÕES
int verificar_ppm(FILE *arq, int *largura, int *altura);
unsigned char *ler_pixels(FILE *arq, int largura, int altura);
float calcular_brilho(unsigned char r, unsigned char g, unsigned char b);
char pixel_para_ascii(float brilho);
void converter_ppm_para_ascii(const char *nome_arquivo);


// FUNÇÃO PRINCIPAL
int main() {
    char nome_arq[256]; // 1byte = 8bits = 256valores(0 a 255valores) + \0

    printf("=== Bem Vindo ao ASCII Art Creator ===\n");
    printf("Digite o nome do arquivo PPM: ");
    scanf("%s", nome_arq);

    converter_ppm_para_ascii(nome_arq);

    return 0;
}

//FUNÇÕES
int verificar_ppm(FILE *arq, int *largura, int *altura) {
    char tipo_arq[3];
    int max_val;
    
    fscanf(arq, "%2s", tipo_arq); // lê os 2 primeiros caracteres do arquivo
    
    if (strcmp(tipo_arq, "P6") != 0) { // compara com "P6" que seria um arq.PPM binário (colorido) 
        printf("Erro! Nao e um arquivo PPM valido!\n");
        return 0; // falhou
    }
    
    fscanf(arq, "%d %d %d", largura, altura, &max_val); // lê largura, altura e valor máximo de cor do cabeçalho
    fgetc(arq); // consome o '\n' após o cabeçalho
    
    return 1; // sucesso
}

unsigned char *ler_pixels(FILE *arq, int largura, int altura) { // aloca memória: cada pixel tem 3 bytes (R, G, B)
    unsigned char *pixels;

    pixels = malloc(largura * altura * 3); // largura * altura = total de pixels | * 3 = bytes por pixel (R, G, B)
    
    if (!pixels) {
        printf("Erro! Memoria insuficiente!\n");
        return NULL;
    }
    
    // lê todos os pixels de uma vez do arquivo binário
    fread(pixels, 3, largura * altura, arq);
    
    return pixels; // retorna o ponteiro para os pixels
}

float calcular_brilho(unsigned char r, unsigned char g, unsigned char b) {
    float brilho;
    brilho = 0.299f * r + 0.587f * g + 0.114f * b; // verde contribui mais para o brilho percebido
    return brilho;
}

char pixel_para_ascii(float brilho) { // converte um valor de brilho (0-255) para o caractere ASCII correspondente
    int indice;
    indice = (int)(brilho / 255.0f * (TAM_PALETA - 1));
    return PALETA[indice];
}

void converter_ppm_para_ascii(const char *nome_arquivo) { // abre o arquivo, lê os pixels e gera o ASCII Art
    int largura, altura;
    int passo;
    int x, y, idx;
    unsigned char *pixels;
    unsigned char r, g, b;
    float brilho;
    char c;
    char nome_saida[256];
    char *ponto;

    // 1. abre o arquivo PPM em modo binário
    FILE *arq = fopen(nome_arquivo, "rb");
    if (!arq) { 
        printf("Erro! Arquivo nao encontrado!\n"); 
        return; 
    }

    // 2. verifica se é PPM e lê dimensões
    if (!verificar_ppm(arq, &largura, &altura)) {
        fclose(arq);
        return;
    }

    // 3. lê os pixels
    pixels = ler_pixels(arq, largura, altura);
    fclose(arq);
    if (!pixels) return;

    // 4. monta o nome do arquivo de saída (troca extensão por .txt)
    strcpy(nome_saida, nome_arquivo);
    ponto = strrchr(nome_saida, '.'); // acha o último ponto
    if (ponto) strcpy(ponto, ".txt"); // substitui extensão por .txt
    else strcat(nome_saida, ".txt"); // se não tiver extensão, adiciona .txt

    FILE *saida = fopen(nome_saida, "w");

    // 5. percorre os pixels e converte
    passo = 2; // pula pixels pra imagem não ficar gigante
    for (y = 0; y < altura; y += passo) {
        for (x = 0; x < largura; x += passo) {
            idx = (y * largura + x) * 3; // calcula posição do pixel no array
            
            // extrai os 3 canais de cor do pixel
            r = pixels[idx];
            g = pixels[idx + 1];
            b = pixels[idx + 2];

            brilho = calcular_brilho(r, g, b);
            c = pixel_para_ascii(brilho);

            // imprime 2x para compensar que caracteres são mais altos que largos
            printf("%c%c", c, c);
            if (saida) fprintf(saida, "%c%c", c, c);
        }
        printf("\n");
        if (saida) fprintf(saida, "\n");
    }

    free(pixels); // libera a memória alocada
    if (saida) fclose(saida); // fecha o arquivo de saída
    printf("\nSalvo em: %s\n", nome_saida);
}