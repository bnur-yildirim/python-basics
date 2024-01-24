import random

print("""Welcome to the rock paper and scissors game!
Type r for rock, s for scissors, p for paper and y for quit.""")

choices = ["r", "p", "s"]
userScore = 0
compScore = 0
userChoice = "n"

while userChoice != "y":
    compChoice = random.choice(choices)
    
    userChoice = input("Type (r/p/s) or y to quit: ").lower()
    
    match userChoice:
        case "r":
            if compChoice == "r":
                print("Computer chose rock. No one gets a point.")
            elif compChoice == "s":
                print("Computer chose scissors. You get a point.")
                userScore += 1
            elif compChoice == "p":
                print("Computer chose paper. Computer gets a point.")
                compScore += 1
        case "p":
            if compChoice == "r":
                print("Computer chose rock. You get a point.")
                userScore += 1
            elif compChoice == "s":
                print("Computer chose scissors. Computer gets a point.")
                compScore += 1         
            elif compChoice == "p":
                print("Computer chose paper. No one gets a point.")
        case "s":
            if compChoice == "r":
                print("Computer chose rock. Computer gets a point.")
                compScore += 1 
            elif compChoice == "s":
                print("Computer chose scissors. No one gets a point.")         
            elif compChoice == "p":
                print("Computer chose paper. You get a point.")
                userScore += 1
        case "y":
            if compScore > userScore:
                print("Computer wins!\n")
            elif compScore < userScore:
                print("You win!\n")
            else:
                print("It's a draw!\n")
            break
        case _:
            print("Wrong choice.\n")
    print(f"Sores are: {userScore} - {compScore}\n")