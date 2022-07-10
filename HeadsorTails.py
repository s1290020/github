print("Who are you?")
name = input()
print("Hello,"+name+'!') 


import random

heads = 0
tails = 0
total = 0
print("Tossing a coin...")

while total < 3:
    total += 1
    randomInt = random.randint(0, 1)

    if randomInt == 1:
        print("Round %d: Heads" % total)
        heads += 1
    else:
        print("Round %d: Tails" % total)
        tails += 1

print("Heads: %d, Tails: %d" % (heads,tails))

if heads > tails:
    print(name+" won!")
else :
    print(name+" lost!")

