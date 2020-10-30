import time
from random import randint

#TODO: Add comments

def selectionSort(nums):
    for num in range(len(nums)):
        minimum = num
        for numnum in range(num+1, len(nums)):
            if nums[minimum] > nums[numnum]:
                minimum = numnum
        temp = nums[num]
        nums[num] = nums[minimum]
        nums[minimum] = temp
    return nums


def main():
    length = randint(0,1000)
    nums = []
    for place in range(0,1000):
        temp = randint(0,1000)
        nums.append(temp)
    start = time.time()
    selectionSort(nums)
    end = time.time()
    print("Successfully sorted! The program ran in " + str(end-start) + " seconds.")


main()
