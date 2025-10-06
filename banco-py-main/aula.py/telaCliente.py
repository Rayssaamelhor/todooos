import getpass
import csv
from conta import Conta

# INICIALIZAÇÃO DE VARIÁVEIS
contas = []
agencia = int(input("Digite a agência: "))
numero_conta = int(input("Digite sua conta corrente: "))
senha = getpass.getpass("Digite a senha: ")
contaEncontrada = None
acesso_liberado = False

def lerArquivo():
    with open('contas.csv', newline = '', encoding = 'utf-8', errors = 'ignore') as lerContas:
        leitor = csv.reader(lerContas, delimiter = ',')
        for linha in leitor:
            conta = Conta(int(linha[0]), int(linha[1]),linha[2],float(linha[3]), linha[4])
            contas.append(conta)

def encontrarContaCorrente():
    global contaEncontrada
    global acesso_liberado
    for conta in contas:
        if numero_conta == conta.numero:
            contaEncontrada = Conta(conta.agencia, conta.numero, conta.titular, conta.saldo, conta.senha)

def verificarAcesso():
    global contaEncontrada
    if contaEncontrada == None: # verifica se a conta é Nula (inexistente)
        print("Dados incorretos")
    else:
        # Verificar se o usuário digitou a senha e agência corretamente
        if senha == contaEncontrada.senha and agencia == contaEncontrada.agencia:
         acesso_liberado = True  
           print("Acesso liberado")
        else:
            print("Dados incorretos")

lerArquivo()
encontrarContaCorrente()
verificarAcesso()

if acesso_liberado == True:
    while(True):
        print("Digite o número da opção desejada: ")
        print("1 - Extrato")
        print("2 - Saque")
        print("3 - Depósito")
        print("4 - Pix")
        transacao = int(input("Digite a opção:"))
        if transacao == 1:
            print(f"o saldo da conta é {contaEncontrada.extrato()}")
            if transacao == 2:
                valor = float(input("Digite o valor do saque:"))
                if contaEncontrada.saque(valor):
                    print("Saque efetuado com sucesso!")
                else:
                    print("Saque negado. consulte seu extrato!")
            else:
                print("opção inválida")