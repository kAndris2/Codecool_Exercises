#5. Kérjünk be egy természetes számot ( a ), majd rajzoljunk ki a képernyőre egy háromszöget csillagokból
#( * ). A háromszög a sornyi csillagból álljon.

x = int(input("Add meg hány sorból álljon a piramis. "))

for i in range(x):
    ws = ' ' * (x - i)
    st = '*' * i
    print(ws + st + "*" + st + ws)