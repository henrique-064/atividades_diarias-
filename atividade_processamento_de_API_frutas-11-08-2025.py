import requests
from requisições.lista_requests import requisitar_get, testar_api

url = "https://securitylogs.pythonanywhere.com/frutas"

resultado = requisitar_get(url)

if resultado and "data" in resultado:
    for item in resultado["data"]:
        fruta = item.get("fruta", {})
        print(f"Nome: {fruta.get('nome')}")
        print(f"Cor: {fruta.get('cor')}")
        print(f"Origem: {fruta.get('origem')}")
        print(f"Tipo: {fruta.get('tipo')}")
        print(f"Vitamina Principal: {fruta.get('vitamina_principal')} \n")
else:
    print("Nenhum dado encontrado ou erro na requisição.")

teste = testar_api(url)
print(teste)