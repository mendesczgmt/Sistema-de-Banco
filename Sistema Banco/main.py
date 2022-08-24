from conta import Conta

resp = None
conta = Conta('123-4', 'João', 120.0, 1000.0)



while resp != 0:
    print("[1] Depositar\n[2] Sacar\n[3] Transferir\n[4] Saldo\n[0] Sair")
    resp = int(input("Qual operação deseja fazer? "))
    if resp > 4:
        print("Perdão, não conseguimos identificar a sua resposta.")
    else:
        if resp == 1:
            print("Certo.")
            qnt = float(input("Qual valor que deseja depositar? "))
            conta.deposita(qnt)
            print("Valor depositado com sucesso")
            break
        elif resp == 2:
            print("Certo")
            qnt = float(input("Qual o valor que deseja sacar? "))
            conta.saca(qnt)
            if conta.saca == True:
                print("Saque feito com sucesso!!!")
            else:
                print("Perdão, saque não pode ser feito")
                break
        elif resp == 3:
            contaD = int(input("Digite a conta de destino: "))
            valor = int(input("Digite o valor da trasnferência: "))
            conta.transfere(contaD, valor)
            break
        elif resp == 4:
            print(conta.saldo)
            break