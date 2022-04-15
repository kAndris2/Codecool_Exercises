#4. Készítsünk programot, amely kiszámolja az első 100 db páratlan szám összegét. (A ciklust vegyük egytől
#százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét eggyel csökkentve - így megkapjuk a
#páratlan számokat. Ezeket hasonlóan adjuk össze, mint az első feladatban).

szam = 0

for i in range(100):
    if i % 2 != 0:
        szam = szam + i
print(szam)