import board
import save

def main():
    state = []
    board.reset(state)

    # TODO: add input
    running = True
    winner = board.NONE
    while running:
        for player in [board.X, board.O]:
            x = 0 # get the x and y on the board
            y = 0
            while not board.set(state, x, y, player):
                # get position until it's an allowed one
                pass
            if board.check_win(state, player):
                winner = player
                break

        # keep running until a tie or someone wins
        running = not board.check_tie(state) and winner == board.NONE

    scoreboard = save.load(save.PATH)

    # TODO: update scoreboard with win/loss/tie
    winner_name = "" # get winner name
    loser_name = "" # get loser name
    save.add(scoreboard, winner_name, loser_name, board.check_tie(state))
    save.print_all(scoreboard)

    save.write(scoreboard, save.PATH)

if __name__ == "__main__":
    main()
