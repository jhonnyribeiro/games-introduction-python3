def play_hangman():
    print("###############################")
    print("########### Forca #############")
    print("###############################")

    hidden_word = "banana"
    right_letters = ['_', '_', '_', '_', '_', '_']

    hung = False
    got_it_right = False

    print(right_letters)

    while (not hung and not got_it_right):
        guess = input("Digite uma letra: ")
        guess = guess.strip()

        index = 0
        for letter in hidden_word:
            if (guess.upper() == letter.upper()):
                right_letters[index] = letter
            index = index + 1
        print(right_letters)

    print("Fim do jogo")


if (__name__ == "__main__"):
    play_hangman()
