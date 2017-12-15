# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:03:42 2017

@author: kygwi_000
"""

from random import randint



def advantage_disadvantage(rolls):
    counter = 0
    for i in range(int(rolls)):
        roll_advantage = [0,0]
        roll_advantage[0] += randint(1,20)
        roll_advantage[1] += randint(1,20)
        roll_advantage.sort()
        counter += roll_advantage[1]
    
    return (counter / int(rolls))

rolls = input("How many times would you like to roll?: ")

print("Effective difference is +" + (str(advantage_disadvantage(rolls) - 10.5)))
    

