#COMP 363 Assignment 11
#Thomas Walsh

targetWord = ''
givenWord = ''
targetIndex = 0
givenIndex = 0
solution = []

def dynamic():
    global targetWord
    global givenWord
    global targetIndex
    global givenIndex
    global solution
    #Sets up the solution list of lists
    for x in range(targetIndex + 1):
        #Makes the right number of lists
        tempy = []
        for y in range(givenIndex + 1):
            #Adds the right number of zeros
            tempy.append(0)
        solution.append(tempy)
    #Checks each letter in target word
    for targetNum in range(targetIndex + 1):
        #Checks every letter in given word
        for givenNum in range(givenIndex + 1):
            #given word is empty
            if givenNum == 0:
                solution[targetNum][givenNum] = targetNum
            #target word is empty
            elif targetNum == 0:
                solution[targetNum][givenNum] = givenNum
            #letters match
            elif targetWord[targetNum - 1] == givenWord[givenNum - 1]:
                solution[targetNum][givenNum] = solution[targetNum - 1][givenNum - 1]
            #letters don't match
            else:
                #Checks to see whats easiest replacement, insertion, or removal
                solution[targetNum][givenNum] = 1 + min(solution[targetNum - 1][givenNum - 1], solution[targetNum][givenNum - 1], solution[targetNum - 1][givenNum])
    
def main():
    global targetWord
    global givenWord
    global targetIndex
    global givenIndex
    global solution
    targetWord = 'loyola'
    givenWord = 'crayola'
    targetIndex = len(targetWord)
    givenIndex = len(givenWord)
    dynamic()
    print(solution[targetIndex][givenIndex])

main()
