#COMP 363 Assignment 7
#Thomas Walsh

import random

#TODO: Add comments
#TODO: Remove the global variables

alpha = 'abcdefghijklmnopqrstuvwxyz'
nodesToVisit = []
graph = [['b','c'], #A
                ['a','c','d','g'], #B
                ['a','b','e','g'], #C
                ['b','e','f','g'], #D
                ['c','d','f','g'], #E
                ['d','e'], #F
                ['b','c','d','e']] #G
x = 0

def main():
    setUpBFS()

def setUpBFS():
    global alpha
    global graph
    global nodesToVisit
    for index in range(0, (len(graph))):
        nodesToVisit.append(alpha[index])
    discovered = [alpha[random.randint(0, (len(graph) - 1))]]
    nodesToVisit.remove(discovered[0])
    print("Start node is: " + discovered[0])
    traversalBFS(discovered)

def traversalBFS(discovered):
    global alpha
    global nodesToVisit
    global graph
    global x
    x += 1
    newDiscovered = []
    if len(nodesToVisit) != 0:
        for node in discovered:
            for connection in graph[alpha.index(node)]:
                if connection in nodesToVisit:
                    nodesToVisit.remove(connection)
                    newDiscovered.append(connection)
                    if x == 1:
                        pluralCheck = 'node'
                    else:
                        pluralCheck = 'nodes'
                    print("Node " + connection + " is " + str(x) + " " + pluralCheck + " away from the start node")
        traversalBFS(newDiscovered)
    
main()
