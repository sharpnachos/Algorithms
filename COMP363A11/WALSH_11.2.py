steps = 1632 #Steps in Hancock
bigStep = 2 #Biggest step we can take
solution = []

#TODO: Pretty sure this is horribly incorrect

def countThemStepsBoi():
    global steps
    global bigStep
    global solution
    steps += 1
    x = 0
    #Fill up solutions list
    for step in range(steps):
        #First 2 only have 1 possibility 1 or 2
        if x == 0:
            solution.append(1)
            x += 1
        elif x == 1:
            solution.append(1)
            x += 1
        else:
            solution.append(0)
    #Checks all the possibilities in the range of steps
    for temp in range(x, steps):
        tempy = 1
        while tempy < bigStep + 1: #Breaks when tempy is bigger than 2
            tempi = solution[temp] + solution[temp - tempy] 
            solution[temp] = tempi
            tempy += 1

def main():
    global solution
    global steps
    countThemStepsBoi()
    steps = steps - 1
    print(solution[steps])

main()
