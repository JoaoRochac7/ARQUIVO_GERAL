import csv

try:
    with open("sensores.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for item in leitor:
            print(f"Máquina: {item['maquina']}")
            print(f"Temperatura: {item['temperatura']}")
            print(f"Status: {item['status']}")
            print("-" * 20)
    print('>' * 30)

    with open("producao.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for item in leitor:
            print(f"Máquina: {item['maquina']}")
            print(f"Pecas Produzidas: {item['pecas_produzidas']}")
            print("-" * 20)

    print('>' * 30)
    with open("sensores_com_erro.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for item in leitor:
            print(f"Máquina: {item['maquina']}")
            print(f"Temperatura: {item['temperatura']}")
            print(f"Status: {item['status']}")
            print("-" * 20)

except FileNotFoundError:
    print("Arquivo não encontrado!")
except Exception as e:
    print(f"Erro: {e}")