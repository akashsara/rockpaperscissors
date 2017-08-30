import random

'''
Inside the game file, do:
choiceU, choiceS = inputoutput.inpoot()
Replace all inputoutput.choiceU with choiceU and inputoutput.choiceS with choiceS
use increase_user() or increase_sys() to increment scores
pls2check and see if it actually works as intended xD
'''

def increase_user():
    user += 1
    
def increase_sys():
    sys += 1

def return_scores():
    return user, sys

def inpoot() :
    TheList = [1,2,3]
    choiceU=input("\t\tCHOICE : ")
    choiceS=random.choice(TheList)
    return choiceU, choiceS

user = 0
sys = 0
