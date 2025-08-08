import requests

url = "https://jsonplaceholder.typicode.com/comments"
resposta = requests.get(url)

dados = resposta.json()

for usuario in dados:
    print(usuario["email"])
