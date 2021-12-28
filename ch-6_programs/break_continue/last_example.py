terminate = False
while not terminate:
    number1 = input("Please enter a number: ")
    number1 = int(number1)
    number2 = input("Please enter an another number: ")
    number2 = int(number2)
    
    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation.lower() == "quit":
            terminate = True
            break
        elif operation not in ["add", "sub"]:
            print("Unknown operation")
            continue
        elif operation == "add":
            print("Result is", number1 + number2)
            break
        elif operation == "sub":
            print("Result is", number1 - number2)
            break