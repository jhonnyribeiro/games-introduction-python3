print("###############################")
print("######## Adivinhação ##########")
print("###############################")

secretValue = 32

guess_str = input("Digite um número: ")
guess = int(guess_str);

print("Você digitou ", guess)

if (secretValue == guess):
    print("Você acertou")
else:
    print("Você errou")

print("Fim do jogo")