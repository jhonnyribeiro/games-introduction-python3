print("###############################")
print("######## Adivinhação ##########")
print("###############################")

secretValue = 32
tryAmount = 3
game = 1;

while (game <= tryAmount):
    print("Tentativa ", game, " de ", tryAmount)
    guessStr = input("Digite um número: ")
    guess = int(guessStr)

    print("Você digitou ", guess)

    gotItRight = guess == secretValue
    bigger = guess > secretValue
    smaller = guess < secretValue

    if (gotItRight):
        print("Você acertou")
        game = tryAmount
    else:
        if (bigger):
            print("Você errou! Seu chute foi maior")
        elif (smaller):
            print("Você errou! Seu chute foi menor")
    game = game + 1
print("Fim do jogo")
