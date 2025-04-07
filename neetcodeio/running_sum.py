def running_sum(nums=[]):
    if not nums:
        return
    sums = [0] * len(nums)
    for i, num in enumerate(nums):
        if i == 0:
            sums[i] = num
        else:
            sums[i] = num + sums[i - 1]
    return sums


# assert running_sum([1,2,3,4,5,6,7,8,9]) == [1,3,6,10,15,21,28,36,45]
running_sum()
