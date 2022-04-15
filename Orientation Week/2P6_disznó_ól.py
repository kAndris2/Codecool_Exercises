x = int(input("Magasság: "))
y = int(input("Szélesség: "))

for i in range(x):
    for n in range(y):
        if i == 0 or i == x-1 or n == 0 or n == y-1 :
            print("*", end='')
        else:
            print(" ", end='')
    print()