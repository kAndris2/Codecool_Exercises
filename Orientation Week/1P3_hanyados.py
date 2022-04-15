#3. Írjunk programot, amely beolvas két természetes számot, majd kiírja a két szám hányadosát és
#maradékát az alábbi formában. A program az adatok beolvasása után hagyjon ki egy üres sort.

a = int(input("Add meg az első számot.\n"))
b = int(input("\nAdd meg a második számot.\n"))

maradek = 0

if a == b:
    print("A bekért számok egyenlőek.")
    print("Hányados: 1 n\ Maradék: 0")
elif a > b:
     hanyados = a / b
     maradek = a % b
     print("Hányados: " + str(hanyados) + "\nMaradék: " + str(maradek))
elif b > a:
        hanyados = b / a
        maradek = b % a
        print("Hányados: " + str(hanyados) + "\nMaradék: " + str(maradek))