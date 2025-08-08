import time

def slow_print(text, delay=0.045):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

slow_print("Olá, como posso te chamar? : ")
nome_u = input().strip()

slow_print(f"Ok, seja bem-vindo {nome_u}!")
slow_print(f"O código é simples, {nome_u}, aqui darei espaço para você fazer uma lista de pessoas, com seus nomes e idade.")

iniciar = input(f"Deseja iniciar o programa {nome_u}? (sim/não): ").strip().lower()

if iniciar != "sim":
    slow_print("Ok, encerrando programa...")
    exit()

pessoas = []

while True:
    slow_print("Coloque o nome: ")
    nome = input().strip()

    slow_print("Coloque a idade: ")
    idade = input().strip()

    slow_print(f"Deseja colocar alguma descrição sobre essa pessoa {nome_u}? (sim/não): ")
    descri_ = input().strip().lower()
    des = ""

    if descri_ == "sim":
        slow_print(f"Coloque a descrição sobre {nome}: ")
        des = input().strip()

    pessoa = {"nome": nome, "idade": idade, "descrição": des}
    pessoas.append(pessoa)
    slow_print(f"{nome} foi adicionado(a) com sucesso à lista!")

    while True:
        slow_print(f"{nome_u}, deseja fazer mais alguma coisa? (adicionar/lista/editar/remover/encerrar): ")
        acao = input().strip().lower()

        if acao == "adicionar":
            break

        elif acao == "lista":
            slow_print("\nLista de pessoas cadastradas:")
            for p in pessoas:
                slow_print(f"Nome: {p['nome']}, Idade: {p['idade']}, Descrição: {p.get('descrição', 'sem descrição')}")
            slow_print("")

        elif acao == "editar":
            while True:
                slow_print("\nLista de pessoas cadastradas:")
                for p in pessoas:
                    slow_print(f"Nome: {p['nome']}, Idade: {p['idade']}, Descrição: {p.get('descrição', 'sem descrição')}")

                slow_print("Digite o nome de quem deseja alterar a informação: ")
                nome_editar = input().strip()

                encontrado_1 = None
                for p in pessoas:
                    if p['nome'].lower() == nome_editar.lower():
                        encontrado_1 = p
                        break

                if not encontrado_1:
                    slow_print(f"O nome '{nome_editar}' não foi encontrado na lista, tente novamente.")
                    continue

                slow_print("O que deseja mudar? (nome/idade/descrição/mudar tudo): ")
                campo = input().strip().lower()

                if campo == "nome":
                    slow_print("Digite o novo nome: ")
                    novo_nome = input().strip()
                    encontrado_1['nome'] = novo_nome
                    slow_print("Nome alterado com sucesso.")

                elif campo == "idade":
                    slow_print("Digite a nova idade: ")
                    nova_idade = input().strip()
                    encontrado_1['idade'] = nova_idade
                    slow_print("Idade alterada com sucesso.")

                elif campo == "descrição":
                    slow_print("Digite a nova descrição (ou deixe em branco para remover): ")
                    nova_desc = input().strip()
                    encontrado_1['descrição'] = nova_desc
                    slow_print("Descrição alterada com sucesso.")

                elif campo == "mudar tudo":
                    slow_print("Digite o novo nome: ")
                    novo_nome_1 = input().strip()
                    slow_print("Digite a nova idade: ")
                    nova_idade = input().strip()
                    slow_print("Digite a nova descrição (ou deixe em branco): ")
                    nova_desc = input().strip()

                    if novo_nome_1:
                        encontrado_1['nome'] = novo_nome_1
                    if nova_idade:
                        encontrado_1['idade'] = nova_idade
                    encontrado_1['descrição'] = nova_desc
                    slow_print("Todas as informações foram atualizadas.")

                slow_print("Deseja alterar mais alguma coisa? (sim/não): ")
                rep = input().strip().lower()
                if rep != "sim":
                    break

        elif acao == "remover":
            slow_print("\nLista de pessoas cadastradas:")
            for p in pessoas:
                slow_print(f"Nome: {p['nome']}, Idade: {p['idade']}, Descrição: {p.get('descrição', 'sem descrição')}")

            slow_print("Digite o nome da pessoa que deseja remover: ")
            nome_remover = input().strip()

            encontrado = False
            for p in pessoas:
                if p['nome'].lower() == nome_remover.lower():
                    pessoas.remove(p)
                    slow_print(f"{p['nome']} foi removido(a) da lista.")
                    encontrado = True
                    break

            if not encontrado:
                slow_print(f"O nome '{nome_remover}' não foi encontrado na lista.")

        elif acao == "encerrar":
            slow_print(f"Ok {nome_u}, encerrando programa...")
            exit()

        while True:
            slow_print("Deseja continuar ou encerrar o programa? (cont/encerrar): ")
            continuar = input().strip().lower()
            if continuar == "cont":
                break
            elif continuar == "encerrar":
                slow_print("Encerrando programa...")
                exit()
            else:
                slow_print("Opção inválida. Encerrando por segurança...")
                exit()