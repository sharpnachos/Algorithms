from random import randint
import time

#TODO: Add comments

def insertionSort(nums):
    for num in range(1, len(nums)):
        current = nums[num]
        previous = num - 1
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
    insertionSort(nums)
    end = time.time()
    print("Successfully sorted! The program ran in " + str(end-start) + " seconds.")

main()