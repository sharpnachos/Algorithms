buildings = [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22], [23, 4, 28], [23, 13, 29]]
#This does not work 100%

def skyline(buildings):
    #No buildings
    if len(buildings) < 0:
        return []
    #1 building
    if len(buildings) < 2:
        return buildings
    #multiple buildings
    else:
        x = len(buildings) - 1
        #picks middle value to split the list in half
        pivot = x // 2
        #left side
        left = skyline(buildings[0 : pivot + 1])
        #right side
        right = skyline(buildings[pivot + 1 :])
        return mergesort(left, right)

def main():
    global buildings
    skylinelist = skyline(buildings)
    output = []
    #sets a new list to properly display the output
    for item in skylinelist:
        for num in item:
            output.append(num)
    maxI = 0
    #finds the max index of any building in the list
    for building in buildings:
        if building[2] > maxI:
            maxI = building[2]
    #Adds this value to the output along with a 0 to finish it off
    output.append(maxI)
    output.append(0)
    #print that shit
    print(output)

def mergesort(left, right):
    skyline = []
    #declares heights
    hl = 0
    hr = 0
    #keeps track of both sides
    leftcount = 0
    rightcount = 0
    while leftcount < len(left) and rightcount < len(right):
        #No overlap scenario
        #Bugged, it doesn't actually determine if there is no overlap
        #picks left element
        if left[leftcount][0] < right[rightcount][0]:
            temp = left[leftcount][0]
            hl = left[leftcount][1]
            #figures out which one is taller
            height = max(hl, hr)
            #record that
            skyline.append((temp, height))
            #increment our place
            leftcount += 1
        #picks right element
        elif left[leftcount][0] == right[rightcount][0]:
            hl = left[leftcount][1]
            hr = right[rightcount][1]
            #gets the start index
            temp = left[leftcount][0]
            #figures out which one is taller
            height = max(hl, hr)
            #record it in skyline
            skyline.append((temp, height))
            #updates our current position
            leftcount += 1
            rightcount += 1
        else:
            tempy = right[rightcount][0]
            hr = right[rightcount][1]
            #figures out which one is taller
            height = max(hl, hr)
            #record it in skyline
            skyline.append((tempy, height))
            #update our place
            rightcount += 1
    #merge left
    while leftcount < len(left):
        mergeleft = left[leftcount]
        mergeleft = mergeleft[:]
        skyline.append(mergeleft)
        leftcount += 1
    #merge right
    while rightcount < len(right):
        mergeright = right[rightcount]
        mergeright = mergeright[:]
        skyline.append(mergeright)
        rightcount += 1
    #sends back the result
    return skyline

main()
