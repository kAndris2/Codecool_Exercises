matrix1 = [[1,3,'A'], ['B','A','C'], [9,'B',4]]
matrix2 = [[1,'A','A'], ['B','B','C'], [4,'A','C']]

val_A = 0
val_B = 0
val_C = 0

for i in range(len(matrix2)):
    row = matrix2[i]
    for j in range(len(row)):
        val = matrix2[i][j]
        if type(val) == str and val == 'A':
            val_A += 1
        elif type(val) == str and val == 'B':
            val_B += 1
        elif type(val) == str and val == 'C':
            val_C += 1

for i in range(len(matrix1)):
    row = matrix1[i]
    for j in range(len(row)):
        val = matrix1[i][j]
        if type(val) == str and val == 'A':
            matrix1[i][j] = val_A
        elif type(val) == str and val == 'B':
             matrix1[i][j] = val_B
        elif type(val) == str and val == 'C':
             matrix1[i][j] = val_C

print(matrix1)