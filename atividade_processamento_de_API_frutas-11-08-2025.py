import requests
from requisições.lista_requests import requisitar_get , testar_api

url = "https://securitylogs.pythonanywhere.com/frutas"

resultado = requisitar_get(url)

if resultado and "data" in resultado:
    for item in resultado["data"]:
        fruta = item.get("fruta", {})
        print(f"Nome: {fruta.get('nome', 'N/A')}")
        print(f"Cor: {fruta.get('cor', 'N/A')}")
        print(f"Origem: {fruta.get('origem', 'N/A')}")
        print(f"Tipo: {fruta.get('tipo', 'N/A')}")
        print(f"Vitamina Principal: {fruta.get('vitamina_principal', 'N/A')} \n")
else:
    print("Nenhum dado encontrado ou erro na requisição.")

print(testar_api(url))
