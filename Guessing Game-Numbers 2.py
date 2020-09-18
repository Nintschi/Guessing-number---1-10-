import random

highest = 10
answer = random.randint(1,highest)
#print(answer) # todo: remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        print("goodbye...")
        break
    if guess > answer:
        print("...guess a lower number")
    if guess < answer:
        print("...guess a higher number")

    guess = int(input())

while guess == answer:
    print ("perfect, well done, you got it right")
    break