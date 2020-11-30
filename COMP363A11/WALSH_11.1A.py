#COMP 363 Assignment 11
#Thomas Walsh

targetWord = ''
givenWord = ''

def memo(targetIndex, givenIndex):
    global targetWord
    global givenWord
    editDistance = 0
    #targetWord is empty, edit distance is insertion * length of given
    if targetIndex == 0:
         editDistance = givenIndex
         return editDistance
    #givenWord is empty, same as above but flipped
    if givenIndex == 0:
        editDistance = targetIndex
        return editDistance
    #Moves down the words
    targetIndex = targetIndex - 1
    givenIndex = givenIndex - 1
    #Letters match -- skip
    if targetWord[targetIndex] == givenWord[givenIndex]:
        return memo(targetIndex, givenIndex)
    #Determines whether the best thing is to replacement (case 1), insertion (case 2), or removal (case 3) is the easiest to do
    return min(memo(targetIndex, givenIndex), memo(targetIndex + 1, givenIndex), memo(targetIndex, givenIndex + 1)) + 1
    
  
def main():
    global targetWord
    global givenWord
    targetWord = 'loyola'
    givenWord = 'crayola'
    targetIndex = len(targetWord)
    givenIndex = len(givenWord)
    print(memo(targetIndex, givenIndex))

main()
