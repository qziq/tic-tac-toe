# tic-tac-toe4_5.py
def playfield(cells):
    """Prints the status of the field."""
    print("---------")
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print("---------")

cells = "         "
game_state = []

playfield(cells)


def game_status():
    """Determines the game status of the match and checks whether a move is possible or not."""
    global game_state

    # horizontal
    if cells[0] == "X" and cells[1] == "X" and cells[2] == "X":
        game_state.append("X wins")
    elif cells[3] == "X" and cells[4] == "X" and cells[5] == "X":
        game_state.append("X wins")
    elif cells[6] == "X" and cells[7] == "X" and cells[8] == "X":
        game_state.append("X wins")
    # vertical
    elif cells[0] == "X" and cells[3] == "X" and cells[6] == "X":
        game_state.append("X wins")
    elif cells[1] == "X" and cells[4] == "X" and cells[7] == "X":
        game_state.append("X wins")
    elif cells[2] == "X" and cells[5] == "X" and cells[8] == "X":
        game_state.append("X wins")
    # diagonal
    elif cells[0] == "X" and cells[4] == "X" and cells[8] == "X":
        game_state.append("X wins")
    elif cells[2] == "X" and cells[4] == "X" and cells[6] == "X":
        game_state.append("X wins")

    # horizontal
    if cells[0] == "O" and cells[1] == "O" and cells[2] == "O":
        game_state.append("O wins")
    elif cells[3] == "O" and cells[4] == "O" and cells[5] == "O":
        game_state.append("O wins")
    elif cells[6] == "O" and cells[7] == "O" and cells[8] == "O":
        game_state.append("O wins")
    # vertical
    elif cells[0] == "O" and cells[3] == "O" and cells[6] == "O":
        game_state.append("O wins")
    elif cells[1] == "O" and cells[4] == "O" and cells[7] == "O":
        game_state.append("O wins")
    elif cells[2] == "O" and cells[5] == "O" and cells[8] == "O":
        game_state.append("O wins")
    # diagonal
    elif cells[0] == "O" and cells[4] == "O" and cells[8] == "O":
        game_state.append("O wins")
    elif cells[2] == "O" and cells[4] == "O" and cells[6] == "O":
        game_state.append("O wins")


    if abs(cells.count("X") - cells.count("O")) > 1:
        print("Impossible")

    elif len(game_state) == 2:  # both X and O won
        print("Impossible")

    elif len(game_state) == 0:  # neither side has three in a row
        if "_" in cells:
            pass
        elif " " in cells:
            pass
        else:
            print("Draw")
            game_state.append("Draw")

    elif len(game_state) == 1:  # either X or O won
        if "X wins" in game_state:
            print("X wins")
        elif "O wins" in game_state:
            print("O wins")


def player_x():
    """Player X chooces the coordinates he wants to put a mark on. Afterwards the field gets updated."""
    global cells

    while True:
        coordinates = input("Enter the coordinates: ")

        # check input
        stripped_coordinates = "".join(coordinates.split())
        if not stripped_coordinates.isdigit():  # check if string contains only digits
            print("You should enter numbers!")
            continue

        if len(coordinates) != 3:
            continue

        for character in "0456789":
            if character in coordinates:
                print("Coordinates should be from 1 to 3!")
                break
            continue

        # update the players move
        if coordinates == "1 1":
            if cells[0] == "_" or cells[0] == " ":
                cells = "X" + cells[1:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "1 2":
            if cells[1] == "_" or cells[1] == " ":
                cells = cells[0] + "X" + cells[2:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "1 3":
            if cells[2] == "_" or cells[2] == " ":
                cells = cells[:2] + "X" + cells[3:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "2 1":
            if cells[3] == "_" or cells[3] == " ":
                cells = cells[:3] + "X" + cells[4:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "2 2":
            if cells[4] == "_" or cells[4] == " ":
                cells = cells[:4] + "X" + cells[5:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "2 3":
            if cells[5] == "_" or cells[5] == " ":
                cells = cells[:5] + "X" + cells[6:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "3 1":
            if cells[6] == "_" or cells[6] == " ":
                cells = cells[:6] + "X" + cells[7:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "3 2":
            if cells[7] == "_" or cells[7] == " ":
                cells = cells[:7] + "X" + cells[8]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "3 3":
            if cells[8] == "_" or cells[8] == " ":
                cells = cells[:8] + "X"
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue
    playfield(cells) 
    game_status()
              

def player_o():
    """Player O chooces the coordinates he wants to put a mark on. Afterwards the field gets updated."""
    global cells


    while True:
        coordinates = input("Enter the coordinates: ")

        # check input
        stripped_coordinates = "".join(coordinates.split())
        if not stripped_coordinates.isdigit():  # check if string contains only digits
            print("You should enter numbers!")
            continue

        if len(coordinates) != 3:
            continue

        for character in "0456789":
            if character in coordinates:
                print("Coordinates should be from 1 to 3!")
                break
            continue


        # update the players move
        if coordinates == "1 1":
            if cells[0] == "_" or cells[0] == " ":
                cells = "O" + cells[1:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "1 2":
            if cells[1] == "_" or cells[1] == " ":
                cells = cells[0] + "O" + cells[2:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "1 3":
            if cells[2] == "_" or cells[2] == " ":
                cells = cells[:2] + "O" + cells[3:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "2 1":
            if cells[3] == "_" or cells[3] == " ":
                cells = cells[:3] + "O" + cells[4:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "2 2":
            if cells[4] == "_" or cells[4] == " ":
                cells = cells[:4] + "O" + cells[5:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "2 3":
            if cells[5] == "_" or cells[5] == " ":
                cells = cells[:5] + "O" + cells[6:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "3 1":
            if cells[6] == "_" or cells[6] == " ":
                cells = cells[:6] + "O" + cells[7:]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "3 2":
            if cells[7] == "_" or cells[7] == " ":
                cells = cells[:7] + "O" + cells[8]
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

        elif coordinates == "3 3":
            if cells[8] == "_" or cells[8] == " ":
                cells = cells[:8] + "O"
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue
    playfield(cells)
    game_status()
          

turn = 1
while len(game_state) == 0:
    if turn % 2 != 0:  # odd turns
        turn += 1
        player_x()
    else:  # even turns
        turn += 1
        player_o()