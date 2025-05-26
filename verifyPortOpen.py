import socket

try:
    dominio = input("Informe o domínio: ")

    while True:
        try:
            porta = int(input("\nInforme a porta: "))
        except ValueError:
            print("Porta inválida. Digite um número.")
            continue

        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.settimeout(1)
        try:
            scan = conexao.connect_ex((dominio, porta))
            if scan == 0:
                print(f"\nPort {porta} is open! return {scan}")
            else:
                print(f"\nPort {porta} is closed!")
        except socket.gaierror:
            print("\nDomínio inválido!")
        finally:
            conexao.close()

        print("\nVerificar outra porta? y/n")
        x = input("\nRetorno: ")
        if x.lower() == "y":
            continue
        else:
            break

except Exception as e:
    print(f"\nOcorreu um erro: {e}")
    input("\nPressione ENTER para sair...")
