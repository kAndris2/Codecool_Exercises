""" 6. Olvassunk be egy szöveget, majd írassuk ki a képernyőre a beolvasott szövegből az összes < és >
jelek közé írt részeket, mindegyiket új sorba. """

mondat = "<Gabor> és Denes <fel>masztak <a diofa>ra."
start = 0
stop = 0

for i in range(len(mondat)): 
        if mondat[i] == '<':
                start = i + 1
        if mondat[i] == '>':
                stop = i
                print(mondat[start:stop])