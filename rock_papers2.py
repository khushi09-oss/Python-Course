print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
choice_player1 = int(input('Enter your choice: '))
if choice_player1== 1:
        choice_name = 'Rock'
elif choice_player1 == 2:
        choice_name = 'Paper'
else:
        choice_name = 'Scissors'

print("Ur choice is :", choice_name)
print("Now player 2 will choose!")
choice_player2 = int(input('Enter your choice: '))
if choice_player2 == 1:
    choice_name = 'Rock'
elif choice_player2 == 2:
    choice_name = 'Paper'
else:
     choice_name = 'Scissors'

print("player 2 chose :", choice_name)

print("both players have chosen, lets start the game!")
if choice_player1 == choice_player2:
    print("Draw")
elif (choice_player1 == 1 and choice_player2 == 2) or (choice_player1 == 2 and choice_player2 == 1):
    print("paper wins")
elif (choice_player1 == 2 and choice_player2 == 3) or (choice_player1 == 3 and choice_player2 == 2):
    print("scissors wins")
elif (choice_player1 == 3 and choice_player2 == 1) or (choice_player1 == 1 and choice_player2 == 3):
    print("rock wins")

