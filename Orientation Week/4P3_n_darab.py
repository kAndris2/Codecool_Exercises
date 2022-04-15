""" 3. Kérjünk be N darab természetes számot (először N -t kérjük be). Az adatok beírása után a program
írja ki a páros és páratlan számok darabszámát, és a páratlan számok összegét! """

szam = int(input("Hány db számból álljon a sorozat?\n"))
c_paros = 0
c_paratlan = 0
paratlan_osszeg = 0
i = 0

while i < szam :
    num = int(input("Add meg az " + str(i+1) + "./" + str(szam) + " számot\n"))
    i += 1
    if (num % 2) == 0:
        c_paros += 1
    else:
       c_paratlan += 1
       paratlan_osszeg += num

print(str(c_paros) + "db páros számot írtál be.\n") 
print(str(c_paratlan) + "db páratlan számot írtál be.\n")
print("A páratlan számok összege: " + str(paratlan_osszeg))