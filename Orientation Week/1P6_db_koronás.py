#A program kérjen be egy pénzösszeget, majd határozza meg, és írja ki, hogy hogyan fizethetjük ki a
#lehető legkevesebb 10, 5, 2 és 1 koronás érmével (használjuk a maradékos osztás % és egész osztás
#// műveleteket)!

osszeg = int(input("Adj meg egy összeget.\n"))
v_10 = 0
v_5 = 0
v_2 = 0
v_1 = 0
o = 0

if osszeg >= 10:
    if osszeg % 10 == 0:
        v_10 = osszeg / 10
    else:
        v_10 = osszeg / 10
        o = osszeg % 10
else:
    v_10 = 0

if o >= 5:
    if o % 5 == 0:
        v_5 = o / 5
    else:
        v_5 = o
        o = o % 5
else:
    v_5 = 0

if o >= 2:
    if o % 2 == 0:
        v_2 = o / 2
    else:
        v_2 = o / 2
        o = o % 2
else:
    v_2 = 0

#v_1 = o

print("Az összeg " + str(osszeg) + "Ft.")
print(str(v_10) + "db 10 koronás")
print(str(v_5) + "db 5 koronás")
print(str(v_2) + "db 2 koronás")
print(str(v_1) + "db 1 koronás")
