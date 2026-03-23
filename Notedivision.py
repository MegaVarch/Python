Amount = int(input("Please Enter amount for withdraw: "))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of rupee 100:", note_1)
print("Notes of rupee 50:", note_2)
print("Notes of rupee 10:", note_3)