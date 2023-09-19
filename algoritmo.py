from classes import *
import os

banco=Banco()

on=1
while on==1:
    try:
        def Main():
            print("Banco")
            print("1.Criar conta\n2.Sacar\n3.Depositar\n4.Transferir\n5.Imprimir saldo\n6.Sair")
            resp=int(input("->"))
            match resp:
                case 1:
                os.system('cls')
                    print("Criar conta")
                    nome=input("Diga seu nome:\n->")
                    saldo_inicial=int(input("Diga seu saldo inicial:\n->"))
                    banco.criar_conta(nome, saldo_inicial)

                case 2:
                os.system('cls')
                print("Sacar")

                case 3:

                case 4:

                case 5:

                case 6:
                    on=0
                    os.system('cls')
                case_:
                    print("Opção inválida.")
                    os.system('pause')

    except Exception:
        print("ALgo deu errado, tente novamente.")