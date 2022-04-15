""" 4. Készítsünk programot, ami bekér egy évszámot, és meghatározza, majd kiírja a húsvét vasárnap
dátumát!
A húsvét vasárnap dátumát a níceai zsinat a következőképpen határozta meg: a tavaszi
napéjegyenlőséget követő első holdtölte utáni első vasárnap.
A dátum március 22-e és április 25-e között változhat. A dátum meghatározására alkalmas a következő
algoritmus!
Jelölje T az évszámot ( 1800 <= T <= 2099 ). Kiszámítjuk a következő osztási maradékokat
A = T / 19 maradéka
B = T / 4 maradéka
C = T / 7 maradéka
D = (19 * A + 24) / 30 maradéka
E = (2 * B + 4 * C + 6 * D + 5) / 7 maradéka
Ezekből a húsvét vasárnap dátuma
H = 22 + D + E , ami márciusi dátum, ha H <= 31 , különben áprilisban H – 31 -e.
Két kivétel van:
ha E = 6 és D = 29 , akkor H = 50 ,
ha E = 6 és D = 28 és A > 10 , akkor H = 49 . """

T = int(input("Adj meg egy évszámot. \n"))
A = T % 19
B = T % 4
C = T % 7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C + 6 * D + 5) % 7
H = 22 + D + E

if E == 6 and D == 29:
    H = 50
if E == 6 and D == 28 and A > 10:
    H = 49

if H <= 31:
    print(str(T) + ".Március." + str(H))
elif H > 31:
    print(str(T) + ".Április." + str(H-31))