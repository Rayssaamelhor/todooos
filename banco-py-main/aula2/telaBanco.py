# from nomeDoArquivo import nomeDaClasse
from conta  import Conta


conta1 =Conta (123, "10500-10", "Luis", 1800.0, 1239)
print(f'Saldo disponivel: {conta1.extrato()}')

conta2 = Conta(124, "10550-10", "Deivison", 1800.0, 1218)
print(f'Saldo disponivel: {conta2.extrato()}')

conta1.saque(2000.0)
print(f'Saldo disponivel: {conta1.extrato()}')

conta1.deposito(99.0)
print(f'Saldo disponivel: {conta1.extrato()}')

conta1.pix(200, conta2)
print(conta1.extrato())
print(conta2.extrato())