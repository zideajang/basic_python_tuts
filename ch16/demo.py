# coding=utf-8
import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Probability of winning =',numWins/numTrials)

if __name__ == '__main__':
    checkPascal(10000)
    
