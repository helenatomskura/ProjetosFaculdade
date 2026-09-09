#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

#define MAX 100
#define TAM 30

void desenho_forca(int estagio);

int main() {
    srand(time(NULL));

    printf("\nBem vindo ao jogo da forca!\n\n");

    char lista_escolhida[MAX][TAM];
    int total_palavras = 0;

    char america[][TAM] = {
        "brasil","argentina","canada","mexico","chile","peru","colombia","uruguai","venezuela"
    };

    char europa[][TAM] = {
        "franca","italia","alemanha","portugal","espanha","holanda","belgica","noruega"
    };

    char asia[][TAM] = {
        "china","japao","india","coreia do sul","tailandia","indonesia"
    };

    char africa[][TAM] = {
        "egito","angola","nigeria","marrocos","quenia","tunisia"
    };

    char oceania[][TAM] = {
        "australia","nova zelandia","fiji","tonga"
    };

    char estados[][TAM] = {
        "parana","sao paulo","bahia","amazonas","mato grosso"
    };

    char cidades[][TAM] = {
        "curitiba","salvador","maceio","palmas","fortaleza"
    };

    // menu
    printf("Escolha a categoria que deseja joga:\n");
    printf("1. Paises do Mundo\n");
    printf("2. Estados brasileiros\n");
    printf("3. Cidades brasileiras\n\n");

    int escolha;
    printf("Insira sua escolha: ");
    scanf("%d", &escolha);

    if (escolha == 1) {
        printf("\nPaises de qual continente?\n");
        printf("1. America\n");
        printf("2. Europa\n");
        printf("3. Asia\n");
        printf("4. Africa\n");
        printf("5. Oceania\n\n");

        int secondesc;
        printf("Insira sua escolha: ");
        scanf("%d", &secondesc);

        if (secondesc == 1) {
            total_palavras = sizeof(america)/sizeof(america[0]);
            for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], america[i]);
        }
        else if (secondesc == 2) {
            total_palavras = sizeof(europa)/sizeof(europa[0]);
            for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], europa[i]);
        }
        else if (secondesc == 3) {
            total_palavras = sizeof(asia)/sizeof(asia[0]);
            for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], asia[i]);
        }
        else if (secondesc == 4) {
            total_palavras = sizeof(africa)/sizeof(africa[0]);
            for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], africa[i]);
        }
        else if (secondesc == 5) {
            total_palavras = sizeof(oceania)/sizeof(oceania[0]);
            for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], oceania[i]);
        }
    }
    else if (escolha == 2) {
        total_palavras = sizeof(estados)/sizeof(estados[0]);
        for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], estados[i]);
    }
    else if (escolha == 3) {
        total_palavras = sizeof(cidades)/sizeof(cidades[0]);
        for(int i=0;i<total_palavras;i++) strcpy(lista_escolhida[i], cidades[i]);
    }

    int pos = rand() % total_palavras;
    char segredo[TAM];
    strcpy(segredo, lista_escolhida[pos]);

    printf("%s\n", segredo); //debug

    // variáveis
    int vidas = 6;
    char letras_corretas[50] = "";
    char letras_erradas[50] = "";
    char tela[TAM];
    int ganhou = 0;

    int tam = strlen(segredo);

    // tela
    for(int i=0;i<tam;i++){
        if(segredo[i]==' ') tela[i] = ' ';
        else tela[i] = '_';
    }
    tela[tam] = '\0';

    // loop
    while(vidas > 0 && !ganhou){
        desenho_forca(6 - vidas);

        printf("\nVidas: %d\n", vidas);

        printf("Letras corretas: %s\n", letras_corretas);
        printf("Letras erradas: %s\n", letras_erradas);

        for(int i=0;i<tam;i++) printf("%c ", tela[i]);
        printf("\n");

        printf("Digite uma letra: ");
        char tentativa;
        scanf(" %c", &tentativa);
        tentativa = tolower(tentativa);

        if(strchr(letras_corretas, tentativa) || strchr(letras_erradas, tentativa)){
            printf("Voce ja usou essa letra!\n");
            continue;
        }

        if(strchr(segredo, tentativa)){
            printf("Voce acertou uma letra!\n");

            int len = strlen(letras_corretas);
            letras_corretas[len] = tentativa;
            letras_corretas[len+1] = ' ';
            letras_corretas[len+2] = '\0';

            for(int i=0;i<tam;i++){
                if(segredo[i] == tentativa){
                    tela[i] = tentativa;
                }
            }

            if(strchr(tela, '_') == NULL){
                ganhou = 1;
            }
        }
        else{
            printf("Essa letra nao existe! Tente novamente!\n");

            int len = strlen(letras_erradas);
            letras_erradas[len] = tentativa;
            letras_erradas[len+1] = ' ';
            letras_erradas[len+2] = '\0';

            vidas--;
        }
    }

    // mensagem finalizando
    if(ganhou){
        printf("\n*******************************\n");
        printf("\nPARABENS! Voce venceu!\n");
        printf("A palavra secreta era: %s\n", segredo);
        printf("\n*******************************\n");
    }
    else{
        desenho_forca(6);
        printf("\n*******************************\n");
        printf("\nVoce perdeu...\n");
        printf("A palavra correta era: %s\n", segredo);
        printf("\n*******************************\n");
    }

    return 0;
}

// boneco forca
void desenho_forca(int estagio) {
    printf("   +---+\n");
    printf("   |   |\n");

    // cabeça
    if (estagio >= 1) printf("   O   |\n");
    else printf("       |\n");

    // tronco e braços
    if (estagio == 2) printf("   |   |\n");
    else if (estagio == 3) printf("  /|   |\n");
    else if (estagio >= 4) printf("  /|\\  |\n");
    else printf("       |\n");

    // pernas
    if (estagio == 5) printf("  /    |\n");
    else if (estagio >= 6) printf("  / \\  |\n");
    else printf("       |\n");

    printf("       |\n");
    printf("=========\n");
}