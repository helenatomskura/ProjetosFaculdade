import random

print()
print("Bem vindo ao jogo da forca!")
print()

lista_escolhida = []

paises = {
    "africa": [
        "africa do sul", "angola", "argelia", "benim", "botsuana", "burquina faso",
        "burundi", "cabo verde", "camaroes", "chad", "comores", "congo", "costa do marfim",
        "djibuti", "egito", "eritreia", "etiopia", "gabao", "gambia", "gana", "guine",
        "guine equatorial", "guine bissau", "lesoto", "liberia", "libia", "madagascar",
        "malaui", "mali", "marrocos", "mauricio", "mauritania", "mocambique", "namibia",
        "niger", "nigeria", "quenia", "republica centro africana", "ruanda", "sao tome e principe",
        "senegal", "serra leoa", "somalia", "sudao", "sudao do sul", "tanzania", "togo",
        "tunisia", "uganda", "zambia", "zimbabue"
    ],
    "america": [
        "antigua e barbuda", "argentina", "bahamas", "barbados", "belize", "bolivia",
        "brasil", "canada", "chile", "colombia", "costa rica", "cuba", "dominica",
        "equador", "el salvador", "estados unidos", "granada", "guatemala", "guiana",
        "haiti", "honduras", "jamaica", "mexico", "nicaragua", "panama", "paraguai",
        "peru", "republica dominicana", "santa lucia", "sao cristovao e neves",
        "sao vicente", "suriname", "trindade e tobago", "uruguai", "venezuela"
    ],
    "asia": [
        "afeganistao", "arabia saudita", "armenia", "azerbaijao", "barem", "bangladesh",
        "brunei", "butao", "camboja", "catar", "cazaquistao", "china", "chipre",
        "coreia do norte", "coreia do sul", "emirados arabes", "filipinas", "georgia",
        "iemen", "india", "indonesia", "ira", "iraque", "israel", "japao", "jordania",
        "kuwait", "laos", "libano", "malasia", "maldivas", "mianmar", "mongolia",
        "nepal", "oma", "paquistao", "palestina", "quirguistao", "singapura", "siria",
        "sri lanka", "tailandia", "taiwan", "tajiquistao", "timor leste", "turcomenistao",
        "turquia", "uzbequistao", "vietna"
    ],
    "europa": [
        "albania", "alemanha", "andorra", "austria", "belgica", "bielorrussia",
        "bosnia e herzegovina", "bulgaria", "croacia", "dinamarca", "eslovaquia",
        "eslovenia", "espanha", "estonia", "finlandia", "franca", "grecia", "holanda",
        "hungria", "irlanda", "islandia", "italia", "letonia", "liechtenstein",
        "lituania", "luxemburgo", "macedonia do norte", "malta", "moldavia", "monaco",
        "montenegro", "noruega", "polonia", "portugal", "reino unido", "republica checa",
        "romenia", "russia", "sao marinho", "servia", "suecia", "suica", "ucrania", "vaticano"
    ],
    "oceania": [
        "australia", "fiji", "ilhas marshall", "ilhas salomao", "kiribati", "micronesia",
        "nauru", "nova zelandia", "palau", "papua nova guine", "samoa", "seicheles",
        "tonga", "tuvalu", "vanuatu"
    ]
}

estados = [
    "acre", "alagoas", "amapa", "amazonas", "bahia", "ceara", "distrito federal",
    "espirito santo", "goias", "maranhao", "mato grosso", "mato grosso do sul",
    "minas gerais", "para", "paraiba", "parana", "pernambuco", "piaui",
    "rio de janeiro", "rio grande do norte", "rio grande do sul", "rondonia",
    "roraima", "santa catarina", "sao paulo", "sergipe", "tocantins"
]

cidades = [
    "aracaju", "belem", "belo horizonte", "boa vista", "brasilia", "campo grande",
    "cuiaba", "curitiba", "florianopolis", "fortaleza", "goiania", "joao pessoa",
    "maceio", "manaus", "natal", "palmas", "porto alegre", "porto velho", "recife",
    "rio branco", "rio de janeiro", "salvador", "sao luis", "sao paulo", "teresina",
    "vitoria", "gramado", "porto seguro", "paraty", "bonito", "foz do iguacu",
    "buzios", "angra dos reis", "caldas novas", "ouro preto", "holambra",
    "petropolis", "campos do jordao", "maragogi", "itacare", "pirenopolis",
    "jericoacoara", "pipa", "canela", "tiradentes", "diamantina", "balneario camboriu",
    "capitolio", "lencois", "salinopolis"
]

# lista ASCII ART
desenho_forca = [
    """
       +---+
       |   |
           |
           |
           |
           |
    ========= """, """
       +---+
       |   |
       O   |
           |
           |
           |
    ========= """, """
       +---+
       |   |
       O   |
       |   |
           |
           |
    ========= """, """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    ========= """, """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    ========= """, """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    ========= """, """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========= """
]

# AQUI começa o programa
# Parte do MENU
print("Escolha a categoria que deseja joga:")
print("1. Países do Mundo")
print("2. Estados brasileiros")
print("3. Cidades brasileiras")
print()

escolha = (input("Digite sua escolha:"))
print()

if escolha == "1":
    print("Países de qual continente?")
    print("1. America")
    print("2. Europa")
    print("3. Asia")
    print("4. Africa")
    print("5. Oceania")
    print()

    secondesc = (input("Digite sua escolha:"))

    if secondesc == "1":
        lista_escolhida = paises["america"]
    elif secondesc == "2":
        lista_escolhida = paises["europa"]
    elif secondesc == "3":
        lista_escolhida = paises["asia"]
    elif secondesc == "4":
        lista_escolhida = paises["africa"]
    elif secondesc == "5":
        lista_escolhida = paises["oceania"]

elif escolha == "2":
    lista_escolhida = estados

elif escolha == "3":
    lista_escolhida = cidades

pos = random.randint(0, len(lista_escolhida)- 1) # -1 evita erro pq a lista começa em 0
segredo = lista_escolhida[pos]

print(segredo) # debug

# LOOP JOGO
# variavéis
vidas = 6
letras_corretas = []
letras_erradas = []
tela = ["_"] * len(segredo) # cria lista

ganhou = False

for i in range(len(segredo)): # o espaço da palavra é preenchido com "_"
    if segredo[i] == " ":
        tela[i] = " "

# loop
while vidas > 0 and ganhou == False:
    print(desenho_forca[6 - vidas]) # mostra o estágio do desenho usando a diferença entre o total de vidas e as atuais
    print("\nVidas:", vidas)

    print("Letras corretas:", end="")
    for letra in letras_corretas:
        print(letra, end=" ")
    print()

    print("Letras erradas:", end="")
    for letra in letras_erradas:
        print(letra, end=" ")
    print()

    for letra in tela:
        print(letra, end=" ")
    print()

    tentativa = input("Digite uma letra: ").lower().strip()
    print()

    if tentativa in letras_corretas or tentativa in letras_erradas:
        print("Você já usou essa letra!")
        continue

    if tentativa in segredo:
        print("Você acertou uma letra!")
        letras_corretas.append(tentativa)  # Vai para a lista de acertos
        for i in range(len(segredo)):
            if segredo[i] == tentativa:
                tela[i] = tentativa
        if "_" not in tela: # vitória
            ganhou = True
    else:
        print("Essa letra não existe! Tente novamente!")
        letras_erradas.append(tentativa)  # Vai para a lista de erros
        vidas -= 1

if ganhou:
    print("\n*******************************")
    print("\nPARABÉNS! Você venceu!")
    print("A palavra secreta era:", segredo)
    print("\n*******************************")
else:
    print(desenho_forca[6])
    print("\n*******************************")
    print("\nVocê perdeu...")
    print("A palavra correta era:", segredo)
    print("\n*******************************")