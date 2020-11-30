import csv

items = []
inTheKnapsack = []
tempP = 0
total = 0

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
        #Passes any item we have already packed
        if item in inTheKnapsack:
            pass
        else:
            #If the whole item fits
            if w - int(item[2]) >= 0:
                inTheKnapsack.append(item)
                w = w - int(item[2])
                total = total + int(item[2])
            #If the item does not fit
            elif w > 0:
                temp = w - int(item[2])
                tempy = int(item[2]) + temp
                tempP = 100 * float(tempy / int(item[2]))
                inTheKnapsack.append(item)
                w = w - (tempy)
                total = total + (int(item[2]) * (tempP/100))
                break
def main(name, w):
    global inTheKnapsack
    global total
    readcsv(name)
    knapsack(w)
    print(total)
    for item in inTheKnapsack:
        print(item[0])
    print("^^^Only " + str(tempP) + "% of this item")
    
main("COMP363A9/Assignment9.csv", 3200)
        
