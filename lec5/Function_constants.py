import random

HEAD = 1
TAITLS = 2
TOSSES = 10

def tosses_coin():
    for toss in range(TOSSES):

        if random.randint(HEAD,TAITLS)==HEAD :
            print("HEADs")
        else:
            print("TAITLS")

tosses_coin()