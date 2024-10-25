def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 24 ) * 2 / 4
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celcius = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit}F is equal to {celcius}C ")