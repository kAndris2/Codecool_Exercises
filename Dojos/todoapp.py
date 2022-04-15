import os

file_name = "to-do.txt"

while True:
    command = input("Please specify a command [list, add, mark, archive]: ")
    if command == "list" or command == "add" or command == "mark" or command == "archive":
        break

def List():
    file = open(file_name,"r")
    for i,line in enumerate(file):
        print("   " + str(i+1) + ". " + line)
    file.close()

if command == "list":
    print("You saved the following to-do items:")
    List()
elif command == "add":
    item = input("Add an item: ")
    file = open(file_name,"a")
    file.write("[] " + item + "\n")
    file.close()
    print("Item added.")
elif command == "mark":
    List()
    mark = int(input("Which one you want to mark as completed: "))
    mark -= 1
    with open(file_name) as file:
        content = file.read().splitlines()
    content[mark] = content[mark].replace("[]", "[x]")
    with open(file_name, "w") as file:
        for item in content:
            file.write("%s\n" % item)      
    print(content[mark].replace("[x]", "") + " is completed!")
elif command == "archive":
    with open(file_name) as file:
        content = file.read().splitlines()
    with open(file_name, 'w') as file:
        for i,line in enumerate(content):
            if line.find("[x]") != 0:
                file.write("%s\n" % line)
    print("All completed tasks got deleted.")
