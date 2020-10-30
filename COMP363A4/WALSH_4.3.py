from bisect import bisect_left 
def fibonacciSearch(nums, x, y):  
    fib1 = 1 #(n-1) fib
    fib2 = 0 #(n-2) fib
    fib = fib2 + fib1 
    #Find small fib
    while (fib < y): 
        fib2 = fib1 
        fib1 = fib
        fib = fib2 + fib1 
    offset = -1
    while (fib > 1): 
        num = min(offset + fib2, y - 1) 
        if (nums[num] < x): 
            #target is greater so move down
            fib = fib1 
            fib1 = fib2 
            fib2 = fib - fib1 
            offset = num
        elif (nums[num] > x): 
            #move 1 down
            fib = fib2 
            fib1 = fib1 - fib2 
            fib2 = fib - fib1 
        else: 
            #Found it
            return num
    if(fib1 and nums[offset + 1] == x): 
        return offset + 1


nums = [3,5,7,10,32,67,84] 
x = 3
y = len(nums)
  
result = fibonacciSearch(nums, x, y)
  
if result != -1: 
    print(result)
else: 
    print("Error")