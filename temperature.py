print("Temperature Conversion Program")
print('Selection:::\nPress 1 to enter Celsius\nPress 2 to enter Farenheit\nPress 3 to enter Kelvin')

choice = int(input("Enter your selection:"))
    
    
if choice == 1 :
    temp = float(input("Enter temperature in Celsius:"))
    farenheit = round((((9/5)*temp)+32),2)
    kelvin = round((temp +273.15),2)
    print(' Temperature in Fahrenheit', farenheit,'deg F')
    print(' Temperature in Kelvin', kelvin,'deg K' )
    
elif choice == 2:
    temp = float(input("Enter temperature in Fahrenheit:")) 
    celsius = round(((5/9)*(temp -32)),2)
    kelvin = round(((temp + 459.67)*(5/9)),2)
    print(' Temperature in Celsius', celsius,'deg C')
    print(' Temperature in Kelvin', kelvin,'deg K')
    
elif choice == 3:
    temp = float(input("Enter temperature in Kelvin;"))
    celsius = round((temp - 273.15),2)
    farenheit = round(((temp*9/5)-459.67),2)
    print(' Temperature in Celsius', celsius,'deg C')
    print('Temperature in Fahrenheit', farenheit,'deg F')
    
else:
    print("Invalid option")