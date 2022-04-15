numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
numbers2 = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]

min = 0
max = 0
max_val = 0
num_add = 0

for row,num in enumerate(numbers):
    #Min
    if num <= min:
        min = num
    #Max
    if num >= max:
        max = num
    #AVG
    if row >= max_val:
        max_val = row
    num_add += num

print("\n[1st List]:")
print("Minimum: " + str(min))
print("Maximum: " + str(max))
print("Average: " + str((num_add/(max_val+1))))

min = 0
max = 0
max_val = 0
num_add = 0

for row,num in enumerate(numbers2):
    if type(num) == int:
         #Min
        if num <= min:
            min = num
        #Max
        if num >= max:
            max = num
        #Avg
        if row >= max_val:
            max_val = row
        num_add += num

    elif type(num) == list:
        max_r = 0
        for i, j in enumerate(num):
            if type(j) == int:
                if j < min:
                    min = j
                if j > max:
                    max = j
                if i >= max_r:
                    max_r = i
                num_add += j
                max_val += max_r

print("\n[2nd List]:")
print("Minimum: " + str(min))
print("Maximum: " + str(max))
print("Average: " + str((num_add/max_val)))
