def bubbleSort(nums):
    for num in range(0,len(nums) - 1):
        if nums[num] > nums[num + 1]:
            temp = nums[num]
            nums[num] = nums[num + 1]
            nums[num + 1] = temp
            bubbleSort(nums)
    return nums

def main():
    nums = [7,1,5,3,8]
    print(bubbleSort(nums))

main()
    
