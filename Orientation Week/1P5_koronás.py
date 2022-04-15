#5. Kérjünk be három természetes számot, ezek rendre 5, 2 és 1 koronásaink számát jelentik. Határozzuk
#meg, és írassuk ki a teljes összeget.

k_5 = int(input("Hány db 5 koronásod van?\n"))
k_2 = int(input("Hány db 2 koronásod van?\n"))
k_1 = int(input("Hány db 1 koronásod van?\n"))

print("\nÖsszeg: " + str( ( (k_5*5) + (k_2*2) + k_1) ) )