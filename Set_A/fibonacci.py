m = int(input("How many numbers should I print out of the sequance? \n"))

szam0 = 0
szam1 = 1
count = 1

print("\nFibonacci sequance:")

while count < m+1:
    print(str(count) + ". " + str(szam0))
    n = szam0 + szam1
    szam0 = szam1
    szam1 = n
    count +=1
