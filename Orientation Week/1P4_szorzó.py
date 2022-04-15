#A program kérjen be egy számot, majd írja ki a kis szorzótáblát erre a számra (1-től 5-ig). A program a
#beolvasás után hagyjon ki egy üres sort.

x = int(input("Adj meg egy számot.\n"))

for i in range(1, 6):
    print(str(x * i) + " ", end='')
