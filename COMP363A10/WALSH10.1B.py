import csv

#TODO: Doesn't work

flights = [] #List of all flight information
solution = [] #List of edges of the spanning tree
progress = [] #List of all clusters of connected nodes - starts with a list of one for each city and as connections are made the lists inside the list get bigger
connected = [] #List of all nodes that have been connected thus far
maxi = 0 #Max distance of any flight
score = 0 #Keeps track of the total distance of the spanning tree

def getData():
    global flights
    global progress
    global maxi
    x = 0 #Method of skipping the first row
    with open('Texas.txt') as tsv:
        for flight in csv.reader(tsv, dialect = "excel-tab"):
            if x == 0: #Skips first row
                x = 1
            else:
                temp = (flight[0], flight[1], int(flight[3])) #Creates a tuple with all necessary information
                flights.append(temp) #Adds this tuple to flights
                if [flight[0]] not in progress: #If start city is not in progress it is added to progress as a list of one
                    progress.append([flight[0]])
                if [flight[1]] not in progress: #If destination city is not in progress it is added to progress as a list of one
                    progress.append([flight[1]])
                if int(flight[3]) > maxi: #Finds the maximum distance of all flights
                    maxi = int(flight[3])

def main():
    global maxi
    getData() #Retrieves data from the text file
    maxi = maxi + 1 #Sets maxi to a number above the maximum flight distance
    kruskalPath()

def kruskalPath():
    global flights
    global solution
    global progress
    global connected
    global maxi
    global score
    while len(progress) > 1: #While loop that breaks when all nodes are connected to each other
        tempMax = maxi #Sets this variable to a number higher than the max distance
        for flight in flights:
            if flight[2] < tempMax: #If the distance is less than our current min
                if flight[0] not in connected: #Case 1: Start city is not in connected
                    tempMax = flight[2] #Updates current min
                    tempFlight = flight #Saves fligth data for potential future use
                elif flight[1] not in connected: #Case 2: Destination city is not in connected
                    tempMax = flight[2]
                    tempFlight = flight
                elif flight[0] in connected and flight[1] in connected: #Case 3: Both cities are in connected but are not connected to each other
                    for connection in progress: #Checks to make sure the cities are not connected to each other
                        if flight[0] in connection and flight[1] not in connection:
                            tempMax = flight[2]
                            tempFlight = flight
                        elif flight[0] not in connection and flight[1] in connection:
                            tempMax = flight[2]
                            tempFlight = flight
        flights.remove(tempFlight) #Removes the shortest flight from flights so it cannot be picked again
        solution.append((tempFlight[0], tempFlight[1])) #Adds the edge to the spanning tree
        score = score + tempFlight[2] #Updates total distance of the spanning tree
        if tempFlight[0] not in connected and tempFlight[1] not in connected: #Case 1: Both cities are not in connected
            connected.append(tempFlight[0]) #Adds city to connected
            connected.append(tempFlight[1])
            progress.remove([tempFlight[0]]) #Removes list of one from progress
            progress.remove([tempFlight[1]])
            progress.append([tempFlight[0],tempFlight[1]]) #Adds list of both cities to progress
        elif tempFlight[0] in connected and tempFlight[1] not in connected: #Case 2: Start city is connected but destination city is not
            connected.append(tempFlight[1]) 
            progress.remove([tempFlight[1]])
            for connection in progress: #Checks all lists in progress and finds the one that has the start city in it
                if tempFlight[0] in connection:
                    connection.append(tempFlight[1]) #Adds destination city to that list
        elif tempFlight[0] not in connected and tempFlight[1] in connected: #Case 3: Destination city is in connected but the start city is not
            connected.append(tempFlight[0])
            progress.remove([tempFlight[0]])
            for connection in progress:
                if tempFlight[1] in connection:
                    connection.append(tempFlight[0])
        else: #Case 4: Both cities are in connected but are not connected to each other
            x = [] #Sets empty list for start city
            y = [] #Sets empty list for destination city
            for connection in progress:
                if tempFlight[0] in connection: #Finds list with start city
                    x = connection
                elif tempFlight[1] in connection: #finds list with destination city
                    y = connection
            progress.remove(x) #Removes list with start city
            for item in x: #Adds all cities in start city's list to destination city's list
                y.append(item)
    print(solution)
    print(score)

main()
        
