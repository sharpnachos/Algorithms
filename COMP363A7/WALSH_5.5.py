import random

#TODO: Add comments
#TODO: Remove the global variables

airports = ['ORD','JFK','ATL','MIA','IAH','LAX','SEA','DEN']
citiesToVisit = []
usaGraph = [['JFK','IAH'], #ORD
            ['ATL','ORD'], #JFK
            ['JFK','DEN','MIA','IAH'], #ATL
            ['ATL'], #MIA
            ['ATL','ORD','LAX'], #IAH
            ['SEA','DEN','IAH'], #LAX
            ['IAH','DEN'], #SEA
            ['SEA','LAX','ATL']] #DEN
x = 0
targetCity = ''
solved = False

def main():
    setUpBFS()

def setUpBFS():
    global airports
    global usaGraph
    global citiesToVisit
    global targetCity
    #citiesToVisit.clear()
    discovered = ['ORD']
    targetCity = airports[random.randint(1,len(usaGraph) - 1)]
    for city in airports:
        citiesToVisit.append(city)
    print('Target City is ' + targetCity)
    traversalBFS(discovered)

def traversalBFS(discovered):
    global airports
    global citiesToVisit
    global usaGraph
    global targetCity
    global x
    global solved
    x += 1
    newDiscovered = []
    if len(citiesToVisit) != 0 and solved == False:
        for node in discovered:
            for connection in usaGraph[airports.index(node)]:
                if connection in citiesToVisit:
                    citiesToVisit.remove(connection)
                    newDiscovered.append(connection)
        if targetCity in newDiscovered:
            solved = True
            if x == 1:
                pluralCheck = 'flight'
            else:
                pluralCheck = 'flights'
            print(targetCity + ' is ' + str(x) + ' ' + pluralCheck + ' away from ORD')
        traversalBFS(newDiscovered)
    
main()
