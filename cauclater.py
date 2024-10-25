def add(z, x):
    return z + x

def subtract(z,x):
    return z - x

def multiply(z,x):
    return z * x

def divide(z,x):
    return z / x

print('Select an Operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')    
print('4. Divide')     

choice = input("Enter your choice (1/2/3/4):")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")    
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}") 
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}") 

else:
    print("Invalid input, please try again!")      