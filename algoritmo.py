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
                    print("Conta criada")
                    os.system('pause')

                case 2:
                    os.system('cls')
                    print("Sacar")
                    conta=input("Digite o nome da sua conta.\n->")
                    valor=int(input("Digite o valor que queira retirar.\n->"))
                    banco.sacar(conta, valor)
                    
                case 3:
                    os.system('cls')
                    print("Depositar")
                    conta=input("")
                    valor=int(input(""))

                case 4:
                    os.system('cls')
                    print("Transferir")
                    conta=input("")
                    valor=int(input(""))
                case 5:
                    os.system('cls')

                case 6:
                    on=0
                    os.system('cls')
                case _:
                    print("Opção inválida.")
                    os.system('pause')

    except Exception:
        print("ALgo deu errado, tente novamente.")