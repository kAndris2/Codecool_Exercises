#9. Készítsen programot faktoriális számolásra.

fakt = int(input("Mennyi legyen a faktoriális értéke?\n"))

num = 1

for i in range(1, fakt+1):
    #print(i)
    num = num * i

print("A(z) " + str(fakt) + " faktoriálisa: " + str(num))

