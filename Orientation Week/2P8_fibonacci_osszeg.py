m = int(input("Hány értéket írjak ki a sorozatból?\n"))

szam0 = 0
szam1 = 1
count = 0
osszeg = 0

while count < m:
    if m <= 0:
        print("Az érték nem lehet nulla vagy nála kisebb!")
    elif m == 1:
        print(szam0)
    else:
        osszeg = osszeg + szam0
        n = szam0 + szam1
        szam0 = szam1
        szam1 = n
        count +=1
print("Az első " + str(m) + " Fibonacci szám összege: " + str(osszeg))