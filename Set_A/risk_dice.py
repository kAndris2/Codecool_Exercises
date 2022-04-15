attacker = 0
defender = 0

while True:
    attacker = int(input("How many attacker unit will play?\n"))
    if attacker == 0:
        print("\nThe number of attackers cannot be 0!\n")
    elif attacker <= 3:
        break
    else:
        print("\nThe maximum number of attackers is 3!\n")

while True:
    defender = int(input("How many defender unit will play?\n"))
    if defender == 0:
        print("\nThe number of defenders cannot be 0!\n")
    elif defender <= 2:
        break
    else:
        print("\nThe maximum number of defenders is 2!\n")

a_rand = []
a_dice = "  Attacker: "
a_out = 0
#
d_rand = []
d_dice = "  Defender: "
d_out = 0

import random

print("\nDice:")

for i in range(0, attacker):
    a_rand.append(random.randrange(1, 6+1))
    if i == 0:
        a_dice += str(a_rand[i])
    else:
        a_dice += ("-" + str(a_rand[i])) 
print(a_dice)

for i in range(0, defender):
    d_rand.append(random.randrange(1, 6+1))
    if i == 0:
        d_dice += str(d_rand[i])
    else:
        d_dice += ("-" + str(d_rand[i])) 
print(d_dice)

def Range_Count():
    if defender > attacker:
        return 1
    else:
        return defender

for i in range(0, Range_Count()):
    if a_rand[i] > d_rand[i]:
        d_out += 1
    elif d_rand[i] > a_rand[i]:
        a_out += 1
    elif a_rand[i] == d_rand[i]:
        a_out += 1

attacker -= a_out
defender -= d_out

def Check(value):
    if value == 0 or value > 1:
        return " units"
    elif value == 1:
        return " unit"
    return 0

print("\nOutcome:")

print("   Attacker: Lost " + str(a_out) + Check(a_out))
print("   Defender: Lost " + str(d_out) + Check(d_out) + "\n")
