def play_hangman():
    print("###############################")
    print("########### Forca #############")
    print("###############################")

    hidden_word = "banana"
    hung = False
    got_it_right = False
    while (not hung and not got_it_right):
        guess = input("Digite uma letra: ")

        index = 0
        for letter in hidden_word:
            if (guess == letter):
                print("Encontrei a letra {} na posição {}".format(letter, index))
            index = index + 1

    print("Fim do jogo")


if (__name__ == "__main__"):
    play_hangman()
