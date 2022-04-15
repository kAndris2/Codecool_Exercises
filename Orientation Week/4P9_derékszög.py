""" 9. A program döntse el, hogy a bekért a , b , c természetes számok lehetnek-e egy derékszögű
háromszög oldalhosszúságai. Az a és b legyen a két befogó (használjuk Pitagorasz tételét). """

a = int(input("Add meg a háromszög egyik befogójának a méretét. \n"))
b = int(input("Add meg a háromszög másik befogójának a méretét. \n"))
c = int(input("Add meg a háromszög átfogójának a méretét. \n"))

if (a*a) + (b*b) == (c*c):
    print("Igen")
else:
    print("Nem!")