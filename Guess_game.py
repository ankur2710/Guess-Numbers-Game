import random
random.randint(1, 100)
jackpot = random.randint(1, 100)
guess= int(input("Chal guess kar "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input("Guess The Number Between 1-100  "))
    counter += 1
print("Correct Answer ")
print("you took", counter, "attempts")
