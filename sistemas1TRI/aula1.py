import random
numero_max = 10
sorteio = random.randint(1, numero_max)
#print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a 10")0000000000
limite_tentativas = 5
tentativa = 1
while (limite_tentativas >= tentativa):
    print("tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou o número era", sorteio)
        break
    elif (chute > sorteio):
        print("Chute um numero menor!")
    elif (chute < sorteio):
        print("Chute um numero maior!")
        tentativa = tentativa + 1
        # FINAL DO LAÇO WHILE
        print("o número sorteados era: ##", sorteio, "##")
        print("### FIM DO JOGO ###")


        