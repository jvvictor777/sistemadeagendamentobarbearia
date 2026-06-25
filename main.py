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
        print("[1]: Adicionar horario.")
        print("[2]: Ver horarios.")
        print("[0]: Sair.\n")
        print("================================")

    elif (menu == "agenda"):
        titulo()
        print("\n============ Agenda ============\n")
        print("[1]: Agendar horario.")
        print("[2]: Ver horarios agendados.")
        print("[0]: Sair.\n")
        print("================================")


    else:
        pass

    if opcoes:
        opcao = input("Digite a sua opção: ")

def cadastra(tipo):
    global qhorario
    if (tipo == "cliente"):
        codigo = len(clientes) +1
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        clientes.append([codigo, nome, email])

    elif (tipo == "horario"):
        codigo = len(horarios) +1
        horario = input("Digite o novo horario: ")
        horarios.append([codigo, horario])

    elif (tipo == "agenda"):

        ocupado = False

        codigo = len(agenda) +1
        cliente = int(input("Digite o Codigo do cliente: "))
        horario = int(input("Digite o codigo do horario: "))

        for agendamento in agenda:
            if agendamento[2] == horario:
                ocupado = True
                break
        
        if ocupado:
            print("Horario já oculpado...")
            entre()

        else:
            agenda.append([codigo, cliente, horario])


    else: 
        pass

def listas(tipo):
    if (tipo == "cliente"):
        for cliente in clientes:
            print(f"user{cliente[0]} -  {cliente[1]} - {cliente[2]}")

    elif (tipo == "horario"):
        for horario in horarios:
            print(f"Codigo {horario[0]} - {horario[1]}")
    
    elif (tipo == "agenda"):
        for agendar in agenda:
            print(f"Vaga {agendar[0]} - Cliente {clientes[agendar[1]-1][1]} - Horario {horarios[agendar[2]-1][1]}")

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
                cadastra("horario")
                limpar()
                break
            
            elif opcao == "2":
                limpar()
                listas("horario")
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
        limpar()
        menu("agenda")

        while True:
            if opcao == "1":
                limpar()
                cadastra("agenda")
                limpar()
                break

            elif opcao == "2":
                limpar()
                listas("agenda")
                entre()
                limpar()
                break
        
        limpar()

    elif opcao == '0':
        limpar()
        print("Programa sendo finalizando...")
        break

    else:
        limpar()
        print("Opção invalida!!")
        continue