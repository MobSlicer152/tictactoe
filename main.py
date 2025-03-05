import board
import save


def getnum():
    while True:
        xpos = input("Enter the x coordinate (number between 0 and 2) of where you want to go: ")
        ypos = input("Enter the y coordinate (number between 0 and 2) of where you want to go: ")

        try:
            xpos = int(xpos)
            ypos = int(ypos)

        except ValueError:
            print("Please input a valid integer")
    
        if (xpos > 2) or (xpos < 0) or (ypos < 0) or (ypos > 2):
            print("Please input a valid integer between 0 and 2")
        else:
            return(xpos, ypos)
    

    
def main():
    while True:
        print("\nWelcome to tic tac toe main menu!\nPlease select:")
        option = input("Type 1 to play the game\nType 2 to view the hall of fame\nType 3 to quit.\n")
        try:
            option = int(option)
        except ValueError:
            print("Please enter a valid integer.")
        
        if option > 3 or option < 1:
            print("Please enter a valid integer.")
        else:
            if option == 1:
                game()
            elif option == 2:
                scoreboard = save.load(save.PATH)
                print("Hall of fame:")
                save.print_all(scoreboard)
            elif option == 3:
                print("Thanks for playing!")
                break


def game():
    state = []
    board.reset(state)
    
    names = {}
    names[board.X] = input("Enter player X's name: ")
    names[board.O] = input("Enter player O's name: ")
    
    running = True
    winner = board.NONE
    loser = board.NONE
    while running:
        for (player, other) in [(board.X, board.O), (board.O, board.X)]:
            if board.get_letter(player) == "X":
                print(f"\n{names[player]}'s turn:")
            elif board.get_letter(player) == "O":
                print(f"\n{names[player]}'s turn:")

            board.print_board(state)
            (x, y) = getnum()
            while not board.set(state, x, y, player):
                (x, y) = getnum()
                pass
            if board.check_win(state, player):
                winner = player
                loser = other
                print(f"\n{names[player]} has won the game!:")
                break
            board.print_board(state)

        # keep running until a tie or someone wins
        running = not board.check_tie(state) and winner == board.NONE

    if board.check_tie(state):
        winner = board.X
        loser = board.O

    scoreboard = save.load(save.PATH)

    winner_name = names[winner]
    loser_name = names[loser]
    # TODO: update scoreboard with win/loss/tie
    save.add(scoreboard, winner_name, loser_name, board.check_tie(state))

    save.write(scoreboard, save.PATH)


if __name__ == "__main__":
    main()
