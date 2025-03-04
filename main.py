import board
import save

def main():
    state = []
    board.reset(state)

    # TODO: main loop where you take input and print the board

    scoreboard = save.load(save.PATH)

    # TODO: update scoreboard with win/loss/tie
    # save.add(scoreboard, winner, loser, board.check_tie(state))
    save.print_all(scoreboard)

    save.write(scoreboard, save.PATH)

if __name__ == "__main__":
    main()
