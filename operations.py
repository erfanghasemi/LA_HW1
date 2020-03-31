<<<<<<< HEAD
def det_nonzero_coulmn(matrix, coulmns, rows):
    for i in range(coulmns):
        for j in range(rows):
            if matrix[j][i] != 0:
                return i


def sel_pivet_position(matrix, pivet_coulmn, rows):
    for i in range(rows):
        if matrix[i][pivet_coulmn] != 0:
            return i


def interchange_rows(matrix, coulmns, first_row, second_row):
    temp_row = []
    for i in range(coulmns):
        temp_row.append(matrix[first_row][i])
        matrix[first_row][i] = matrix[second_row][i]
        matrix[second_row][i] = temp_row[i]


# def row_replacements_U(matrix, coulmns, rows, pivet_row, pivet_coulmn):
#     for i in range(pivet_row):
#         scale = (-1) * (matrix[pivet_row][pivet_coulmn] / matrix[i][pivet_coulmn])
#         for j in range(coulmns):
#             matrix[i][j] = (scale * matrix[i][j]) + matrix[pivet_row][j]


def row_replacements_D(matrix, coulmns, rows, pivet_row, pivet_coulmn):
    for i in range(pivet_row + 1, rows):
        scale = (-1) * (matrix[pivet_row][pivet_coulmn] / matrix[i][pivet_coulmn])
        # print(scale)
        for j in range(coulmns):
            matrix[i][j] = (scale * matrix[i][j]) + matrix[pivet_row][j]


def sacle_row(matrix, coulmns, pivet_row, pivet_coulmn):
    for i in range(coulmns):
        matrix[pivet_row][i] = matrix[pivet_row][i] / matrix[pivet_row][pivet_coulmn]


def det_end_operation(matrix, coulmns, rows):
    for i in range(rows):
        for j in range(coulmns):
            if matrix[i][j] != 0:
                return 0
    return 1
=======
def display_matrix(matrix, size):      # function for display a matrix from 2D array
    for row in range(size):
        for column in range(size+1):

            if round(matrix[row][column], 2) - int(matrix[row][column]) == 0:
                print("%9.0d" % matrix[row][column], end='')

            else:
                print("%9.2f" % matrix[row][column], end='')

        print("\n")


def det_nonzero_column(matrix, column, start_row, size):   # this function detect of existence of a nonzero
    for row in range(start_row, size):                       # element in specific column to change rows
        if matrix[row][column] != 0:
            return row
    else:
        return -1


def interchange_rows(matrix, first_row, second_row):       # this function interchange two rows
    matrix[[first_row, second_row]] = matrix[[second_row, first_row]]
    return matrix


def row_replacements_forward(matrix, size, pivot_row, pivot_column):   # this function make 0
    for row in range(pivot_row + 1, size):                             # elements that below the pivot positions
        if matrix[row][pivot_column] != 0:
            scale = (-1) * (matrix[row][pivot_column] / matrix[pivot_row][pivot_column])
            for column in range(size+1):
                matrix[row][column] = (scale * matrix[pivot_row][column]) + matrix[row][column]
            print("\n\n")
            print("Row Replacement Forward Operation In Column %d By Scale size ( %1.2f ) For Row : %d  ---> \n\n" % (pivot_column+1, scale, row + 1))
            display_matrix(matrix, size)
    return matrix


def scale_pivots(matrix, size, pivot_row, pivot_column):      # this function make 1 pivot positions
        scale = matrix[pivot_row][pivot_column]
        if scale != 1:
            for column in range(size+1):
                matrix[pivot_row][column] = matrix[pivot_row][column] / scale
            print("\n\n")
            print("Scaling Operation By Scale size ( %1.2f ) On Row : %d  ---> \n\n" % (scale, pivot_row + 1))
            display_matrix(matrix, size)
        return matrix


def row_replacements_backward(matrix, size, pivot_row, pivot_column):      # this function make 0
    for row in range(pivot_row):                                           # elements that above the pivot positions
        scale = (-1) * matrix[row][pivot_column]
        for column in range(size+1):
            matrix[row][column] = (scale * matrix[pivot_row][column]) + matrix[row][column]
        print("\n\n")
        print("Row Replacement backward Operation In Column %d By Scale size ( %1.2f ) For Row : %d  ---> \n\n" % (pivot_column+1, scale, row+1))
        display_matrix(matrix, size)
    return matrix
>>>>>>> calculate row echelon matrix added.
