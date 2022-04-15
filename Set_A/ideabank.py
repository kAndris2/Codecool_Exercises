import sys

file_name = "ideabank.txt"

def List():
    file = open(file_name,"r")
    print("\nYour ideabank:")
    for i,line in enumerate(file):
        print(str(i+1) + ". " + line)
    file.close()

if len(sys.argv) > 1:
    if sys.argv[1] == "--list":
       List()
    elif sys.argv[1] == "--delete" and int(sys.argv[2]) > 0:
        file = open(file_name,"r+")
        list = list(file)
        file.close()
        del list[int(sys.argv[2]) - 1]
        #
        file = open(file_name,"w")
        for i in list:
            file.write(i)
        file.close()
        List()
else:
    idea = input("What is your new idea: ")
    file = open(file_name,"a")
    file.write(idea + "\n")
    file.close()
    List()
