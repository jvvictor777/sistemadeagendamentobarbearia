import os

opcao = 0

clientes = []
agendas = []
horarios = []

def limpar():
    os.system ("cls" if os.name == "nt" else 'clear')

def titulo():
    print("______            _                     _         _____             _         ______            _                     ")
    print("| ___ \          | |                   (_)       /  ___|           | |        | ___ \          | |                    ")
    print("| |_/ / __ _ _ __| |__   ___  __ _ _ __ _  __ _  \ `--.  __ _ _ __ | |_ __ _  | |_/ / __ _ _ __| |__   __ _ _ __ __ _ ")
    print("| ___ \/ _` | '__| '_ \ / _ \/ _` | '__| |/ _` |  `--. \/ _` | '_ \| __/ _` | | ___ \/ _` | '__| '_ \ / _` | '__/ _` |")
    print("| |_/ / (_| | |  | |_) |  __/ (_| | |  | | (_| | /\__/ / (_| | | | | || (_| | | |_/ / (_| | |  | |_) | (_| | | | (_| |")
    print("\____/ \__,_|_|  |_.__/ \___|\__,_|_|  |_|\__,_| \____/ \__,_|_| |_|\__\__,_| \____/ \__,_|_|  |_.__/ \__,_|_|  \__,_|")

def menu_principal():
    print("============ Cliente ============")
    print("")
    print("[1]: Cliente.")
    print("[2]: Horario.")
    print("[3]: Agenda.")
    print("[0]: Sair.")
    print("")
    print("================================")

def menu_cliente():
    print("============ Cliente ============")
    print("")
    print("[1]: Adicionar clinte.")
    print("[2]: Ver cliente.")
    print("[0]: Voltar.")
    print("")
    print("================================")

def menu_horario():
    print("============ Horario ============")
    print("")
    print("[1]: Ver horarios disponiveis.")
    print("[2]: Ver horarios oculpados.")
    print("[3]: Ver visão geral de horarios.")
    print("[0]: Sair.")
    print("")
    print("================================")

def agendar():
    print("Sistema para agendar horario aqui.")

limpar()
while True:
    titulo()
    menu_principal()

    opcao = input("Digite a sua opção: ")

    if opcao == "1":
        limpar()
        menu_cliente() 

        while True:
            opcao = input("Digite a sua opção: ")

            if opcao == "1":
                pass
                break

            elif opcao == "2":
                pass
                break

            else:
                print("Opção invalida!!")
                continue
                
    
    elif opcao == "2":
        limpar()
        menu_horario()

        while True: 
            opcao = input("Digite a sua opção: ")
            break
        
            if opcao == "1":
                print("Ver horarios dispoiniveis aqui.")
                break
            
            elif opcao == "2":
                print("Ver horarios oculpados aqui.")
                break

            elif opcao == "3":
                print("Ver todos os horarios .")
                break

            else: 
                print("Opção invalida!!")
                continue

            

    elif opcao == '3':
        limpar()
        agendar()

    elif opcao == '0':
        limpar()
        print("Obrigado pela sua preferecia!!")
        break

    else:
        limpar()
        print("Opção invalida!!")
        continue