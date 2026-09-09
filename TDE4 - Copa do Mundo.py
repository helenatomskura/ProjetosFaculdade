import json
import csv

## carrega o conteúdo do arquivo e converte em dicionário
with open('copas_do_mundo_historico.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

def listar_copas(dados): ## listar todas as Copas do Mundo
    print()
    for copa in dados:
        for chave, valor in copa.items():
            print(chave, ": ", valor)
        print("-" * 40)

def buscar_por_ano(dados): ## busca Copa por ano
    ano = input("Qual ano você deseja consultar?: ")
    print()
    for copa in dados:
        if str(copa['Ano']) == ano: ## compara o ano da Copa com o que o usuário digitou
            for chave, valor in copa.items(): ## exibe todos os campos daquela Copa específica
                print(chave, ": ", valor)

def titulos_por_selecao(dados):
    print()
    selecao = input("Digite o nome da seleção: ")
    anos = [] ## cria uma lista vazia, que vai guardar os anos em que esse país foi campeão
    for copa in dados:
        if copa['Campeao'].lower() == selecao.lower(): ## compara o campeão daquela Copa com o que o usuário digitou
            anos.append(copa['Ano']) ## se bateu, adiciona o ano da Copa na lista
    print(selecao, "foi campeã nos anos: ", anos)

def ranking_campeoes(dados):
    print()
    contagem = {} ## cria um dicionário vazio, que vai guardar quantas vezes cada país foi campeão
    for copa in dados:
        campeao = copa['Campeao'] ## pega o nome do campeão daquela Copa
        if campeao in contagem:
            contagem[campeao] = contagem[campeao] + 1
        else:
            contagem[campeao] = 1 ## cria a entrada com valor 1

    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True) ## organiza o ranking de forma decrescente

    for selecao, titulos in ranking:
        print(selecao, ":", titulos, "título(s)")

def participacoes_em_finais(dados):
    print()
    contagem = {} ## guarda quantas vezes cada país foi finalista
    for copa in dados:
        finalistas = [copa['Campeao'], copa['Vice']] ## cria uma lista com os dois times finalistas
        for selecao in finalistas:
            if selecao in contagem:
                contagem[selecao] = contagem[selecao] + 1
            else:
                contagem[selecao] = 1

    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    for selecao, vezes in ranking:
        print(selecao, "participou em:", vezes, "final(is)")

def exportar_csv(dados):
    with open('copas_exportadas.csv', 'w', newline='', encoding='utf-8-sig') as arquivo_csv:
        escritor = csv.writer(arquivo_csv, delimiter=';')
        escritor.writerow(['Ano', 'Campeao', 'Vice', 'Terceiro Lugar']) ## escreve o cabeçalho (ano,campeao,vice,terceiro_lugar)
        for copa in dados:
            escritor.writerow([copa['Ano'], copa['Campeao'], copa['Vice'], copa['Terceiro Lugar']]) ## escreve os dados de uma Copa
    print("✅ Arquivo 'copas_exportadas.csv' foi exportado com sucesso!!")


def menu():
    opcao = ""

    while opcao != "0":
        print("\n======== COPA DO MUNDO ========")
        print("0. 🚪 Sair")
        print("1. 🌍 Listar todas as Copas do Mundo")
        print("2. 📅 Buscar Copa por ano")
        print("3. 🏆 Listar títulos por seleção")
        print("4. 🥇 Mostrar ranking de campeões")
        print("5. 🆚 Consultar participações em finais")
        print("6. 💾 Exportar dados para CSV")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print(" Fim de jogo! 🏁 ")
            break
        elif opcao == "1":
            listar_copas(dados)
        elif opcao == "2":
            buscar_por_ano(dados)
        elif opcao == "3":
            titulos_por_selecao(dados)
        elif opcao == "4":
            ranking_campeoes(dados)
        elif opcao == "5":
            participacoes_em_finais(dados)
        elif opcao == "6":
            exportar_csv(dados)
        else:
            print(" ⚠️  Opção inválida!!  ⚠️ ")

menu()