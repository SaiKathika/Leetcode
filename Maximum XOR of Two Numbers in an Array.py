#O(n)
def findMaximumXOR(nums):
    answer = 0
    for i in range(32)[::-1]:
        answer <<= 1    #same as answer * 2**1
        prefixes = {num >> i for num in nums}
        #below line same as
        '''
        candidate = ans + 1
            for p in prefixes:
                if candidate ^ p in prefixes:
                    ans = candidate
                    break
        '''
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer

print(findMaximumXOR([3, 10, 5, 25, 2, 8]))
'''
#O(n^2)
def findMaximumXOR(nums):
    l = len(nums)
    lst = []
    for i in range(l):
        for j in range(l):
            a = nums[i] ^ nums[j]
            #print(f'{nums[i]}^{nums[j]} = {a}')
            lst.append(a)
    return max(lst)

print(findMaximumXOR([3, 10, 5, 25, 2, 8]))
'''