#COMP 363 Assignment 8
#Thomas Walsh

tree = {'a':['b','c'], 'b':['d','e'], 'c':['f','g'], 'd':['',''], 'e':['',''],'f':['',''], 'g':['h',''], 'g':['','']}

def deleteNode(n):
    global tree
    connections = tree[n]
    #Identifies left and right child
    left = connections[0]
    right = connections[1]
    #If node has no children
    if left == '' and right == '':
        #Goes through each child of each node and switches any occurence of the node to delete to a blank
        for node in tree:
            connectedNodes = tree[node]
            index = 0
            for connectedNode in connectedNodes:
                if connectedNode == n:
                    connectedNodes[index] = ''
                index +=1
        del tree[n]
        print(tree)
    #If node has 2 children
    elif left != '' and right != '':
        #Goes to the right child
        subtree = tree[n]
        connections = tree[subtree[1]]
        #Finds the leftmost child in the subtree
        temp = connections[0]
        node = subtree[1]
        while temp != '':
            node = temp
            connections = tree[temp]
            temp = connections[0]
        mini = node
        #Finding all occurences of node to delete and switching it out with that minimum we just found
        for node in tree:
            connectedNodes = tree[node]
            index = 0
            for connectedNode in connectedNodes:
                if connectedNode == n:
                    connectedNodes[index] = mini
                index += 1
        #recursively call deleteNode to delete the mini value
        deleteNode(mini)
        #I already used temp dont judge me
        tempy = tree[n]
        del tree[n]
        #adds a new element with the children of the deleted node and the key of the minimum
        tree[mini] = tempy
        print(tree)
    #If node has one child
    else:
        #Sets the saved value equals to the correct child (not the blank one)
        if left == '':
            saved = right
        else:
            saved = left
        #Finds all occurences of node to delete and switches it with the aforementioned child
        for node in tree:
            connectedNodes = tree[node]
            index = 0
            for connectedNode in connectedNodes:
                if connectedNode == n:
                    connectedNodes[index] = saved
                index += 1
        del tree[n]
        print(tree)
    
def main():
    deleteNode("d")
    deleteNode("b")
    deleteNode("a")
    
main()
