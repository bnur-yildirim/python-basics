import random

def getNum():
    num = int(input("Enter a number(1-100): "))
    while num < 1 and num > 100:
        num = int(input("Number should be betwenn 1-100: ")) 
    return num

number = random.randint(1,100)

userNum = 0
score = 0
while userNum != number:
    userNum = getNum()
    score+=1

    if userNum > number:
        print("Too high.\n")
    elif userNum < number:
        print("Too low.\n")
    else:
        print("You Found the number!")
        print("Your score is: ", score) 