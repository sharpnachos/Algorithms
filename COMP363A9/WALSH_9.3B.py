import csv

items = []
inTheKnapsack = []

def readcsv(name):
    global items
    #Gets the info from the csv
    with open(name) as csvfile:
        data = csv.reader(csvfile, delimiter = ',')
        x = 1
        for row in data:
            y = 0
            if x == 1:
                x = 0
            else:
                items.append(row)
    #Deletes any item worth 0 or negative points
    toDelete = []
    for item in items:
        if int(item[1]) <= 0:
            toDelete.append(item)
    for item in toDelete:
        items.remove(item)
    #Calculates the weight to points ratio
    for item in items:
        bang4buck = int(item[1]) / int(item[2])
        item.append(bang4buck)
    #Sorts them in order of points per weight
    newitems = []
    while len(newitems) < len(items):
        maximum = 0
        maxI = 0
        for item in items:
            if item[3] > maximum:
                maximum = item[3]
                maxI = items.index(item)
        newitems.append(items[maxI])
        items.remove(items[maxI])
    items.clear()
    for item in newitems:
        items.append(item)
    
def knapsack(w):
    global inTheKnapsack
    global items
    for item in items:
        #Passes over items that have already been added to the knapsack
        if item in inTheKnapsack:
            pass
        else:
            #The whole item fits in the knapsack
            if w - int(item[2]) >= 0:
                inTheKnapsack.append(item)
                w = w - int(item[2])

def main(name, w):
    global inTheKnapsack
    readcsv(name)
    knapsack(w/2)
    for item in inTheKnapsack:
        print(item[0])
    pointValue()
    knapsack(w/2)
    pointValue()
    for item in inTheKnapsack:
        print(item[0])

def pointValue():
    global inTheKnapsack
    total = 0
    weight = 0
    for item in inTheKnapsack:
        weight = weight + int(item[2])
        total = total + int(item[1])
    print("total weight is " + str(weight))
    
main("Assignment9.csv", 3200)
        
