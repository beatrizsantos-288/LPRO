""" aqui estamos a utilizar o ciclo while para uma simulação de um banco, 
nesse caso utilizamos o while True O para apresentar o menu
continuamente até o utilizador escolher a opção desejada, e o break para
sair do ciclo quando o utilizador escolher a opção 0 """
saldo = 0
while True:
    print("\n1. Depositar  2. Levantar  0. Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        saldo += float(input("Valor: "))
    elif opcao == "2":
        valor = float(input("Valor: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
    print(f"Saldo: {saldo:.2f} €")
print("Até breve!")
