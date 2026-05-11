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
    print("[2]: Visão geral de horarios.")
    print("[3]: Marcar Horario.")
    print("[0]: Sair.")
    print("")
    print("=============================")

def agendaH():
    while True:
        
        try:
            escolha = input("Escolha seu hórario: ")

            if horario[escolha] == "Disponivel":
                horario[escolha] = "Ocupado"
                print("horario agendado")
                break

            elif horario[escolha] == "Ocupado":
                print("Horario ocupado.")
                continue
            
            elif horario[escolha] == "Horario de Almoco":
                print("a escravidão foi abolida faz um tempo")
                continue

            elif horario[escolha] == "Fechado":
                print("a escravidão foi abolida faz um tempo")
                continue

            else:
                print("Horario invalido.")
                continue
        
        except KeyError:
            print("Erro!!")
            continue



horario = {
    "08:00": "Disponivel",
    "08:30": "Disponivel",
    "09:00": "Disponivel",
    "09:30": "Disponivel",
    "10:00": "Disponivel",
    "10:30": "Disponivel",
    "11:00": "Disponivel",
    "11:30": "Disponivel",
    "12:00": "Disponivel",
    "12:30": "Disponivel",
    "13:00": "Disponivel",
    "13:30": "Horario de Almoco",
    "14:00": "Disponivel",
    "14:30": "Disponivel",
    "15:00": "Disponivel",
    "15:30": "Disponivel",
    "16:00": "Disponivel",
    "16:30": "Disponivel",
    "17:00": "Disponivel",
    "17:30": "Disponivel",
    "18:00": "Disponivel",
    "18:30": "Disponivel",
    "19:00": "Disponivel",
    "19:30": "Disponivel",
    "20:00": "Disponivel",
    "20:30": "Disponivel",
    "21:00": "Fechado"
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
        for hora,status in horario.items():
            if status == "Disponivel":
                print(hora, "Disponivel")
        print(f"[1]  Agenda horario", end= ". " )
        print("[2] Voltar ao menu.")

        while True:   
            
            opcao1 = input("Opção: ")
            
            if opcao1 == "1":
                agendaH()
                break

            elif opcao1 == "2":
                limpar()
                break

            else:
                print("Opção invalida.")

    
    elif opcao == "2":
        limpar()
        for hora,status in horario.items():
            print(hora, status)
        
        print(f"[1]  Agenda horario", end= ". " )
        print("[2] Voltar ao menu.")

        while True:

            opcao1 = input("Opção: ")

            if opcao1 == "1":
                agendaH()
                break

            elif opcao1 == "2":
                limpar()
                break

            else:
                print("Opção invalida.")

    

    elif opcao == '3':
        limpar()
        agendaH()

    elif opcao == '0':
        limpar()
        print("Obrigado pela sua preferecia!!")
        break

    else:
        limpar()
        print("Opção invalida!!")
        continue
