import math



a = float(input("X coordinate of point A [-100, 100]: "))

while a < -100 or a > 100:

    a = float(input("Please enter a valid input (between -100 and 100): "))

b = float(input("Y coordinate of point A [-100, 100]: "))

while b < -100 or b > 100:

    b = float(input("Please enter a valid input (between -100 and 100): "))

c = float(input("X coordinate of point B [-100, 100]: "))

while c < -100 or c > 100:

    c = float(input("Please enter a valid input (between -100 and 100): "))

d = float(input("Y coordinate of point B [-100, 100]: "))

while d < -100 or d > 100:

    d = float(input("Please enter a valid input (between -100 and 100): "))

e = float(input("X coordinate of point C [-100, 100]: "))

while e < -100 or e > 100:

    e = float(input("Please enter a valid input (between -100 and 100): "))

f = float(input("Y coordinate of point C [-100, 100]: "))

while f < -100 or f > 100:

    f = float(input("Please enter a valid input (between -100 and 100): "))



# Calculating the lengths of all sides

side_a = math.sqrt((c - a)**2 + (d - b)**2)

side_b = math.sqrt((e - a)**2 + (f - b)**2)

side_c = math.sqrt((e - c)**2 + (f - d)**2)



# Semi-perimeter for Heron's formula

s = ((side_a + side_b + side_c) / 2)



# Heron's formula for area

area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))



print("Triangle's area is: ", round(area, 2))