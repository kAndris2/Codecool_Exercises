while True:
    try:
        num1 = int(input("Enter a number (or a letter to exit): "))

    except ValueError:
        break
    else:
        op = input("Enter an operation: ")
        num2 = int(input("Enter another number: "))
        num1 = int(num1)

        if op == "+":
            print("Result: " + str(num1 + num2) + "\n")
        elif op == "-":
            print("Result: " + str(num1 - num2) + "\n")
        elif op == "*":
            print("Result: " + str(num1 * num2) + "\n")
        elif op == "/":
            print("Result: " + str(num1 / num2) + "\n")
