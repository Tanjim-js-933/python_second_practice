saarc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

country = input("Enter the name of the country: ")
if country in saarc:
    print( country , "is a member of saarc")
else:
    print(country, "is not a member of saarc.")
    
print("Program Terminated.")