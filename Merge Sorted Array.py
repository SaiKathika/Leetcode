def merge(nums1, m, nums2, n):
    del nums1[m:]
    nums1.extend(nums2)
    nums1.sort()
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))