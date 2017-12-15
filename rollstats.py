from random import randint

def roll_stats():
    """
    Returns a list of 6 stats from highest to lowest
    These stats are built by rolling 4d6, dropping the lowest
    Then addings the remaining 3 together
    """
    returnValues = []
    for j in range(6):
        rollList = []
        for i in range(4):
            rollList.append(randint(1,6))
        rollList.sort()
        del rollList[0]
        returnValues.append(sum(rollList))
    returnValues.sort(reverse=True)
    return returnValues