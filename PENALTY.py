import random

print("FOOTBALL PENALTY GAME ")

score = 0

for i in range(5):

    print("\nRound", i + 1)
    print("1 = Left")
    print("2 = Center")
    print("3 = Right")

    player = input("Choose your shot: ")

    goalkeeper = random.randint(1, 3)

    if player not in ["1", "2", "3"]:
        print(" Invalid choice!")
        continue

    player = int(player)

    if player == goalkeeper:
        print(" SAVED by goalkeeper!")
    else:
        print(" GOOOOAL!")
        score += 1

print("\n Final Score:", score, "/5")