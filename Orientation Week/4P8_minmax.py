""" 8. Egészítsük ki az előző programunkat úgy, hogy a beolvasás után a számok közül ne csak a legkisebbet,
de a legnagyobbat is írja ki. (Ehhez vezessünk be egy max nevű változót, melyet mindegyik szám
beolvasása után összehasonlítunk a számmal, és ha a szám nagyobb, akkor megjegyezzük ebben a
változóban. A max változót a program elején állítsuk be a lehető legkisebb számra, aminél biztos hogy
mindegyik szám nagyobb - pl. –32767, vagy ez helyett a beállítás helyett az első számot olvassuk be
(állítsuk be) a max változóba.) """

num = int(input("Add meg hány számból álljon a sor. \n"))

min = 32768
max = -32767
i = 1

while i < num+1:
    num2 = int(input("Add meg az " + str(i) + "./" + str(num) + " elemet.\n"))
    if num2 < min:
        min = num2
    if num2 > max:
        max = num2
    i += 1
    
print("A legkisebb szám a(z) '" + str(min) + "' volt.")
print("A legnagyobb szám a(z) '" + str(max) + "' volt.")