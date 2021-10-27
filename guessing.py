print("###############################")
print("######## Adivinhação ##########")
print("###############################")

secretValue = 32

guess_str = input("Digite um número: ")
guess = int(guess_str);

print("Você digitou ", guess)

gotItRight = guess == secretValue
bigger = guess > secretValue
smaller = guess < secretValue

if (gotItRight):
    print("Você acertou")
else:
    if (bigger):
        print("Você errou! Seu chute foi maior")
    elif (smaller):
        print("Você errou! Seu chute foi menor")
print("Fim do jogo")
