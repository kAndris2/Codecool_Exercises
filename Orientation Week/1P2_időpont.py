#Kérjünk be két, egy napon belüli, időpontot (először az órát, aztán a percet, végül a másodpercet).
#Számítsuk ki a két időpont közti különbséget másodpercekben és írassuk ki!

hour = int(input("1.Óra: "))
minute = int(input("1.Perc: "))
sec = int(input("1.Másodperc: "))

hour2 = int(input("2.Óra: "))
minute2 = int(input("2.Perc: "))
sec2 = int(input("2.Másodperc: "))

print("1.Időpont: " + str(hour) + ":" + str(minute) + ":" + str(sec))
print("2.Időpont: " + str(hour2) + ":" + str(minute2) + ":" + str(sec2))

t1 = (hour * 3600) + (minute * 60) + sec
t2 = (hour2 * 3600) + (minute2 * 60) + sec2

print("Az időpontok közötti különbség " + str(abs(t1-t2)) + "mp")
 

