import pygame
import math
import configparser
import importlib.util
import threading
from sys import exit

from Renderer import AlgDrawerRanderer
from Utils import makeList
import Utils

# read the config file
config = configparser.ConfigParser()
config.read("config.txt")
width = int(config["BASICS"]["width"])
height = int(config["BASICS"]["height"])
listLength = int(config["BASICS"]["listLength"])
listType = config["BASICS"]["listType"].upper()
algsList = [item.strip() for item in config["ALGORITHMS"]["algorithmsList"].split(",")]


# initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sort Sorter")
clock = pygame.time.Clock()

# generate the list for sorting
list = makeList(listLength, listType)


# replicate the list for each algorithm to sort
listOfLists = [list.copy() for i in range(len(algsList))]

#creates a list with information for the renderer for each algorithm
listOfInfo = [{"Colors": [0] * listLength, "Comparisons": 0, "Swaps" : 0} for _ in range(len(algsList))]


# creates a list of threads
threads = []

# spools up threads for each algorithm and runs them
for i, alg in enumerate(algsList):
    file_name = f"Algorithms/{alg}.py"

    spec = importlib.util.spec_from_file_location(alg, file_name)

    # creates a new module based on spec
    foo = importlib.util.module_from_spec(spec)

    # executes the module in its own namespace
    # when a module is imported or reloaded.
    spec.loader.exec_module(foo)

    threads.append(threading.Thread(target=foo.func, args=(listOfLists[i], listOfInfo[i])))

    #set thread as daemon (will be killed when main thread exits)
    threads[i].daemon = True
    # Start the thread
    threads[i].start()

#define space of each algorithm to render in
algHeigh = height / len(listOfLists)

#Renderer loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    screen.fill((0, 0, 0))
    for i, alg in enumerate(listOfLists):
        AlgDrawerRanderer(pygame, screen, listOfLists[i], (0, algHeigh * i, width, algHeigh), listOfInfo[i], algsList[i])
    pygame.display.update()
    clock.tick(60)


# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Done")
