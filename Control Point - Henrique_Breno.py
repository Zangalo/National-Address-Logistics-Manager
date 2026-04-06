import requests
import matplotlib.pyplot as plt

# Gráfico de pizza
def gerar_grafico(dados):
    estados = list(dados.keys())
    quantidades = [len(lista) for lista in dados.values()]

    plt.figure(figsize=(8, 8))
    plt.pie(quantidades, labels=estados, autopct="%1.1f%%", startangle=90)
    plt.title("Distribuição de Encomendas por Estado")
    plt.axis("equal")
    plt.show()

# Programa principal
def main():
    dados = agrupar_por_estado(CEPS)

    print("\n Resumo:")
    for uf, lista in dados.items():
        print(f"{uf}: {len(lista)} endereços")

    salvar_por_estado(dados)
    gerar_grafico(dados)

if _name_ == "_main_":
    main()
