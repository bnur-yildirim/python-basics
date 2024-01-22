import random

#constant variables
MIN_NUM = 1
MAX_NUM = 100

#input a number from the user
def get_num():
    while True:
        num = int(input(f"Enter a number ({MIN_NUM}-{MAX_NUM}): ")) 
        if MIN_NUM <= num and MAX_NUM >= num:
            return num
        else:
            print(f"Number should be between {MIN_NUM}-{MAX_NUM}.")

print(f"""Welcome to the guessing number game.
You will try to guess a random number between{MIN_NUM} and {MAX_NUM}.
The program will keep track of the number of tries you make and display it as score.
Good luck!!\n""")

number = random.randint(MIN_NUM, MAX_NUM)
userNum = get_num()
score = 1

while userNum != number:
    if userNum > number:
        print("Too high.\n")
    elif userNum < number:
        print("Too low.\n")
    userNum = get_num()
    score+=1

print(f"You found the number!\nYour score is {score}\n")