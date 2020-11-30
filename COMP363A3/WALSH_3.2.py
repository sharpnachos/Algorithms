from random import randint
import time

#Bubble Sort

#Time Complexity Best Case: O(n) - Occurs when list is already sorted
#Time Complexity Worst Case: O(n^2) - 

def bubbleSort(nums):
    # Iterate through the list
    for num in range(0,len(nums) - 1):
        if nums[num] > nums[num + 1]:
            temp = nums[num]
            nums[num] = nums[num + 1]
            nums[num + 1] = temp
            bubbleSort(nums)
    return nums

def main():
    length = randint(0,50)
    nums = []
    for place in range(0,length):
        temp = randint(0,200)
        nums.append(temp)
    start = time.time()
    bubbleSort(nums)
    end = time.time()
    print("Successfully sorted! The program ran in " + str(end-start) + " seconds.")


main()
    
