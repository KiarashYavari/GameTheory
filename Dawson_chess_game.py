possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]  # each number defines a cell
player_one_wining_flag = 0


def remove_chosen_cells(player_input):  # the function Check all scenarios in two main part
    # condition one # player do not choose the first available cell
    if player_input > possible_moves[0]:
        if player_input == possible_moves[len(possible_moves) - 1]:  # last cell of row chosen
            if player_input - 1 in possible_moves:  # is that a single cell?
                possible_moves.remove(player_input - 1)
            possible_moves.remove(player_input)  # not a single cell so delete two cells
            return possible_moves
        # sub-condition 1-1 # player choose a cell in the middle
        if player_input + 1 in possible_moves:
            possible_moves.remove(player_input + 1)  # chosen cell's next cell is available
        if player_input - 1 in possible_moves:
            possible_moves.remove(player_input - 1)  # chosen cell's previous cell is available
        possible_moves.remove(player_input)  # must delete the chosen cell on any condition
        return possible_moves
    #  condition two  #player choose the first available cell in the row--this cell has no previous
    if player_input == possible_moves[0]:
        if player_input == possible_moves[len(possible_moves) - 1]:
            possible_moves.remove(player_input)
            return possible_moves
        if player_input < possible_moves[len(possible_moves) - 1]:
            if player_input + 1 in possible_moves:
                possible_moves.remove(player_input + 1)
            if player_input - 1 in possible_moves:
                possible_moves.remove(player_input - 1)
            possible_moves.remove(player_input)
            return possible_moves


# solve the the game and optimal play solution fo player two
def nim_pick_and_divide():
    remain_cells = len(possible_moves)
    if remain_cells % 4 == 0:
        # we are in p step and doomed
        return possible_moves[len(possible_moves) - 1]
    else:
        if remain_cells % 4 == 1:
            for i in range(1, len(possible_moves) - 1):  # if there is a single spot delete that
                if possible_moves[i] + 1 != possible_moves[i + 1]:
                    if possible_moves[i] - 1 != possible_moves[i - 1]:
                        return possible_moves[i]
            # there is no single cell so we could not make it
            return possible_moves[0]
        elif remain_cells % 4 == 2:  # two differences from p situation?
            for i in range(1, len(possible_moves) - 1):
                if possible_moves[i] + 1 == possible_moves[i + 1]:
                    if possible_moves[i] - 1 != possible_moves[i - 1]:
                        return possible_moves[i]
            return possible_moves[0]  # delete two cells and go for a win
        elif remain_cells % 4 == 3:
            # delete three cells and divide the remaining cells
            for i in range(1, len(possible_moves) - 1):
                if possible_moves[i] + 1 == possible_moves[i + 1]:
                    if possible_moves[i] - 1 == possible_moves[i - 1]:
                        return possible_moves[i]
            return possible_moves[1]


def starting_position(deleted_cells, number_of_cells):
    starting_point = list(range(1, number_of_cells + 1))
    for index in range(0, len(deleted_cells)):
        if deleted_cells[index] in starting_point:
            starting_point.remove(deleted_cells[index])
    return starting_point


def specific_position_request():
    error = 1
    while error:
        print("do you want to choose a specific point to begin?! yes/no")
        starting_position_flag = input()
        if starting_position_flag == "yes":
            error = 0
            print("type your deleted cells (like:8,12,17):")
            deleted_cells = input().split(",")
            for i in range(0, len(deleted_cells)):
                deleted_cells[i] = int(deleted_cells[i])
            number_of_cells = int(input("how many columns you want in general?\n"))
            started_position = starting_position(deleted_cells, number_of_cells)  # same as possible_moves
            return started_position
        elif starting_position_flag == "no":
            error = 0
            return possible_moves
        else:
            print("Error: you type an incorrect answer! please try again!")


def two_players_option():
    error = 1
    while error:
        two_player_mode = input("do you want to play with two players?! yes/no\n")
        if two_player_mode == "yes":
            error = 0
            two_players = 1
            return two_players
        elif two_player_mode == "no":
            error = 0
            two_players = 0
            return two_players
        else:
            print("Error:you Enter incorrect answer! try again please!")
            continue


possible_moves = specific_position_request()
two_players_mode = two_players_option()
while possible_moves:
    #  begin of players moves
    print("player one:please choose a cell from:" + " " + str(possible_moves))
    player_one_input = int(input())
    if player_one_input not in possible_moves:
        print("Error_your input is not a possible move!")
        continue
    possible_moves = remove_chosen_cells(player_one_input)
    print("now remain cells are: " + str(possible_moves))
    if not possible_moves:
        print("player one wins the game! :)")
        player_one_wining_flag = 1
        break
    # second player role started here
    if two_players_mode == 0:  # play against pc
        player_two_move = nim_pick_and_divide()
        print("Computer select:" + " " + str(player_two_move))
        possible_moves = remove_chosen_cells(player_two_move)
    else:  # play with another player/two players mode
        print("player two please choose a cell from:" + " " + str(possible_moves))
        player_two_move = int(input())
        possible_moves = remove_chosen_cells(player_two_move)

if player_one_wining_flag == 0:
    print("player two wins the game! :)")

input("Press Enter to exit!")
