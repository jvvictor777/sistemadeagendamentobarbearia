import os 

opcao = 0
clientes = []
horarios = []
agenda = []

def entre():
    input("Digite ENTRE para continuar...")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def titulo():
    print(""" 
    ______            _                     _         _____             _         ______            _                     
    | ___ \          | |                   (_)       /  ___|           | |        | ___ \          | |                    
    | |_/ / __ _ _ __| |__   ___  __ _ _ __ _  __ _  \ `--.  __ _ _ __ | |_ __ _  | |_/ / __ _ _ __| |__   __ _ _ __ __ _ 
    | ___ \/ _` | '__| '_ \ / _ \/ _` | '__| |/ _` |  `--. \/ _` | '_ \| __/ _` | | ___ \/ _` | '__| '_ \ / _` | '__/ _` |
    | |_/ / (_| | |  | |_) |  __/ (_| | |  | | (_| | /\__/ / (_| | | | | || (_| | | |_/ / (_| | |  | |_) | (_| | | | (_| |
    \____/ \__,_|_|  |_.__/ \___|\__,_|_|  |_|\__,_| \____/ \__,_|_| |_|\__\__,_| \____/ \__,_|_|  |_.__/ \__,_|_|  \__,_|                                                                                                                  
    """)

def menu(tipo, opcoes = True):
    global opcao

    linha = "===================\n"

    if (tipo == "principal"):
        limpar()
        titulo()
        print(linha)
        print("[1] - Clientes.")
        print("[2] - Horarios.")
        print("[3] - Agendar.")
        print("[0] - Sair.\n")
        print(linha)

    elif(tipo == "clientes"):
        limpar()
        titulo()
        print(linha)
        print("[1] - Adcionar Clinte.")
        print("[2] - Ver Clintes.")
        print("[0] - Voltar.\n")
        print(linha)

    elif(tipo == "horario"):
        limpar()
        titulo()
        print(linha)
        print("[1] - Adcionar horario.")
        print("[2] - Ver Horarios.")
        print("[0] - Voltar.\n")
        print(linha)

    elif(tipo == "agenda"):
        limpar()
        titulo()
        print(linha)
        print("[1] - Agendar horario.")
        print("[2] - Ver horarios Agendado")
        print("[0] - Voltar.\n")
        print(linha)

    if opcoes:
        opcao = input("Digite a sua opção: ")

def add(tipo):

    if tipo == "clientes":
        codigo = len(clientes) +1
        nome = input("Digite o nome do Clinte: ")
        email = input("Digite o email do Clinte: ")
        clientes.append([codigo, nome, email])

    elif tipo == "horarios":
        codigo = len(horarios) +1
        horario = input("Digite o horario: ")
        horarios.append([codigo, horario])

    elif tipo == "agendar":
        ocupado = False
        codigo = len(agenda) +1
        lista("clientes")
        idcliente = int(input("\nDigite o Codigo do cliente: "))
        print("")
        lista("horarios")
        idhorario = int(input("\nDigite o Codigo do horario: "))
        
        for agendamento in agenda:
            if agendamento[2] == idhorario:
                ocupado = True

        if ocupado: 
            print("Horario já ocupado.")
            entre()
    
        else:
            agenda.append([codigo, idcliente, idhorario])
            print("\nhorario agendado.\n")
            entre()

def lista(tipo):
    
    if tipo == "clientes":
        for cliente in clientes:
            print(f"Codigo: {cliente[0]} - Nome: {cliente[1]} - Email: {cliente[2]}")
    elif tipo == "horarios":
        for horario in horarios:
            print(f"Codigo: {horario[0]} - Horario: {horario[1]}")
    elif tipo == "agendar":
        for agendar in agenda:
            print(f"Codifo: {agendar[0]} - clinte: {clientes[agendar[1]-1][1]} - Horario: {horarios[agendar[2]-1][1]}")


while True:
    menu("principal")

    if opcao == "1":
        while True:
            menu("clientes")
            
            if opcao == "1":
                limpar()
                titulo()
                add("clientes")
                print("\nClinte adcionado.\n")
                entre()

            elif opcao == "2":
                limpar()
                lista("clientes")
                entre()

            elif opcao == "0":
                break

            else:
                print("Erro...")
                entre()
                limpar()
                continue

    elif opcao == '2':
        while True:
            menu("horario")

            if opcao == "1":
                limpar()
                titulo()
                add("horarios")
                print("\nhorario adcionado.\n")
                entre()

            elif opcao == "2":
                limpar()
                lista("horarios")
                entre()


            elif opcao == "0":
                break

            else:
                print("Erro...")
                entre()
                limpar()
                continue



    elif opcao == '3':
        while True:
            menu("agenda")

            if opcao == "1":
                limpar()
                titulo()
                add("agendar")


            elif opcao == "2":
                limpar()
                lista("agendar")
                entre()

            elif opcao == "0":
                break

            else:
                print("Erro...")
                entre()
                limpar()
                continue


    elif opcao == "0":
        limpar()
        print("Programa sendo finalizando...")
        break