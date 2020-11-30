#COMP 363 Assignment 7
#Thomas Walsh
#this is actual code
import random
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
startNode = ""
winningPath = []

#TODO: Add comments
#TODO: Thus begins the crutch of global variables

def main():
    graph = [['b','c'], #A
            ['a','c','d','g'], #B
            ['a','b','e','g'], #C
            ['b','e','f','g'], #D
            ['c','d','f','g'], #E
            ['d','e'], #F
            ['b','c','d','e']] #G
    setUp(graph)
    
def setUp(graph):
    global alpha
    global startNode
    global winningPath
    startNode = random.randint(0, len(graph) - 1)
    startNode = alpha[startNode]
    toDelete = []
    edgesRemaining = []
    x = 0
    for node in graph:
        nodeName = alpha[x]
        x += 1
        for connection in node:
            edge = nodeName + connection
            edgesRemaining.append(edge)
    for edge in edgesRemaining:
        node1 = alpha.index(edge[0])
        node2 = alpha.index(edge[1])
        if node1 > node2:
            toDelete.append(edge)
    for edge in toDelete:
        edgesRemaining.remove(edge)
    traversal(startNode, edgesRemaining)

def traversal(currentNode, edgesRemaining):
    global startNode
    global alpha
    global winningPath
    #Fixes the problem with node A!!!
    if len(winningPath) > 2:
        for index in range(1, len(winningPath) - 2):
            prev = winningPath[index - 1]
            current = winningPath[index]
            following = winningPath[index + 1]
            for node in prev:
                if node in current and node in following:
                    winningPath.remove(current)
                    edgesRemaining.append(current)
    for edge in edgesRemaining:
        if currentNode in edge:
            i = edge.index(currentNode)
            if i == 1:
                i2 = 0
            if i == 0:
                i2 = 1
            x = 0
            for edge2 in edgesRemaining:
                if edge[i2] in edge2:
                    x += 1
            if x > 1:
                currentNode = edge[i2]
                winningPath.append(edge)
                edgesRemaining.remove(edge)
                traversal(currentNode, edgesRemaining)
            elif x == 1:
                if len(edgesRemaining) == 1 and edge[i2] == startNode:
                    winningPath.append(edge)
                    path = ""
                    for edge in range(0,len(winningPath)):
                        if edge < len(winningPath)-1:
                            path = path + winningPath[edge] + " -> "
                        else:
                            path = path + winningPath[edge]
                    print("SOLVED! The winning path is edges: " + path)
main()
