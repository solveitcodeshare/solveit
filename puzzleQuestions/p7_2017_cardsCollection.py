#problem 7, cooperative card collection

#work out a sequence of cards where no card rank repeats
#test with random sets of cards
import random

def getSequences(hands):
    hands = [list(set(x)) for x in hands]
    #print(hands)
    sequences = [[x] for x in hands[0]]
    #print(sequences)
    for i in range(len(hands))[1:]:
        chand = hands[i]
        #print(chand)
        newSequences = []
        for c in chand:
            for x in sequences:
                if c not in x:
                    newSequences.append(x+[c])
        sequences = newSequences
    return sequences

#print(deck)
def getMaxCard(hands):

    if len(hands)==1:
        print("at bottom, return ",max(hands[0]), "from ",hands[0])
        return [max(hands[0])]
    else:
        subchoice = getMaxCard(hands[1:])
        print("hands ",hands)
        print(" subchoice ",subchoice)
        print("set(subchoice) ",set(subchoice))
        print("set(hands)-set(subchoice) ",set(hands[0])-set(subchoice))
        newchoice = [max(set(hands[0])-set(subchoice))]
        print("newchoice ",newchoice)
        print("newchoice + subchoice ",newchoice + subchoice)
        return newchoice + subchoice

suit = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suitranks = [x for x in range(13)]
#print(suitranks)

deck = []

for i in range(4):
    for c in suitranks:
        deck.append(c)

random.shuffle(deck)

#assign deck to 13 players

players = [[0,0,0,0] for _ in range(13)]
for i,c in enumerate(deck):
    players[i%13][i%4] = c

chosen = []

# for i in range(13):
#     remaining = set(players[i])-set(chosen)
#     if len(remaining) == 0:
#         print("Can't choose anything")
#         print(players)
#         print("current player ",i," chosen= ",chosen," player has ",players[i])
#     choice = max(set(players[i])-set(chosen))
#
#     print(choice)
#     chosen.append(choice)

    #chosen.append(choice)
#chosen = getMaxCard(players)
sequences = getSequences(players)
#need to return only one sequence based on the highest cards
print(len(sequences))
numSequences = len(sequences)
i = 0
while numSequences > 1:
    numSequences = len(sequences)
    maxNum = max([x[i] for x in sequences])
    #print(maxNum)
    sequences = [x for x in sequences if x[i] == maxNum]
    i+=1

result = [suit[x] for x in sequences[0]]
for r in result:
    print(r,end=" ")
