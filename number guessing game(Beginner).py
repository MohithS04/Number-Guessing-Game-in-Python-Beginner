import random
import math

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

# generating random numbers between the lower and upper
v = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, "chances to guess the integer!\n")

# Initializing the number of guesses

count = 0
flag = False

# for calculation of minimum number of guesses depends upon range

while count < total_chances:
    count += 1

    # Taking guessing number as input
    guess_number = int(input("Guess a number:- "))

    # condition testing
    if v == guess_number:
        print("Congratulations you did it in", 
              count, "try")
        # once guessed, loop will break
        flag = True
        break
    elif v > guess_number:
        print("You guessed too samll")
    elif v < guess_number:
        print("You guessed too high!")

# If guessing is more than required guesses,
# shows this output.
if not flag:
    print("\nThe number is %d" % v)
    print("\tBetter Luck Next time!")

