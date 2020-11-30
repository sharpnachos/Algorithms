#COMP 363 Assignment 3
#Thomas Walsh
# A Humble Implementation of Insertion Sort

# Time Complexity Best Case: O(1) - occurs when list is already sorted
# Time Complexity Average/Worst Case: O(n^2) - worst case occurs when list is in descending order

from random import randint
import time

def insertionSort(nums):
    #loops through all numbers in the list
    for num in range(1, len(nums)):
        #saves the current node and the previous node, starts at the second node in the list
        current = nums[num]
        previous = num - 1
        #Compare current to previous. If previous is bigger than current swap them
        while previous >= 0 and current < nums[previous]:
            nums[previous + 1] = nums[previous]
            previous = previous - 1
        nums[previous + 1] = current
    return nums

def main():
    length = randint(0,50)
    nums = []
    for place in range(0,length):
        temp = randint(0,200)
        nums.append(temp)
    start = time.time()
    response = insertionSort(nums)
    end = time.time()
    print("Successfully sorted! The program ran in " + str(end-start) + " seconds.")
    #print(response)
    

main()