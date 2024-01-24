# Program to calculate simple interest

print("This program will calculate simple interest.")

principal = int(input("Enter principal amount: "))
time = int(input("Enter time in units: "))
rate = int(input("Enter rate: "))

interest = (principal*time*rate)/100

print("Simple interest is : ",interest)
