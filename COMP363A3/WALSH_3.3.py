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
