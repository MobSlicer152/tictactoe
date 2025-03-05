PATH = "save.txt"
ENCODING = "utf-8"
SEPARATOR = ";"

# list[(winner, loser, was_tie)]
Save = list[tuple[str, str, bool]]


def load(path: str) -> Save:
    """read and parse the save file at the given path"""
    text = []
    try:
        with open(path, "rb") as f:
            text = [line.decode(encoding=ENCODING) for line in f.readlines()]
    except:
        return []

    try:
        # get non-empty lines
        entries = list(filter(None, text))

        # parse entries
        return [
            # make tuple of (winner, loser, is_tie)
            (e[0].strip(), e[1].strip(), e[2].strip().title() == "True")
            # split by semicolons
            for e in [list(e.split(SEPARATOR)) for e in entries]
        ]
    except:
        raise "Failed to parse save!"


def add(save: Save, winner: str, loser: str, was_tie: bool):
    save.append((winner, loser, was_tie))


def write(save: Save, path: str):
    try:
        serialized = [
            bytes(f"{e[0]}{SEPARATOR}{e[1]}{SEPARATOR}{e[2]}\n", encoding=ENCODING)
            for e in save
        ]
        with open(path, "wb") as f:
            f.writelines(serialized)
    except:
        raise "Failed to write save!"


def print_entry(save: Save, i: int):
    """
    prints an entry of the scoreboard:
    ("Elliot", "Dylan", true) gives "Elliot tied Dylan"
    ("Elliot", "Dylan", false) gives "Elliot beat Dylan" or "Dylan lost to Elliot"
    """

    # TODO: dylan write this
    (winner, loser, was_tie) = save[i]
    print("")


def print_all(save: Save):
    for i in range(0, len(save)):
        print_entry(save, i)
