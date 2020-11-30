import csv

items = []
inTheKnapsack = []

#TODO: This doesn't work

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
        #Passes by any item already added to the knapsack
        if item in inTheKnapsack:
            pass
        else:
            #If the entire item can fit
            if w - int(item[2]) >= 0:
                inTheKnapsack.append(item)
                w = w - int(item[2])

def main(name, w):
    global inTheKnapsack
    readcsv(name)
    knapsack(w)
    pointValue()
    for item in inTheKnapsack:
        print(item[0])

def pointValue():
    total = 0
    for item in inTheKnapsack:
        total = total + int(item[2])
    print(total)
    
main("Assignment9.csv", 3200)
        
