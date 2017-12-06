from random import randint

def roll_stats():
    returnValues = []
    for j in range(6):
        rollList = []
        for i in range(4):
            rollList.append(randint(1,6))
        rollList.sort()
        del rollList[0]
        returnValues.append(sum(rollList))        
    return returnValues