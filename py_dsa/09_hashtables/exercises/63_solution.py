def find_pairs(nums1, nums2, target):
    set2 = set(nums2)
    res = []
    for num in nums1:
        complement = target - num
        if complement in set2:
            res.append((num,complement))
    return res

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
assert pairs.__str__() == "[(1, 6), (3, 4), (5, 2)]"
