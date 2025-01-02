def merge(nums1, m, nums2, n):
    """Start Here"""



# Testing Arenas:

# Test 0:
nums1 = [2,3,0,0,0]
nums2 = [0,1,3]
M = 2
N = 3
print(f"Before: {nums1}, {nums2}")
merge(nums1=nums1, m=M, nums2=nums2, n=N)
print(f"After: {nums1}")

# Test 1:
nums1 = [2]
nums2 = []
M = 1
N = 0
print(f"Before: {nums1}")
merge(nums1=nums1, m=M, nums2=nums2, n=N)
print(f"After: {nums1}")

# Test 2:
nums1 = [2]
nums2 = [0,1,3]
M = 2
N = 3
print(f"Before: {nums1}")
merge(nums1=nums1, m=M, nums2=nums2, n=N)
print(f"After: {nums1}")