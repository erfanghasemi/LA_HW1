<<<<<<< HEAD
import operations

# This is a program to convert a Matrix to row echelon matrix.

print("Please enter size of your Matrix")  # first enter number of rows an next coulmns

Nrows = int(input("\nrows: "))
Ncoulmns = int(input("coulmns: "))

primary_matrix = [[0 for i in range(Ncoulmns)] for j in range(Nrows)]
result_matrix = [[0 for i in range(Ncoulmns)] for j in range(Nrows)]

print("\nPlease enter indexes of your Matrix")  # enter indexes of Matrix

for i in range(0, Nrows):
    one_row = input("")
    splited_row = one_row.split(" ")
    row = []
    for j in range(0, splited_row.__len__()):
        if splited_row[j].isdigit():
            row.append(int(splited_row[j]))
    primary_matrix[i] = row

row_result = 0

while True:
    pivet_coulmn = operations.det_nonzero_coulmn(primary_matrix, Ncoulmns, Nrows)
    pivet_row = operations.sel_pivet_position(primary_matrix, pivet_coulmn, Nrows)
    operations.interchange_rows(primary_matrix, Ncoulmns, pivet_row, 0)
    operations.row_replacements_D(primary_matrix, Ncoulmns, Nrows, pivet_row, pivet_coulmn)
    Nrows -= 1

    for i in range(Ncoulmns):
        result_matrix[row_result][i] = primary_matrix[0][i]
    row_result += 1

    primary_matrix.remove(primary_matrix[0])

    if operations.det_end_operation(primary_matrix, Ncoulmns, Nrows) == 1:
        break

print(result_matrix)
=======
import numpy as np
import operations as op

# This is a program to convert a Matrix to row echelon matrix.

print("Please enter size of your Matrix : ")  # first enter size of n

n = int(input())
entries = []    # array for elements of matrix

for row in range(n):
    entries = entries + list(map(float, input().split()))     # input elements of each line
matrix_A = np.array(entries).reshape(n, n)      # create n * n array with numpy library by using reshape func

vector_b = list(map(float, input().split()))       # input elements of vector b

augmented_matrix = np.column_stack((matrix_A, vector_b))     # create augmented matrix of [A | b] by using column stack

print("Augmented Matrix   ---> \n\n")
op.display_matrix(augmented_matrix, n)      # display augmented matrix of [A | b]
print("\n")

complete_row = 0       # number of rows that find pivot in them
pivotPositions = []    # list of pivot positions
for column in range(n+1):

    pivot_r_position = op.det_nonzero_column(augmented_matrix, column, complete_row, n)   # find the first none_zero
    if pivot_r_position == -1:                                                            # elements in specific column
        continue
    else:
        pivotPositions.append(tuple([complete_row, column]))     # add pivot position to list of them
        augmented_matrix = op.interchange_rows(augmented_matrix, complete_row, pivot_r_position)
        if pivot_r_position != complete_row:                                                # change two rows if needed
            print("Rows Interchange Operation For Rows : %d and %d ---> \n\n" % (pivot_r_position+1, complete_row+1))
            op.display_matrix(augmented_matrix, n)

    augmented_matrix = op.row_replacements_forward(augmented_matrix, n, complete_row, column)

    complete_row += 1


for pivot_row, pivot_column in pivotPositions:       # this section make 1 pivot positions
    augmented_matrix = op.scale_pivots(augmented_matrix, n, pivot_row, pivot_column)

for pivot_row, pivot_column in reversed(pivotPositions):  # this section make 0 elements that above the pivot positions
    augmented_matrix = op.row_replacements_backward(augmented_matrix, n, pivot_row, pivot_column)

state_answer = 0    # state 0 for consistence and state 1 for inconsistence

for pivot_row, pivot_column in reversed(pivotPositions):
    if pivot_column == n:
        state_answer = 1
        break

if state_answer == 1:
    print("System of equations doesn't have any answer.")
elif len(pivotPositions) < n:
    print("System of equations have countless answers.")
else:
    print("Answer : \n")
    for row in range(n):       # printing the unique answer
        if round(augmented_matrix[row][n], 2) - int(augmented_matrix[row][n]) == 0:
            print("        X%d = %2.0d\n" % (row+1, augmented_matrix[row][n]))
        else:
            print("        X%d = %2.2f\n" % (row+1, augmented_matrix[row][n]))
>>>>>>> calculate row echelon matrix added.
