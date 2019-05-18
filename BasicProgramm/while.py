
import random

def read(highest,answer):
    print("Please Enter Number between {} to {}".format(1,highest))
    try:
        guess = int(input())
        if guess != answer:
            if(guess < answer):
                print("please Guess Higher")
                read(highest,answer)
            else:
                print("please Guess lower")
                read(highest,answer)
        else:
          print("Game Over")
    except:
        print("please Enter vaild Input")

highest = 10
answer  = random.randint(1,highest)
read(highest,answer)




