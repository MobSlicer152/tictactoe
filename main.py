import board
import save


# suggestion: make a function that gets a number and rejects it if there's a ValueError or it's outside the allowed range
# otherwise, just use int(input())


def main():
    state = []
    board.reset(state)

    # TODO: add in
    running = True
    winner = board.NONE
    while running:
        for player in [board.X, board.O]:
            # TODO: get these
            x = 0  # get_number(0, 2)
            y = 0  # get_number(0, 2)
            while not board.set(state, x, y, player):
                # TODO: get position until it's an allowed one
                pass
            if board.check_win(state, player):
                winner = player
                break

        # keep running until a tie or someone wins
        running = not board.check_tie(state) and winner == board.NONE

    # TODO: say who won
    print()

    scoreboard = save.load(save.PATH)

    # TODO: update scoreboard with win/loss/tie
    winner_name = ""  # get winner name
    loser_name = ""  # get loser name
    save.add(scoreboard, winner_name, loser_name, board.check_tie(state))
    save.print_all(scoreboard)

    save.write(scoreboard, save.PATH)


if __name__ == "__main__":
    main()
