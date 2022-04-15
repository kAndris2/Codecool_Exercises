matrix = [[1,4,7], [9,2,1], [1,2,3]]
result = 0

for i in range(len(matrix)):
    row = matrix[i]
    for j in range(len(row)):
        num = matrix[i][j]
        if ((i == 0) and (j == 0)) or ((i == 1) and (j == 1)) or ((i == 2) and (j == 2)):
            print(num)
            result += num
print("A mátrix keresett elemeinek összege: " + str(result))