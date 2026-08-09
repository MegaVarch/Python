marks = [85, 72, 91, 68, 79]

print("Marks:", marks)
print("Number of subjects:", len(marks))

print("First mark:", marks[0])
print("First three marks:", marks[:3])

print("All marks:")
for mark in marks:
    print(mark)

total = sum(marks)
average = total / len(marks)
smallest = min(marks)
largest = max(marks)

print("Total:", total)
print("Average:", average)
print("Smallest:", smallest)
print("Largest:", largest)