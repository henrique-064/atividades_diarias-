import requests

print("Bem-vindo ao programa de consulta de Pokémon!")

while True:
    nome_pokemon = input("\nQual Pokémon você quer ver? ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}" # isso permite que seja possível buscar o pokémon pelo nome
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print("Pokémon não encontrado. Tente novamente.")
        continue
    
    dados = resposta.json()
    
    nome = dados["name"].capitalize()
    id_pokemon = dados["id"]
    altura = dados["height"] / 10 
    peso = dados["weight"] / 10    
    tipos = [t["type"]["name"] for t in dados["types"]]
    imagem = dados["sprites"]["front_default"]
    
    fraquezas = set()
    for tipo in tipos:
        url_tipo = f"https://pokeapi.co/api/v2/type/{tipo}"
        resposta_tipo = requests.get(url_tipo)
        if resposta_tipo.status_code == 200:
            dados_tipo = resposta_tipo.json()
            double_damage_from = dados_tipo["damage_relations"]["double_damage_from"]
            for t in double_damage_from:
                fraquezas.add(t["name"])
    
    print(f"\nNome: {nome}")
    print(f"ID: {id_pokemon}")
    print(f"Altura: {altura} m")
    print(f"Peso: {peso} kg")
    print(f"Tipo(s): {', '.join(tipos)}")
    print(f"Fraquezas: {', '.join(fraquezas) if fraquezas else 'Nenhuma'}")
    print(f"")
    print(f"Imagem: {imagem}")

    for tipo in tipos:
        url_tipo = f"https://pokeapi.co/api/v2/type/{tipo}/" # requisitando as informações sobre os pokémons a partir do pokémon que foi selecionado
        response = requests.get(url_tipo)

        if response.status_code == 200:
            data = response.json()
            damage_relations = data["damage_relations"]

            print("Fraco contra (double_damage_from):")
            if damage_relations['double_damage_from']:
                for item in damage_relations["double_damage_from"]:
                    print(f" - {item['name']}")
            else:
                print("   nenhum")
        
            print("Resistente contra (half_damage_from):")
            if damage_relations['half_damage_from']:
                for item in damage_relations["half_damage_from"]:
                    print(f" - {item['name']}")
            else:
                print("   nenhum")

            print("Imune contra (no_damage_from):")
            if damage_relations['no_damage_from']:
                for item in damage_relations["no_damage_from"]:
                    print(f" - {item['name']}")
            else:
                print("   nenhum")

            print()

        else:
            print(f"Erro ao acessar tipo {tipo}")

    print("Lista de ataques disponíveis:")

    lista_ataques = []

    for ataque in dados["moves"]:
        nome_ataque = ataque["move"]["name"]
        detalhes_aprendizado = ataque["version_group_details"][0]  # peguei só o primeiro, para simplificar
        metodo = detalhes_aprendizado["move_learn_method"]["name"]
        nivel = detalhes_aprendizado["level_learned_at"]

        ataque_info = {
            "nome": nome_ataque,
            "metodo": metodo,
            "nivel": nivel
        }

        lista_ataques.append(ataque_info)

    for atk in lista_ataques:
        if atk["metodo"] == "level-up":
            print(f"- {atk['nome']} (nível {atk['nivel']})")
        else:
            print(f"- {atk['nome']} ({atk['metodo']})")


    
    outro = input("\nQuer ver outro Pokémon? (sim/não) ").strip().lower() # pergunta se o usuário quwer ver outro pokémon
    if outro != 'sim':
        print("Até mais!...")
        break
