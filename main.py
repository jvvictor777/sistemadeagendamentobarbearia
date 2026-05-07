#Gerencia uma agenda diária (lista com horários fixos). O usuário escolhe um horário e o sistema marca como "Ocupado".

import os

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
    print("[1]: Ver Horarios disponiveis.")
    print("[2]: Marcar Horario.")
    print("[0]: Sair.")
    print("")
    print("=============================")

def horarios():
    horario = {
        
    }

limpar()
while True:
    titulo1()
    menu1()
    
    try:
        opcao = input("Digite a sua opção: ")
    except:
        limpar()
        print("Erro!!")
        continue

    if opcao == "1":
        limpar()
        print("Horarios disponiveis aqui.")
    
    elif opcao == '2':
        limpar()
        print("Agenda horario aqui.")

    elif opcao == '0':
        limpar()
        print("Obrigado pela sua preferecia!!")
        break

    else:
        limpar()
        print("Opção invalida!!")
        continue
