doors = []

while len(doors) < 100:
    doors.append(True)

step = 0
num = 0

while True:
    num += 1
    step += 1
    if num < 100:
        for i in range(0,100,step):
            doors[i] = not doors[i]
    else:
        break

print("Numbers of the open doors:")
for i in range(len(doors)):
    if doors[i] == False:
        print(i)
