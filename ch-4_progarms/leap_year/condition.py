ask_input = input("please enter a year: ")
ask_input = int(ask_input)

if ask_input % 4 == 0:
    if ask_input % 100 == 0:
        if ask_input % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")