print("###############################")
print("######## Adivinhação ##########")
print("###############################")

secretValue = 32
tryAmount = 3
game = 1

for game in range(1, tryAmount+1):
    print("Tentativa {} de {}".format(game, tryAmount))
    guessStr = input("Digite um número entre 0 e 35: ")
    guess = int(guessStr)

    print("Você digitou ", guess)

    if(guess < 1 or guess > 35):
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
