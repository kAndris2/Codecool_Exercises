mondat = input("Adj meg egy mondatot. \n")
ascii = 0

for i in range(len(mondat)): 
    if mondat[i] == 'x' or mondat[i] == 'y' or mondat[i] == 'z' or mondat[i] == 'X' or mondat[i] == 'Y' or mondat[i] == 'Z':
        ascii = ord(mondat[i]) - 23
    else:
        ascii = ord(mondat[i])
        ascii = ascii + 3
    print(chr(ascii), end="")