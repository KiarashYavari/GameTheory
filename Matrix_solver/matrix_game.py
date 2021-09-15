# Initialize matrix

player_one_strategies = []
player_two_strategies = []


def getting_input():
    matrix = []
    Rows_Numbers = int(input("How many Rows do you have?\n"))
    Columns_Number = Rows_Numbers  # numbers of rows and columns ae the same
    # For user input # get user's matrix
    for i in range(Rows_Numbers):  # A for loop for row entries
        print("Enter the value Row" + str(i) + " :")
        a = []
        for j in range(Columns_Number):  # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)
    return matrix


#  add a column of 1 end with 0, row of -1 end with 0
#  1  2  3  1
#  4  5  6  1
#  7  8  9  1
# -1 -1 -1  0
def adding_row_column(Rows_Number, Columns_Number, in_matrix):
    matrix_a = in_matrix
    for i in range(Rows_Number):
        matrix_a[i].append(1)

    extended_rows = []
    for j in range(Columns_Number):
        extended_rows.append(-1)
    matrix_a.append(extended_rows)
    matrix_a[len(matrix_a) - 1].append(0)
    return matrix_a


# find the lola
def finding_lola(input_matrix):
    Lola = None
    Lola_position = []
    for index_i in range(len(input_matrix)):
        for index_j in range(len(input_matrix[index_i])):
            if input_matrix[index_i][index_j] > 0:
                last_row = input_matrix[len(input_matrix) - 1]
                if last_row[index_j] < 0:
                    Candidate = input_matrix[index_i][len(input_matrix[index_i]) - 1] / input_matrix[index_i][index_j]
                    if Lola:
                        if Candidate < Lola:
                            Lola = Candidate
                            Lola_position = [index_i, index_j]
                    else:
                        Lola = Candidate
                        Lola_position = [index_i, index_j]
            else:
                pass
    return Lola_position


def printing_matrix(num_of_rows, num_of_columns, Matric):  # For printing the matrix
    for i in range(num_of_rows):
        for j in range(num_of_columns):
            print(Matric[i][j], end="   ")
        print()


def check(list1, val):  # check last row to see if all elements are positive
    # traverse in the list
    for x in list1:

        # compare with all the values
        # with val
        if val > x:
            return True
    return False


# not right
def updating_matrix(lola_pos):
    new_matrix = matrix
    P = matrix[lola_pos[0]][lola_pos[1]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == lola_pos[0] and j == lola_pos[1]:  # lola element
                new_matrix[i][j] = 1 / matrix[i][j]  # reverse Lola value
            elif i == lola_pos[0]:  # rows of lola
                new_matrix[i][j] = matrix[i][j] / P
            elif j == lola_pos[1]:  # columns of lola
                new_matrix[i][j] = -(matrix[i][j] / P)
            else:  # not lola's rows or columns
                r = matrix[lola_pos[0]][j]
                c = matrix[i][lola_pos[1]]
                new_matrix[i][j] = matrix[i][j] - (r * c / P)

    return new_matrix


# main procedure of game
print(" welcome! if you think the matrix game might have  a value <=0 then add a positive "
      "value to all elements "" then Enter it here!")
matrix = getting_input()  # Rows and Columns have the same Number
Rows_Numbers = len(matrix)
# add column of one's and rows of -1 ends with 0
matrix = adding_row_column(Rows_Numbers, Rows_Numbers, matrix)

for pointer in range(Rows_Numbers):
    player_one_strategies.append('x' + str(pointer + 1))  # [x1,x2,x3]
for pointer in range(Rows_Numbers):
    player_two_strategies.append('y' + str(pointer + 1))

last_row_check = matrix[len(matrix) - 1]

while check(last_row_check, 0):  # check the ending condition
    Lola_position = finding_lola(matrix)
    matrix = updating_matrix(Lola_position)
    if Lola_position[0] < Rows_Numbers and Lola_position[1] < Rows_Numbers: # changing Labels
        Temp = player_one_strategies[Lola_position[0]]
        player_one_strategies[Lola_position[0]] = player_two_strategies[Lola_position[1]]
        player_two_strategies[Lola_position[1]] = Temp

added_value_to_game = int(input("gave me the value you add at first to each matrix elements\n"))
value_of_game = 1 / (matrix[len(matrix) - 1][len(matrix) - 1] - added_value_to_game)

optimal_strategies_one = []  # calculate player one optimal strategies
optimal_strategies_two = []  # calculate player two optimal strategies
for indexes in range(len(player_one_strategies)):
    if 'x' in player_one_strategies[indexes]:
        optimal_strategies_one.append(0)  # for the left side x
    else:
        optimal_strategies_two.append(matrix[indexes][len(matrix[indexes])-1] * value_of_game)

for indexes in range(len(player_two_strategies)):
    if 'y' in player_two_strategies[indexes]:
        optimal_strategies_two.append(0)  # for the up side y's
    else:
        optimal_strategies_one.append(matrix[len(matrix[indexes])-1][indexes] * value_of_game)

print("value of game is: " + str(value_of_game) +
      " ,player one optimal strategies are " + str(optimal_strategies_one)
      + " and player two optimal strategies are " + str(optimal_strategies_two))
