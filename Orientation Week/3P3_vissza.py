#3. Készítsünk programot, amely bekér egy mondatot, majd kiírja ugyanezt a mondatot fordítva.

mondat = input("Írj be egy mondatot: \n")

for i in reversed(range(len(mondat))):
    print(mondat[i], end="")