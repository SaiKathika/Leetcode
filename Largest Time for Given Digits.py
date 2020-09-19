from itertools import permutations

def largestTimeFromDigits(A):
    lst = []
    for i in permutations(A):
        if i[0]*10 + i[1] <= 23 and i[2] <= 5:
            lst.append('{}{}:{}{}'.format(str(i[0]), str(i[1]), str(i[2]), str(i[3])))
    if lst:
        return max(lst)
    return ""
print(largestTimeFromDigits([1,2,3,4]))