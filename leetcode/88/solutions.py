def merge(nums1, m, nums2, n):
    a = m + n
    m_idx = m-1
    n_idx = n-1
    
    while a >= 0:
        a -= 1
        print(a, m_idx, n_idx)
        if n_idx < 0:
            nums1[a] = nums1[m_idx]
            if m_idx >= 0:
                m_idx -= 1
            continue

        if m_idx < 0:
            nums1[a] = nums2[n_idx]
            if n_idx >= 0:
                n_idx -= 1
            continue

        if nums1[m_idx] >= nums2[n_idx]:
            nums1[a] = nums1[m_idx]
            m_idx -= 1
        else:
            nums1[a] = nums2[n_idx]
            n_idx -= 1
    
    print(nums1)


# Testing:
# Testlast_indexng Arena:
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
nums1 = []
nums2 = [1]
M = 0
N = 1
print(f"Before: {nums1}")
merge(nums1=nums1, m=M, nums2=nums2, n=N)
print(f"After: {nums1}")