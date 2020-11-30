import csv
#Comments are the same as 10.1B, I will note any changes

flights = []
solution = []
progress = []
connected = []
score = 0

def getData():
    global flights
    global progress
    x = 0
    with open('COMP363A10/Texas.txt') as tsv:
        for flight in csv.reader(tsv, dialect = "excel-tab"):
            if x == 0:
                x = 1
            else:
                temp = (flight[0], flight[1], int(flight[2])) #Reads # of flights instead of distance
                flights.append(temp)
                if [flight[0]] not in progress:
                    progress.append([flight[0]])
                if [flight[1]] not in progress:
                    progress.append([flight[1]])

def main():
    getData()
    kruskalPath()

def kruskalPath():
    global flights
    global solution
    global progress
    global connected
    global score
    while len(progress) > 1:
        tempMin = 0
        for flight in flights:
            if flight[2] > tempMin: #Looks for bigger numbers instead of smaller numbers
                if flight[0] not in connected:
                    tempMin = flight[2]
                    tempFlight = flight
                elif flight[1] not in connected:
                    tempMin = flight[2]
                    tempFlight = flight
                elif flight[0] in connected and flight[1] in connected:
                    for connection in progress:
                        if flight[0] in connection and flight[1] not in connection:
                            tempMin = flight[2]
                            tempFlight = flight
                        elif flight[0] not in connection and flight[1] in connection:
                            tempMin = flight[2]
                            tempFlight = flight
        flights.remove(tempFlight)
        solution.append((tempFlight[0], tempFlight[1]))
        score = score + tempFlight[2]
        if tempFlight[0] not in connected and tempFlight[1] not in connected:
            connected.append(tempFlight[0])
            connected.append(tempFlight[1])
            progress.remove([tempFlight[0]])
            progress.remove([tempFlight[1]])
            progress.append([tempFlight[0],tempFlight[1]])
        elif tempFlight[0] in connected and tempFlight[1] not in connected:
            connected.append(tempFlight[1])
            progress.remove([tempFlight[1]])
            for connection in progress:
                if tempFlight[0] in connection:
                    connection.append(tempFlight[1])
        elif tempFlight[0] not in connected and tempFlight[1] in connected:
            connected.append(tempFlight[0])
            progress.remove([tempFlight[0]])
            for connection in progress:
                if tempFlight[1] in connection:
                    connection.append(tempFlight[0])
        else:
            x = []
            y = []
            for connection in progress:
                if tempFlight[0] in connection:
                    x = connection
                elif tempFlight[1] in connection:
                    y = connection
            progress.remove(x)
            for item in x:
                y.append(item)
    print(solution)
    print(score)

main()
        

