#2. Kérjünk be egy keresztnevet, majd írassuk ki ezt a nevet betűnként függőlegesen lefelé a képernyőre.

nev = input("Írj egy egy nevet: \n")

for i in range(len(nev)):
    print(nev[i])