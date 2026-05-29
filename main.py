import os

opcao = 0

clientes = []
agendas = []
horarios = []

def limpar():
    os.system ("cls" if os.name == "nt" else 'clear')

def titulo1():
    print("______            _                     _         _____             _         ______            _                     ")
    print("| ___ \          | |                   (_)       /  ___|           | |        | ___ \          | |                    ")
    print("| |_/ / __ _ _ __| |__   ___  __ _ _ __ _  __ _  \ `--.  __ _ _ __ | |_ __ _  | |_/ / __ _ _ __| |__   __ _ _ __ __ _ ")
    print("| ___ \/ _` | '__| '_ \ / _ \/ _` | '__| |/ _` |  `--. \/ _` | '_ \| __/ _` | | ___ \/ _` | '__| '_ \ / _` | '__/ _` |")
    print("| |_/ / (_| | |  | |_) |  __/ (_| | |  | | (_| | /\__/ / (_| | | | | || (_| | | |_/ / (_| | |  | |_) | (_| | | | (_| |")
    print("\____/ \__,_|_|  |_.__/ \___|\__,_|_|  |_|\__,_| \____/ \__,_|_| |_|\__\__,_| \____/ \__,_|_|  |_.__/ \__,_|_|  \__,_|")

def menu1():
    print("============ MENU ============")
    print("")
    print("[1]: Cliente.")
    print("[2]: Agenda.")
    print("[3]: Horario.")
    print("[0]: Sair.")
    print("")
    print("=============================")

limpar()
while True:
    titulo1()
    menu1()

    opcao = input("Digite a sua opção: ")

    if opcao == "1":
        limpar()
        pass
    
    elif opcao == "2":
        limpar()
        pass

    elif opcao == '3':
        limpar()
        pass

    elif opcao == '0':
        limpar()
        print("Obrigado pela sua preferecia!!")
        break

    else:
        limpar()
        print("Opção invalida!!")
        continue