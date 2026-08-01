# Simple Subtraction Program

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

answer = a - b

print("The answer is:", answer)

if answer < 0:
    print("The answer is a negative number.")
else:
    print("The answer is a positive number.")
