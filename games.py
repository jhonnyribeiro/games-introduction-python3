import guessing
import hangman

print("###############################")
print("########### JOGOS #############")
print("###############################")

print("(1) Advinhação, (2) Forca")

game = int(input("Escolha o jogo: "))

if(game == 1):
    print("JOGANDO ADVINHAÇÃO")
    guessing.play_guessing()
elif(game == 2):
    print("JOGANDO FORCA")
    hangman.play_hangman()
