ask = input()
i = 0 
ask = int(ask)

while i < ask:
    i += 1
    in1 = input()
    in1 = int(in1)
    if in1 % 2 == 0:
        print("even.")
    else:
        print("odd.")
