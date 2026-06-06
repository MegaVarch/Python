try:
    age = int(input("Enter your age: "))
    if age%2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
except SyntaxError:
    print("Please enter a integer(your age)")
except ValueError:
    print("Please enter your age only")
finally:
    print("This will print no matter what")

