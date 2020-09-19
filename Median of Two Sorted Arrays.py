def findMedianSortedArrays(nums1, nums2):
    lst = sorted(nums1 + nums2)
    n = len(lst)
    if n % 2 > 0:
        return float(lst[n//2])
    else:
        i = n//2
        return float((lst[i-1] + lst[i]) / 2)
print(findMedianSortedArrays([1,3], [2,4]))

'''
#using statistics module
import statistics 
lst = sorted(nums1 + nums2)
m = statistics.median(lst)
return m
'''