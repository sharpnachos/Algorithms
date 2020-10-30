def binarySearch (nums, l, y, x): 
    if y >= l:
        #Find the median
        mid = l + (y - l)//2
        #Check if num is median
        if nums[mid] == x: 
            return mid
        #If mid is bigger than target than go to the left side of the array
        elif nums[mid] > x: 
            return binarySearch(nums, l, mid-1, x)
        #If mid is smaller than target than go to the right side of the array
        else: 
            return binarySearch(nums, mid + 1, y, x) 
    else:
        #Target not in array
        return False

nums = [3,5,7,10,32,67,84] 
x = 67
  
result = binarySearch(nums, 0, len(nums)-1, x) 
  
if result != -1: 
    print(result)
else: 
    print("Error")