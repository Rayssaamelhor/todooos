import random
import getpass 
from conta import conta 
#FORMULARIO PARA CRIAÇÃO DE CONTA
while(True):
    print("### CADASTRO DE CONTA BANCÁRIAs - BANCO VAI LÉO ###")
    print("Preencha os seguintes dados:")
    agencia - int(input("Número da agência: "))
    numero = random.randint(10000, 99999)
    titular = input("Nome do cliente: ")
    saldo = float(input("Saldo inicial: "))
    senha = getpass.getpass ("Digite uma nova senha: ")
    novaConta = Conta(agencia, numero, títular, saldo, senha)
    print(f'Conta {novaConta.numero}criada com sucesso!\n')
