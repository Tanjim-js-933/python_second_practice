test_cases = int(input())
for i in range(test_cases):
    number = int(input())
    multiplier = 1
    print("Case", (i+1), end=": ")
    while(multiplier <= number/2):
        if(number%multiplier == 0):
            print(multiplier)
        multiplier += 1
    print(number)