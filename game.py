game_field = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]

victorie_case = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_game_field():
    print(game_field[0], end=" ")
    print(game_field[1], end=" ")
    print(game_field[2])

    print(game_field[3], end=" ")
    print(game_field[4], end=" ")
    print(game_field[5])

    print(game_field[6], end=" ")
    print(game_field[7], end=" ")
    print(game_field[8])

def step_game_field(step, symbol):
    ind = game_field.index(step)
    game_field[ind] = symbol

def get_result():
    win = ""

    for i in victorie_case:
        if game_field[i[0]] == "X" and game_field[i[1]] == "X" and game_field[i[2]] == "X":
            win = "X"
        if game_field[i[0]] == "O" and game_field[i[1]] == "O" and game_field[i[2]] == "O":
            win = "O"
    return win

def check_line(sum_O, sum_X):
    step = ""
    for line in victorie_case:
        o = 0
        x = 0

        for j in range(0, 3):
            if game_field[line[j]] == "O":
                o = o + 1
            if game_field[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if game_field[line[j]] != "O" and game_field[line[j]] != "X":
                    step = game_field[line[j]]

    return step

def opponent():
    step = ""

    step = check_line(2, 0)

    if step == "":
        step = check_line(0, 2)

    if step == "":
        step = check_line(1, 0)

    if step == "":
        if game_field[4] != "X" and game_field[4] != "O":
            step = 5

    if step == "":
        if game_field[0] != "X" and game_field[0] != "O":
            step = 1

    return step

game_over = False
my_move = True

while game_over == False:

    print_game_field()

    if my_move == True:
        symbol = "X"
        step = int(input("Пожалуйста, ходите: "))
    else:
        print("Мой ход: ")
        symbol = "O"
        step = opponent()

    if step != "":
        step_game_field(step, symbol)
        win = get_result()
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "-"

    my_move = not (my_move)

print_game_field()
print("Победитель", win)