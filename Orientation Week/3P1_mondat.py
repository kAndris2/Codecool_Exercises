#1. Készítsünk programot, amely bekér egy mondatot, majd kiírja ugyanezt a mondatot úgy, hogy mindegyik
#betű (karakter) után kirak egy szóközt.

mondat = input("Írj be egy mondatot.\n")

for i in range(len(mondat)):
    print(mondat[i] + ' ', end='')