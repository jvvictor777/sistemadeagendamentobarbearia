import os

opcao = 0

clientes = []
horarios = []
agenda = []

def entre():
    input("Pressione ENTRE para continuar...")

def limpar():
    os.system ("cls" if os.name == "nt" else 'clear')

def titulo():
    print("______            _                     _         _____             _         ______            _                     ")
    print("| ___ \          | |                   (_)       /  ___|           | |        | ___ \          | |                    ")
    print("| |_/ / __ _ _ __| |__   ___  __ _ _ __ _  __ _  \ `--.  __ _ _ __ | |_ __ _  | |_/ / __ _ _ __| |__   __ _ _ __ __ _ ")
    print("| ___ \/ _` | '__| '_ \ / _ \/ _` | '__| |/ _` |  `--. \/ _` | '_ \| __/ _` | | ___ \/ _` | '__| '_ \ / _` | '__/ _` |")
    print("| |_/ / (_| | |  | |_) |  __/ (_| | |  | | (_| | /\__/ / (_| | | | | || (_| | | |_/ / (_| | |  | |_) | (_| | | | (_| |")
    print("\____/ \__,_|_|  |_.__/ \___|\__,_|_|  |_|\__,_| \____/ \__,_|_| |_|\__\__,_| \____/ \__,_|_|  |_.__/ \__,_|_|  \__,_|")

def menu(menu, opcoes = True):
    global opcao

    if (menu == "principal"):
        titulo()
        print("\n============ Menu ============\n")
        print("[1]: Cliente.")
        print("[2]: Horario.")
        print("[3]: Agenda.")
        print("[0]: Sair.\n")
        print("==============================")

    elif (menu == "cliente"):
        titulo()
        print("\n============ Cliente ============\n")
        print("[1]: Adicionar clinte.")
        print("[2]: Ver cliente.")
        print("[0]: Voltar.\n")
        print("================================")

    elif (menu == "horario"):
        titulo()
        print("\n============ Horario ============\n")
        print("[1]: Ver horarios disponiveis.")
        print("[2]: Ver horarios oculpados.")
        print("[3]: Ver visão geral de horarios.")
        print("[0]: Sair.\n")
        print("================================")

    else:
        pass

    if opcoes:
        opcao = input("Digite a sua opção: ")

def cadastra(tipo):
    if (tipo == "cliente"):
        codigo = len(clientes) +1
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        clientes.append([codigo, nome, email])

    else: 
        pass

def listas(tipo):
    if (tipo == "cliente"):
        for cliente in clientes:
            print(f"user{cliente[0]} -  {cliente[1]} - {cliente[2]}")

    else:
        pass

limpar()
while True:
    menu("principal")

    if opcao == "1":
        limpar()
        menu("cliente") 

        while True:
            if opcao == "1":
                limpar()
                cadastra('cliente')
                limpar()
                break

            elif opcao == "2":
                limpar()
                listas('cliente')
                entre()
                limpar()
                break

            elif opcao == "0":
                limpar()
                break

            else:
                print("Opção invalida!!")
                continue
                
    
    elif opcao == "2":
        limpar()
        menu("horario")

        while True: 
        
            if opcao == "1":
                limpar()
                print("Ver horarios dispoiniveis aqui.")
                entre()
                limpar()
                break
            
            elif opcao == "2":
                limpar()
                print("Ver horarios oculpados aqui.")
                entre()
                limpar()
                break

            elif opcao == "3":
                limpar()
                print("Ver todos os horarios .")
                entre()
                limpar()
                break

            elif opcao == "0":
                limpar()
                break
                
            else: 
                print("Opção invalida!!")
                continue

            

    elif opcao == '3':
        pass
        limpar()

    elif opcao == '0':
        limpar()
        print("Obrigado pela sua preferecia!!")
        break

    else:
        limpar()
        print("Opção invalida!!")
        continue