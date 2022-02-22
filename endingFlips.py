import random

# main combo is at [0]
Combos = [[0,1,0],[1,1,0]]
timesEnded = [0]*len(Combos)


def hasEndedSingle(ending_combo, flips_list):
    if list(reversed(flips_list))[:len(ending_combo)] == list(reversed(ending_combo)):
        return True
    return False


def hasEnded(ending_combos, flips_list):
    for combo in ending_combos:
        if hasEndedSingle(combo, flips_list):
            return [True, Combos.index(combo)]
    return [False]


def flips(ending_combos):
    flipsList = []
    ended = [False]
    while not ended[0]:
        flipsList.append(random.randint(0, 1))
        ended = hasEnded(ending_combos, flipsList)
    timesEnded[ended[1]] += 1
    # print(flipsList, ', ', Combos[ended[1]])


for i in range(pow(10,7)):
    flips(Combos)
# print(hasEndedSingle([0,1],[1,1,1,0,0,1]))
print(timesEnded)
chanceOfMain = timesEnded[0]/sum(timesEnded)
print(chanceOfMain)
