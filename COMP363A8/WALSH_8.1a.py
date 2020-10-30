#Buildings need to be sorted from left to right for this to work, if they have the same start index then the one with the lower height is placed first
buildings = [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22], [23, 4, 28], [23, 13, 29]]

def skyline():
    global buildings
    #set empty list for output
    skyline = []
    #set empty list for heights at each index
    heights = []
    #set empty variable for max index
    lastIndex = 0
    #finds max index
    for building in buildings:
        if building[2] > lastIndex:
            lastIndex = building[2]
    #add a 0 as a height for every index in the range of 0 to the max index
    for i in range(0, lastIndex):
        heights.append(0)
    #goes through every index of each building and sets the value of heights at that index equals to the height of the current building if that is bigger
    for building in buildings:
        for index in range(building[0], building[2]):
            if building[1] > heights[index]:
                heights[index] = building[1]
    #Identifies each time the height changes and adds the index followed by the new height to the output
    for index in range(0, len(heights) - 1):
        if heights[index] != heights[index + 1]:
            skyline.append(index + 1)
            skyline.append(heights[index + 1])
    #add in the last index and the height of 0 to finish off the output
    skyline.append(lastIndex)
    skyline.append(0)
    #print that shit
    print(skyline)
    
def main():
    skyline()

main()
