import requests

#Lista de CEPs
CEPS = [
    "01001000",
    "20040002",
    "30140071",
    "40010000",
    "70040900",
    "80010000",
    "90010000",
    "69005000",
    "66010000",
    "64000000",
    "69050510"
]

#Função para consultar API ViaCEP
def buscar_endereco(cep):
    cep = cep.replace("-", "").strip()

    # Validação simples
    if len(cep) != 8 or not cep.isdigit():
        print(f"CEP inválido: {cep}")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()

        # ViaCEP retorna {"erro": true} se não existir
        if "erro" in dados:
            print(f"CEP não encontrado: {cep}")
            return None

        return dados

    except requests.exceptions.RequestException:
        print(f"Erro na requisição do CEP: {cep}")
        return None
