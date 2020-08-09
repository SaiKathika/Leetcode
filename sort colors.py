#Best solution
'''
l = len(nums)
    for i in range(l-1):
        for j in range(0, l-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
'''
def sortColors(nums):
    beg, mid, end = 0, 0, len(nums) - 1
        
    while mid <= end:
        if nums[mid] == 0:
            nums[beg], nums[mid] = nums[mid], nums[beg]
            mid += 1
            beg += 1
        elif nums[mid] == 2:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1
        else:  #nums[mid] == 1:
            mid += 1

'''
The idea here is the following: we keep 3 pointers: for each of colors (numbers). I called them
beg = 0, mid = 0, end = len(nums) - 1. The idea here is to put sorted 0 and 1 to the beginning and sorted 2s to the end. Then we iterate over all elements and process each new element in the following way. Imagine, that we already sorted some of the elements, our invariant will be 00...0011...11......22....22, where we already put some 0 and 1 in the beggining and some 2 to the end. Then there are 3 possible optinos for new element ?:

00...0011...11?......22....22, where ? = 1, then we do not need to change any elements, just move mid pointer by 1 to the right.
00...0011...11?......22....22, where ? = 2, then we need to put this element befor the first already sorted 2, so we change these elements and then move pointer end by 1 to the left.
00...0011...11?......22....22, where ? = 0, then we need to swap this element with the last sorted 0 and also move two pointers mid and beg by 1.
We can see it this way, that pointers beg, mid and end always point at elements just before the last 0 , the last 1 and the first 2.

Complexity: Time complexity is O(n), because each moment of time we move at least one of the pointers. Additional space complexity is O(1): to keep only 3 variables: beg, mid and end.
'''