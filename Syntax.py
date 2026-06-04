try:
    num1, num2 = eval(input("Enter 2 numbers separeated by a comma: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by 0 is error")
except SyntaxError:
    print("Numbers separated by comma like this 1,2")

except:
    print("Wrong input")

else:
    print("No exception")

finally:
    print("This will execute no matter what")
