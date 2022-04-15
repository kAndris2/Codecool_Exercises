""" 4. Olvassunk be egy a természetes számot és egy ch karaktert. Rajzoljunk ki a beolvasott karakterből
egy a oldalú négyzetet a képernyőre (minden sorban a db karakter legyen és összesen a db
sorunk legyen) egymásba ágyazott cilusok segítségével. """

szam = int(input("Írj be egy számot: \n"))
char = input("Adj meg egy karaktert: \n")

for i in range(szam):
    print(char*szam)