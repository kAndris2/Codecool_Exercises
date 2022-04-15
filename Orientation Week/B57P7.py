length = int(input("What is the length of the room in feet? \n"))
width = int(input("What is the width of the room in feet? \n"))

print("You entered dimensions of " + str(length) + " feet by " + str(width) + " feet.")

print("The area is")
print(str(length * width) + " square feet.")
m = 0.3048
meter = (width * m) * (length * m)
print(meter + " square meters")
