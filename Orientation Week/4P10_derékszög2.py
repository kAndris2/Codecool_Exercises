""" 10. A program döntse el, hogy a bekért a , b , c, természetes számok lehetnek-e egy derékszögű
háromszög oldalhosszúságai. A programot úgy írjuk meg, hogy az a , b , c számok közül bármelyik
lehet a háromszög átfogója, a maradék kettő pedig a befogók (használjuk Pitagorasz tételét). """

a = int(input("Első érték: \n"))
b = int(input("Második érték: \n"))
c = int(input("Harmadik érték: \n"))
atf = 0
b1 = 0
b2 = 0


if a > b and a > c:
    atf = a
elif b > a and b > c:
    atf = b
elif c > a and c > b:
    atf = c

#print("Átfogó: " + str(atf))

if a != atf:
    if b1 == 0:
        b1 = a
    else:
        b2 = a

if b != atf:
    if b1 == 0:
        b1 = b
    else:
        b2 = b

if c != atf:
    if b1 == 0:
        b1 = c
    else:
        b2 = c

if (b1*b1) + (b2*b2) == (atf*atf):
    print("Igen")
else:
    print("Nem")