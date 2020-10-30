def insertionSort(nums):
    for num in range(1, len(nums)):
        item = nums[num]
        previous = num - 1
        while previous >= 0 and item < nums[previous]:
            nums[previous + 1] = nums[previous]
            previous = previous - 1
        nums[previous + 1] = item
    print(nums)
