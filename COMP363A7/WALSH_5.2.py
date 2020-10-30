#Note: I wasn't sure if the start node had to be just 'A' or any node within the tree
#so for DFS and BFS I pick a random start node and for IDDFS I just pick 'A'
#Also, I was not sure if you wanted us to print out all the nodes we backtracked
#to in DFS so I did it just to be safe, if you did not want the nodes backtracked
#to be in the path then all it takes to fix is moving 1 line of code into an if
#statement

import random

#TODO: Add comments
#TODO: Remove the global variables

tree = [['b','c'], #A
        ['d','e'], #B
        ['f','g'], #C
        ['h','i'], #D
        ['j','k'], #E
        [], #F
        ['l'], #G
        [], #H
        ['m','n'], #I
        [], #J
        [], #K
        [], #L
        [], #M
        []] #N
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
path = []
nodesToVisit = []
x = 0
y = 0

def main():
    setUpDFS()
    setUpBFS()

def setUpDFS():
    global alpha
    global tree
    global nodesToVisit
    global path
    #nodesToVisit.clear()
    #path.clear()
    for index in range(0, len(tree)):
        nodesToVisit.append(alpha[index])
    currentNode = alpha[random.randint(0, (len(tree) - 1))]
    nodesToVisit.remove(currentNode)
    path.append(currentNode)
    traversalDFS(currentNode)

def traversalDFS(currentNode):
    global tree
    global alpha
    global nodesToVisit
    global path
    global x
    for node in tree[alpha.index(currentNode)]:
        if node in nodesToVisit:
            currentNode = node
            nodesToVisit.remove(node)
            path.append(node)
            traversalDFS(currentNode)
    if len(nodesToVisit) >= 1:
        for parent in tree:
            if currentNode in parent:
                currentNode = alpha[tree.index(parent)]
                path.append(currentNode)
                if currentNode in nodesToVisit:
                    nodesToVisit.remove(currentNode)
                traversalDFS(currentNode)
    elif len(nodesToVisit) == 0:
        x += 1
        if x == 8:
            print('DFS Path:')
            print(path)

def setUpBFS():
    global alpha
    global tree
    global nodesToVisit
    global path
    #nodesToVisit.clear()
    #path.clear()
    for index in range(0, (len(tree))):
        nodesToVisit.append(alpha[index])
    discovered = [alpha[random.randint(0, (len(tree) - 1))]]
    nodesToVisit.remove(discovered[0])
    path.append(discovered[0])
    traversalBFS(discovered)

def traversalBFS(discovered):
    global alpha
    global nodesToVisit
    global path
    global tree
    newDiscovered = []
    if len(nodesToVisit) != 0:
        for node in discovered:
            for child in tree[alpha.index(node)]:
                if child in nodesToVisit:
                    nodesToVisit.remove(child)
                    newDiscovered.append(child)
                    path.append(child)
            for parent in tree:
                if node in parent:
                    parentLetter = alpha[tree.index(parent)]
                    if parentLetter in nodesToVisit:
                        newDiscovered.append(parentLetter)
                        nodesToVisit.remove(parentLetter)
                        path.append(parentLetter)
                    break
        traversalBFS(newDiscovered)
    else:
        print('BFS Path:')
        print(path)

main()
