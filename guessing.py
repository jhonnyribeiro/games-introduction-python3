import random

print("###############################")
print("######## Adivinhação ##########")
print("###############################")

secretValue = round(random.randrange(1, 101))
tryAmount = 3
game = 1

print("Níveis de dificuldade")
print("(1) Fácil, (2) Médio, (3), Difícil")

nivel = int(input("Digite seu nível: "))

if (nivel == 1):
    tryAmount = 20
elif (nivel == 2):
    tryAmount = 10
else:
    tryAmount = 5

for game in range(1, tryAmount + 1):
    print("Tentativa {} de {}".format(game, tryAmount))
    guessStr = input("Digite um número entre 0 e 35: ")
    guess = int(guessStr)

    print("Você digitou ", guess)

    if (guess < 1 or guess > 35):
        print("O valor deve estar entre 0 e 35")
        continue

    gotItRight = guess == secretValue
    bigger = guess > secretValue
    smaller = guess < secretValue

    if (gotItRight):
        print("Você acertou")
        break
    else:
        if (bigger):
            print("Você errou! Seu chute foi maior")
        elif (smaller):
            print("Você errou! Seu chute foi menor")

print("Fim do jogo")
