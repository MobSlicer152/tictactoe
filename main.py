import board
import save


# suggestion: make a function that gets a number and rejects it if there's a ValueError or it's outside the allowed range
# otherwise, just use int(input())
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
    state = []
    board.reset(state)

    running = True
    winner = board.NONE
    while running:
        for player in [board.X, board.O]:
            print(f"\nPlayer {board.get_letter(player)}'s turn:")
            board.print_board(state)
            # TODO: get these
            (x, y) = getnum()
            while not board.set(state, x, y, player):
                (x, y) = getnum()
                pass
            if board.check_win(state, player):
                winner = player
                break
            board.print_board(state)

        # keep running until a tie or someone wins
        running = not board.check_tie(state) and winner == board.NONE

    # TODO: say who won, and the final state of the board

    scoreboard = save.load(save.PATH)

    # TODO: update scoreboard with win/loss/tie
    winner_name = ""  # get winner name
    loser_name = ""  # get loser name
    save.add(scoreboard, winner_name, loser_name, board.check_tie(state))
    save.print_all(scoreboard)

    save.write(scoreboard, save.PATH)


if __name__ == "__main__":
    main()
