import csv

flights = [] #List of all flights with the start city, destination city, and distance
solution = [] #Compiled list of all edges in the spanning tree
toVisit = [] #Cities that have not been visited yet
visited = [] #Cities that have been visited
maxi = 0 #Variable to store the maximum distance of any flight
score = 0 #Counter to keep track of the spanning tree's total distance

def getData():
    global flights
    global toVisit
    global maxi
    x = 0 #Sets x equal to zero as a method of skipping the first row
    with open('COMP363A10/Texas.txt') as tsv: #Opens the file as a tab separated values file
        for flight in csv.reader(tsv, dialect = "excel-tab"): #Separates the values using tab, had an error with "delimiter = '/t'" but i found this work around
            if x == 0: #Skips first row
                x = 1
            else:
                temp = (flight[0], flight[1], int(flight[3])) #Takes only the data we need from the row and creates a tuple of that info
                flights.append(temp) #Adds tuple to flights
                if flight[0] not in toVisit: #Checks to see if the start city has not been added to toVisit
                    toVisit.append(flight[0])
                if flight[1] not in toVisit: #Checks to dee if the destination city has not been added to toVisit
                    toVisit.append(flight[1])
                if int(flight[3]) > maxi: #Checks to see if the distance for this flight is greater than our current max
                    maxi = int(flight[3])

def main():
    global toVisit
    global visited
    global maxi
    getData() #Retrieves data from the text file
    start = "HOUSTON" #Chooses Houston as the starting city
    toVisit.remove(start) #Removes Houston from toVisit
    visited.append(start) #Adds Houston to Visited
    maxi = maxi + 1 #Adds 1 to the maximum distance to identify a number larger than all distances
    primPath() 

def primPath():
    global flights
    global solution
    global toVisit
    global visited
    global maxi
    global score
    while len(toVisit) > 0: #This while loop breaks when all nodes have been visited
        tempMin = maxi #Sets tempMin to a number higher than any distance
        for flight in flights:
            if flight[0] in toVisit and flight[1] in visited: #Case 1: Start city has not been visited, destination city has
                if flight[2] < tempMin: #Checks to see if distance is smaller than current min
                    tempMin = flight[2] #Updates current min
                    tempFlight = flight #Saves flight info for later
            elif flight[1] in toVisit and flight[0] in visited: #Case 2: Destination city has not been visited but start city has
                if flight[2] < tempMin:
                    tempMin = flight[2]
                    tempFlight = flight
            else: #Case 3: Anything else
                pass
        solution.append((tempFlight[0], tempFlight[1])) #Adds edge to spanning tree
        score = score + tempFlight[2] #Updates total distance of spanning tree
        if tempFlight[0] in visited: #Case 1: Destination city has not been visited
            toVisit.remove(tempFlight[1]) 
            visited.append(tempFlight[1])
        else: #Case 2: Start city has not been visited
            toVisit.remove(tempFlight[0])
            visited.append(tempFlight[0])
    print(solution)
    print(score)

main()
