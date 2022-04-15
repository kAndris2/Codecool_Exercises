#3. Készítsünk programot, amely kiszámolja az első 100 db páros szám összegét. (A ciklust vegyük egytől
#százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét - így megkapjuk a páros számokat.
#Ezeket hasonlóan adjuk össze, mint az első feladatban.)

szam = 0
for i in range(100):
    if i % 2 == 0:
        szam = szam + i
print(szam)