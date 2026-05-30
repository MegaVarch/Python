import os

def shutdown():
    choice = input("Do you want to shut down the system? (Yes/No): ")

    if choice == "Yes":
        print("System will shut down in 60 seconds.")
        os.system("shutdown /s /t 60")
    elif choice == "No":
        print("Abort shutdown")
        os.system("shutdown /a")
    else:
        print("Sorry")

shutdown()