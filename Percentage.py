print("Enter marks obtained in 4 subjects: ")
math = int(input("Marks in maths: "))
English = int(input("Marks in English: "))
Hindi = int(input("Marks in Hindi: "))
Science = int(input("Marks in Science: "))


sum = English+math+Science+Hindi
print("Sum of math,English,Hindi,Science = ",sum)

perc = (sum/400)*100
print(end="Percentage mark: ")
print(perc)
