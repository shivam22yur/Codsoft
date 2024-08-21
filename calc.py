def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Can't divide by zero!"
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Answer:", add(num1, num2))
        elif choice == '2':
            print("Answer:", sub(num1, num2))
        elif choice == '3':
            print("Answer:", multi(num1, num2))
        elif choice == '4':
            print("Answer:", div(num1, num2))
    else:
        print("Invalid Input")