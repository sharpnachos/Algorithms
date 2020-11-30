import csv

items = []
inTheKnapsack = []

#So this kind of doesn't work for a couple of reasons. I coded this to be in
#exact accordance with the way the question was phrased and I don't think the data
#is conducive to this question. All the highest value items are the smaller items
#so when I choose to replace the ladst item I added to the knapsack not only
#does it have a low weight, but I have already added all of the small items to
#the knapsack. I have a few ideas of how to alter the code so that it works better
#Instead of removing the last item you could remove the heaviest item and instead
#of requiring that it needs 2 items to replace the removed item you can just
#replace it with 1 item.

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
        #Checks if the item has already been put in the knapsack
        if item in inTheKnapsack:
            pass
        else:
            #
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
    print()
    print("BUT WAIT")
    print("We want more")
    print()
    #Identifies the last item put in the knapsack
    toRemove = inTheKnapsack[len(inTheKnapsack) - 1]
    lastitem(int(toRemove[2]))
    inTheKnapsack.remove(toRemove)
    for item in inTheKnapsack:
        print(item[0])
    pointValue()
    
def pointValue():
    total = 0
    for item in inTheKnapsack:
        total = total + int(item[2])
    print(total)

def lastitem(w):
    global inTheKnapsack
    global items
    #TRIES to find 2 items that are worth less than the weight of the last item put in the knapsack
    for item in items:
        if item in inTheKnapsack:
            pass
        else:
            if (w/2) - int(item[2]) >= 0:
                inTheKnapsack.append(item)
                w = w - int(item[2])
                
main("COMP363A9/Assignment9.csv", 3200)
