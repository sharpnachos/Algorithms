import math 
def jumpSearch(nums, x, y):
    jump = math.sqrt(y) 
    num = 0
    while (nums[int(min(jump, y) - 1)] < x): 
        #If below x jump forward
        num = jump
        jump += math.sqrt(y) 
        if num >= y: 
            #Element is not found
            return False
    while nums[int(num)] < x: 
        num += 1
        if num == min(jump, y): 
            #Element is not found
            return False
    if nums[int(num)] == x: 
        #Found it
        num = num //1
        return num
    return False

nums = [3,5,7,10,32,67,84] 
x = 3
y = len(nums)
  
result = jumpSearch(nums, x, y)
  
if result != -1: 
    print(result)
else: 
    print("Error")