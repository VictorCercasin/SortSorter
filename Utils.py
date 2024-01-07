import numpy as np
import time
import configparser
import random

# read the config file
config = configparser.ConfigParser()
config.read("config.txt")
comparisonsPerSecond = float(config["BASICS"]["comparisonsPerSecond"])



def isBiggerNumber(a, b, info):
    info["Comparisons"] = info["Comparisons"] + 1
    time.sleep(1/comparisonsPerSecond)
    if a > b:
        return True
    return False

def isBiggerListIndex(list,a, b, info):
    info["Comparisons"] = info["Comparisons"] + 1
    info["Colors"][a] = 1
    info["Colors"][b] = 1
    time.sleep(1/comparisonsPerSecond)
    for i, item in enumerate( info['Colors']):
        if item == 1:
            info['Colors'][i] = 0
    if list[a] > list[b]:
        return True
    return False

def isEqualListIndex(list, a, b, info):
    info["Comparisons"] = info["Comparisons"] + 1
    time.sleep(1/comparisonsPerSecond)
    if list[a] == list[b]:
        return True
    return False

def isEqualNumber(a, b, info):
    info["Comparisons"] = info["Comparisons"] + 1
    time.sleep(1/comparisonsPerSecond)
    if a == b:
        return True
    return False

def swap(list, i, j, info):
    info["Swaps"] = info["Swaps"] + 1
    for k, item in enumerate( info['Colors']):
        if item == 2:
            info['Colors'][k] = 0
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    info['Colors'][i] = 2
    info['Colors'][j] = 2




#generate a random list of number
def makeList(listLength, listType):
    list = []
    for i in range(listLength):
        # list.append(np.random.randint(0, listLength * 10))
        list.append(i)
    if  listType == 'SHUFFLED':
        random.shuffle(list)
    return list