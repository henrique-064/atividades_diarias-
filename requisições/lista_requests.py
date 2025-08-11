# pasta com os arquivos para requisição de API

import requests
import json

# 1. Função GET


def requisitar_get(url, params=None, headers=None):
    try:
        resposta = requests.get(url, params=params, headers=headers)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"[GET] Erro na requisição: {e}")
        return None

# 2. Função POST


def requisitar_post(url, dados=None, headers=None):
    try:
        resposta = requests.post(url, json=dados, headers=headers)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"[POST] Erro na requisição: {e}")
        return None

# 3. Função DELETE


def requisitar_delete(url, headers=None):
    try:
        resposta = requests.delete(url, headers=headers)
        resposta.raise_for_status()
        return {"status": "sucesso", "codigo": resposta.status_code}
    except requests.exceptions.RequestException as e:
        print(f"[DELETE] Erro na requisição: {e}")
        return None

# 4. função de teste de API


def testar_api(url, params=None, headers=None):
    print(f"\n Testando API: {url}")
    resposta = requisitar_get(url, params=params, headers=headers)

    if resposta is None:
        print(" Nenhuma resposta recebida (possível erro na requisição).")
        return

    print("\n Resposta recebida com sucesso.")
    print(f" Tipo da resposta: {type(resposta).__name__}")

    # Caso a resposta seja um dicionário (objeto JSON)
    if isinstance(resposta, dict):
        print("\n Chaves principais encontradas:")
        for chave in resposta:
            print(f"  - {chave}")

        # mostra quais são as chaves da API
        lista_chave = None
        for chave in resposta:
            if isinstance(resposta[chave], list):
                lista_chave = chave
                break

        # Tenta detectar se há listas internas (ex: "data", "results", etc.)
        lista_chave = None
        for chave in resposta:
            if isinstance(resposta[chave], list):
                lista_chave = chave
                break

        if lista_chave:
            print(f"\n A chave '{lista_chave}' contém uma lista com {len(resposta[lista_chave])} itens.")
            primeiro_item = resposta[lista_chave][0]
            print("- Exemplo do primeiro item:")
            print(json.dumps(primeiro_item, indent=4, ensure_ascii=False))

            if isinstance(primeiro_item, dict):
                print("\n Exemplo de acesso ao nome de uma fruta (se existir):")
                for campo in ['nome', 'name', 'fruta']:
                    if campo in primeiro_item:
                        print(f"  → item['{campo}'] = {primeiro_item[campo]}")
                        break
                    elif 'fruta' in primeiro_item and isinstance(primeiro_item['fruta'], dict):
                        fruta = primeiro_item['fruta']
                        if 'nome' in fruta:
                            print(f"  → item['fruta']['nome'] = {fruta['nome']}")
                            break
        else:
            print("\n Nenhuma lista encontrada diretamente na resposta.")
            print("Conteúdo completo:")
            print(json.dumps(resposta, indent=4, ensure_ascii=False))

    # Caso a resposta seja uma lista direta
    elif isinstance(resposta, list):
        print(f"\n A resposta é uma lista com {len(resposta)} itens.")
        print("- Exemplo do primeiro item:")
        print(json.dumps(resposta[0], indent=4, ensure_ascii=False))

        if isinstance(resposta[0], dict):
            print("\n Exemplo de acesso ao nome de uma fruta (se existir):")
            if 'nome' in resposta[0]:
                print(f"  → item['nome'] = {resposta[0]['nome']}")

    # Caso a resposta seja string, número, ou outro
    else:
        print("\n Resposta em formato inesperado:")
        print(resposta)
