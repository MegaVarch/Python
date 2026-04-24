num = input("Enter a number: ")

if num[0] == '-':
    num = num[1:]

count = len(num)

print("Number of digits:", count)