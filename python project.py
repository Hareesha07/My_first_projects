def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def Division(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter ypur choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        if choice == '1':
            print("Result:", addition(number1, number2))
        elif choice == '2':
            print("Result:", subtraction(number1, number2))
        elif choice == '3':
            print("Result:", multiplication(number1, number2))
        elif choice == '4':
            print("Result:", Division(number1, number42))
        
        One_More_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if One_More_calculation.lower() != 'yes':
            break
    else:
        print("Invalid input")