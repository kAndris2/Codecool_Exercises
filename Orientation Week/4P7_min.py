""" 7. Készítsünk programot, amely beolvas egy N természetes számot, majd billentyűzetről bekér N db
természetes számot és a beolvasás után kiírja melyik ezek közül a számok közül a legkisebb. (Ehhez
vezessünk be egy min nevű változót, melyet mindegyik szám beolvasása után összehasonlítunk a
számmal, és ha a szám kisebb, akkor megjegyezzük ebben a változóban. A min változót a program
elején állítsuk be a lehető legnagyobb számra, aminél biztos hogy mindegyik szám kisebb - pl. 32768,
vagy e helyett a beállítás helyett az első számot olvassuk be (állítsuk be) a min változóba.) """

num = int(input("Add meg hány számból álljon a sor. \n"))

min = 32768
i = 1

while i < num+1:
    num2 = int(input("Add meg az " + str(i) + "./" + str(num) + " elemet.\n"))
    if num2 < min:
        min = num2
    i += 1
    
print("A legkisebb szám a(z) '" + str(min) + "' volt.")