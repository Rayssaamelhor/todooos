import adivinhação

print("Escolha o jogo desejado:")
print("1 - adivinhação")
print("2 - forca")

opcao = int(input("Digite o número do jogo desejado:"))

if opcao == 1:
    print("Executando adivinhação...")
    adivinhação.jogar()
elif opcao == 2:
    print("Executando forca...")
else:
    print("Executando adivinhação")