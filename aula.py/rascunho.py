#Criar um formulário, para o gerente preencher os

# dados da conta

# Usar prints e inputs para receber:

# Agência

# Número da conta (criar um número aleatório de 5 dígitos)

#Titular

# Saldo

# Senha

# Usar laço de repetição infinito para que o sistema permita
class Conta:
   def __init__(self, numero, agencia, titular, saldo, senha):
      self.__numero = numero
      self.__agencia = agencia
      self.__titular = titular
      self.__saldo = saldo
      self.__senha = senha   

   def extrato(self):
      return f"Conta: {self.numero} - Titular: {self.titular} - Saldo: R$ {self.saldo:.2f}"

   def saque(self, valor):
      if valor <= 0:
         print("Valor de saque deve ser positivo.")
         return False
      if valor > self.saldo:
         print("Saldo insuficiente para saque.")
         return False
      self.saldo -= valor
      print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
      return True

   def deposito(self, valor):
      if valor <= 0:
         print("Valor de depósito deve ser positivo.")
         return False
      self.saldo += valor
      print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
      return True

   def pix(self, valor, conta_destino):
      if valor <= 0:
         print("Valor de PIX deve ser positivo.")
         return False
      if valor > self.saldo:
         print("Saldo insuficiente para PIX.")
         return False
      self.saldo -= valor
      conta_destino.saldo += valor
      print(f"PIX de R$ {valor:.2f} realizado com sucesso para a conta {conta_destino.numero}.")
      return True