string = input("Please enter your own string: ")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nOriginal string was", string)
print("\nReversed string is ", string2)
