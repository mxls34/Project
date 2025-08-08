# Example Program : 5
# *****************************
import random
num = 0
num_inp = 0
done = True
print("Program : Number Guessing Game ( 1- 99)")
print("===========================")
num = random.randint(1,99)
while done:
    num_inp = int(input("Enter guess number(1-99) : "))
    if (num_inp == num):
        done = False
    elif (num_inp < num):
        print( num_inp , " is less than")
    else:
        print( num_inp , " is grater than")

print("\nCorrect, number is %d" % num)
