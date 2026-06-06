import random 

while True:
    user_action = input("Enter a choice (ROCK. PAPER, SCISSORS): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose ) {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both player selected {user_action} ITS A TIE!!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors YOU WIN")
        else:
            print("Paper covers rock YOU LOSE")
    elif user_action == "paper" :
        if computer_action == "scissors":
           print("Paper covers rock You Win")
        else:
            print("Scissors cuts paper You Lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper You Win")
        else:
            print("Rock smashes Scissors You Lose")


    play_again = input("Play again (y\n): ")
    if play_again != "y":
        break
            

