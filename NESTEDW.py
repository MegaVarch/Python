string = input("Please Enter your own word: ")

char = input("Please enter your own character: ")
i = 0
count = 0
while (i < len(string)): 
    if (string[i] == char):
        count = count + 1
    i = i + 1

print("THE TOTAL NUMBER OF TIMES",char, "HAS OCCURED IS ",count)
