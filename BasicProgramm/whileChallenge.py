import random

def read(highest,answer):
    print("Please Enter Number between {} to {}".format(1,highest))
    try:
        guess = 0
        while guess != answer:
            guess = int(input())
            if guess < answer:
                print("please Guess Higher")
            elif guess > answer :
                print("please Guess lower")
            else:
               print("Game Over You Won")
    except:
        print("please Enter vaild Input")

highest = 10
answer  = random.randint(1,highest)
read(highest,answer)
