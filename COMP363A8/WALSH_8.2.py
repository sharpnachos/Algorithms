import random

nums = [0, 7, 3, 12, 1, 32, 56, 23, 4]
x = 0

def quickSort_r(start, stop):
    #makes sure the partitions are valid
    if stop - start > 0:
        #Calls partition to get the index of the pivot
        pivot = partition_r(start, stop)
        #Recursive calls for the left and right side of a list
        quickSort_r(start, pivot - 1) 
        quickSort_r(pivot + 1, stop)

def quickSort(start, stop):
    #Makes sure the partitions are valid
    if stop - start > 0:
        #calls partition to get the index of the pivot
        pivot = partition(start, stop)
        #recursive calls for the left and right side of the list
        quickSort(start, pivot - 1) 
        quickSort(pivot + 1, stop)

def partition_r(start, stop):
    global nums
    global x
    x += 1
    #sets the pivot as the last element
    swap(stop, random.randint(start, stop))
    #identifies the index of the pivot
    pivot = stop
    #keeps track of the current index, initialized at the start index - 1
    index = start - 1
    for num in range(start, stop):
        #Swaps numbers to find the correct placement for the pivot
        if nums[num] < nums[pivot]:
            index += 1
            swap(index, num)
        else:
            pass
    #swaps numbers to find the correct placement for the pivot
    index += 1
    swap(pivot, index)
    #returns the index of the correctly placed pivot
    return (index) 

def partition(start, stop):
    global nums
    global x
    x += 1
    #sets the pivot as the first element
    pivot = nums[start]
    #gets that element out of the way
    swap(start, stop)
    #keeps track of the current index, initializes it as the start index - 1
    index = start - 1
    for num in range(start, stop):
        #swaps numbers to find the correct placement for the pivot
        if nums[num] < pivot: 
            index += 1
            swap(num, index)
        else:
            pass
    #swaps numbers to find the correct placement for the pivot
    index += 1
    swap(index, stop)
    #returns the index of the correctly placed pivot
    return (index) 

def main():
    global nums
    global nums2
    global x
    print(nums)
    print('First element is pivot:')
    quickSort(0, len(nums) - 1)
    print(nums)
    print("Partitioned " + str(x) + " times")
    x = 0
    nums.clear()
    nums = [0, 7, 3, 12, 1, 32, 56, 23, 4]
    print('Randomly chosen pivot:')
    quickSort_r(0, len(nums) - 1)
    print(nums)
    print("Partitioned " + str(x) + " times")

def swap(i1, i2):
    #Method for swapping elements in a list using their indices as parameters
    global nums
    temp = nums[i1]
    nums[i1] = nums[i2]
    nums[i2] = temp
    
main()

