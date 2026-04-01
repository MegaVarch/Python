print("Enter marks obtained in 5 subjects: ")

mark_1 = int(input("Enter mark 1: "))
mark_2 = int(input("Enter mark 2: "))
mark_3 = int(input("Enter mark 3: "))
mark_4 = int(input("Enter mark 4: "))
mark_5 = int(input("Enter mark 5: "))

avg = ((mark_1+mark_2+mark_3+mark_4+mark_5)/5)

if avg>=91 and avg <=100:
    print("your marks are A1")

elif avg>=90 and avg <=81:
    print("your marks are A2")

elif avg>=80 and avg <=71:
    print("your marks are B1")

elif avg>=70 and avg <=61:
    print("your marks are B2")

elif avg>=60 and avg <=51:
    print("your marks are C1")

elif avg>=50 and avg <=41:
    print("your marks are C2")

elif avg>=40 and avg <=31:
    print("your marks are D")

elif avg>=30 and avg <=21:
    print("your marks are E1")

elif avg>=20 and avg <=11:
    print("your marks are E2")

else: 
    print("INVALID INPUT")


