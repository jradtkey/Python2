from random import randint


def coinToss(arg):
    print "Starting the program..."
    heads = 0
    tails = 0
    for value in range(0, arg+1):
        toss = randint(0,1)
        if toss == 0:
            heads = heads + 1
            print "Attempt #" + str(value) + ": Throwing a coin...It's a head!...Got " + str(heads) + " head(s) so far and", tails, " tail(s) so far."
        elif toss == 1:
            tails = tails + 1
            print "Attempt #" + str(value) + ": Throwing a coin...It's a tail!...Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
    print "Program over."

coinToss(5000)
