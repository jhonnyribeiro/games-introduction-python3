import random

print("###############################")
print("######## Adivinhação ##########")
print("###############################")

secretValue = round(random.randrange(1, 36))
tryAmount = 3
game = 1
score = 1000

print("Níveis de dificuldade")
print("(1) Fácil, (2) Médio, (3), Difícil")

level = int(input("Digite seu nível: "))

if (level == 1):
    tryAmount = 20
elif (level == 2):
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
        print("Você acertou e fez {} pontos".format(score))
        break
    else:
        if (bigger):
            print("Você errou! Seu chute foi maior")
        elif (smaller):
            print("Você errou! Seu chute foi menor")
        score_lost = abs(secretValue - guess)
        score = score - score_lost

print("Fim do jogo")
