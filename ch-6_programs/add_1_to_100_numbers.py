result = 0
for num in range(1, 100):
    if num % 5 == 0:
        print(num)
        result = result + num
print('Sum is', result)