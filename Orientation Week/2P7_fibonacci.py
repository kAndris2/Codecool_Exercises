m = int(input("Hány értéket írjak ki a sorozatból?\n"))

szam0 = 0
szam1 = 1
count = 0

while count < m:
    if m <= 0:
        print("Az érték nem lehet nulla vagy nála kisebb!")
    elif m == 1:
        print(szam0)
    else:
        print(szam0, end=' ')
        n = szam0 + szam1
        szam0 = szam1
        szam1 = n
        count +=1