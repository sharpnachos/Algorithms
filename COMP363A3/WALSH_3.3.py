def selectionSort(nums):
    for num in range(len(nums)):
        #finds smallest guy
        minimum = num
        for numnum in range(num+1, len(nums)):
            if nums[minimum] > nums[numnum]:
                minimum = numnum
        #switches little guy with first guy
        temp = nums[num]
        nums[num] = nums[minimum]
        nums[minimum] = temp
    return nums
