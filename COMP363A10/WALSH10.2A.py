import csv
#Comments are going to be the same as 10.1A, I will comment about any difference

#TODO: Doesn't work

flights = [] 
solution = [] 
toVisit = [] 
visited = [] 
score = 0 

def getData():
    global flights
    global toVisit
    global maxi
    x = 0 
    with open('Texas.txt') as tsv:
        for flight in csv.reader(tsv, dialect = "excel-tab"):
            if x == 0:
                x = 1
            else:
                temp = (flight[0], flight[1], int(flight[2])) #Reads number of flights instead of distance
                flights.append(temp)
                if flight[0] not in toVisit: 
                    toVisit.append(flight[0])
                if flight[1] not in toVisit: 
                    toVisit.append(flight[1])

def main():
    global toVisit
    global visited
    getData()
    start = "HOUSTON" 
    toVisit.remove(start)
    visited.append(start)
    primPath()

def primPath():
    global flights
    global solution
    global toVisit
    global visited
    global score
    while len(toVisit) > 0: 
        tempMax = 0 
        for flight in flights: 
            if flight[0] in toVisit and flight[1] in visited:
                if flight[2] > tempMax: #Finds bigger numbers instead of smaller numbers
                    tempMax = flight[2]
                    tempFlight = flight
            elif flight[1] in toVisit and flight[0] in visited:
                if flight[2] > tempMax: #^^^
                    tempMax = flight[2]
                    tempFlight = flight
            else:
                pass
        score = score + tempFlight[2]
        solution.append((tempFlight[0], tempFlight[1]))
        if tempFlight[0] in visited:
            toVisit.remove(tempFlight[1])
            visited.append(tempFlight[1])
        else:
            toVisit.remove(tempFlight[0])
            visited.append(tempFlight[0])
    print(solution)
    print(score)

main()

