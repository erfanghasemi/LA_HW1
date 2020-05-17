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
