import csv

items = []
inTheKnapsack = []
tempP = 0
total = 0
final = []

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
    global tempP
    global total
    for item in items:
        #Passes over any item already in the knapsack
        if item in inTheKnapsack:
            pass
        else:
            #The whole item fits in the knapsack
            if w - int(item[2]) >= 0:
                inTheKnapsack.append(item)
                w = w - int(item[2])
                total = total + int(item[2])
            elif w > 0:
                #only part of the item fits in the knapsack
                temp = w - int(item[2])
                tempy = int(item[2]) + temp
                tempP = 100 * float(tempy / int(item[2]))
                inTheKnapsack.append(item)
                w = w - (tempy)
                total = total + (int(item[2]) * (tempP/100))
                break

def main(name):
    global inTheKnapsack
    global tempP
    global total
    readcsv(name)
    w = 3200
    knapsack(w/2)
    print(total)
    x = total
    for item in inTheKnapsack:
        print(item[0])
        final.append(item[0])
    print("^^^Only " + str(tempP) + "% of this item")
    inTheKnapsack.clear()
    total = 0
    knapsack(w/2)
    print(total)
    for item in inTheKnapsack:
        print(item[0])
    print("^^^Only " + str(tempP) + "% of this item")
    print("Total weight is equal to " + str(x + total))
    
main("COMP363A9/Assignment9.csv")
        
