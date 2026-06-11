def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Enter your choice:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("DIVIDE")
equation = int(input("Enter your operation number: "))

num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))


if equation == 1:
    print(num1 + num2)

elif equation == 2:
    print(num1 - num2)

if equation == 3:
    print(num1 * num2)

if equation == 4:
    print(num1 / num2)