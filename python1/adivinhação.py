def jogar():

    import random

    print("@@@ JOGO DA ADIVINHAÇÃO @@@")
    print("Adivinhe o número que estou pensando, de 1 a 10")
    sorteio = random.randint(1,10)

    limite_tentativas = 3
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
            print("Chute um numero maior")
        
        
        tentativa = tentativa + 1 
if(__name__ == "__main__"):
    jogar()