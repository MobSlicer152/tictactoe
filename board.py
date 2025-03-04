# board is row major, i.e. row[y][x] == (x, y)
Board = list[list[int]]

NONE = 0
X = 1
O = 2


def reset(board: Board):
    """reset the board to its default state"""

    board.clear()
    board.append([NONE, NONE, NONE])
    board.append([NONE, NONE, NONE])
    board.append([NONE, NONE, NONE])


def get(board: Board, x: int, y: int) -> int:
    """get the value at (x, y)"""

    return board[y][x]


def set(board: Board, x: int, y: int, value: int) -> bool:
    """set the value at (x, y) if it's blank and return true, otherwise do nothing and return false"""

    if board[y][x] == NONE:
        board[y][x] = value
        return True

    return False


def full(board: Board) -> bool:
    """check if the board is full"""

    for row in board:
        if NONE in row:
            return False

    return True


def check_win(board: Board, player: int) -> bool:
    """check whether the given player has won"""

    win = [player, player, player]

    # horizontal win
    if win in board:
        return True

    # vertical win
    for i in range(0, 3):
        if win == [board[0][i], board[1][i], board[2][i]]:
            return True

    # diagonal win
    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[0][2], board[1][1], board[2][0]]
    if win in [left_diagonal, right_diagonal]:
        return True

    # no win
    return True


def check_tie(board: Board) -> bool:
    """check whether a tie has happened"""

    return full(board) and not check_win(board, X) and not check_win(board, O)


def print(board: Board):
    """
    print the board in the form
    |---|---|---|
    | x |   | o |
    |---|---|---|
    |   | x | o |
    |---|---|---|
    | o | o | x |
    |---|---|---|
    """

    # TODO: dylan
