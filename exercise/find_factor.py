numberOfInput = input()
numberOfInput = int(numberOfInput)
counter = 1

while counter <= numberOfInput:
    number = input()
    number = int(number)
    i = 1

    print("Case", counter, end=": ")
    while i <= number:
        if number % i == 0:
            print(i, end=" ")
        i = i + 1
    print("\n")
    counter = counter + 1