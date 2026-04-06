import requests
import matplotlib.pyplot as plt

# Lista de CEPs
CEPS = [
    "01001-000", "01310-000", "02011-000", "03345-000", "04567-000","88010-000","89201-000","88330-000",
    "20010-000", "20550-000", "22290-240", "22775-040","30110-000", "31030-000", "31515-000","70040-010",
    "70800-000","40010-000", "41820-000", "41950-000","80010-000", "80530-000","90010-000", "90450-000",
    "88010-000","60010-000", "60830-000","50010-000", "50740-000","69005-000", "69085-000","66010-000",
    "64000-000","59010-000","57010-000","49010-000","77001-000","76801-000","69301-000","68900-000",
    "75000-000", "75800-000","78005-000", "78700-000","79002-000","65010-000","69900-000","68005-000"
]

# Mapeamento de estados para regiões
REGIOES = {
    "Norte": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"],
    "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "Centro-Oeste": ["DF", "GO", "MT", "MS"],
    "Sudeste": ["SP", "RJ", "MG", "ES"],
    "Sul": ["PR", "RS", "SC"]
}

# Função para consultar API ViaCEP
def buscar_endereco(cep):
    cep = cep.replace("-", "").strip()

    if len(cep) != 8 or not cep.isdigit():
        print(f"CEP inválido: {cep}")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print(f"CEP não encontrado: {cep}")
            return None
        return dados
    except requests.exceptions.RequestException:
        print(f"Erro na requisição do CEP: {cep}")
        return None

# Agrupar por estado
def agrupar_por_estado(ceps):
    resultado = {}

    for cep in ceps:
        endereco = buscar_endereco(cep)
        if endereco:
            uf = endereco["uf"]
            if uf not in resultado:
                resultado[uf] = []
            resultado[uf].append(endereco)
    return resultado

# Agrupar por região
def agrupar_por_regiao(dados_por_estado):
    dados_regiao = {}
    for regiao, estados in REGIOES.items():
        dados_regiao[regiao] = []
        for uf in estados:
            if uf in dados_por_estado:
                dados_regiao[regiao].extend(dados_por_estado[uf])
    return dados_regiao

# Salvar arquivos por região
def salvar_por_regiao(dados_regiao):
    for regiao, enderecos in dados_regiao.items():
        nome_arquivo = f"entregas_{regiao}.txt"

        with open(nome_arquivo, "w", encoding="utf-8") as f:
            for e in enderecos:
                linha = f"{e['cep']} - {e['logradouro']} - {e['localidade']}/{e['uf']}\n"
                f.write(linha)
