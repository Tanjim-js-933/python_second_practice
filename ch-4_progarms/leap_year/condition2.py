year = input("Please enter a year: ")
year = int(year)
if year % 400 == 0:
    print("Yes")
elif year % 100 == 0:
    print("YEs")
elif year % 4 == 0:
    print("yES")
else:
    print("No") 
    