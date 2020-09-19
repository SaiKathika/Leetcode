def sortArrayByParity(A):
    def sortFunc(i):
        return i%2

    A.sort(key=sortFunc)
    return A

print(sortArrayByParity([3,1,2,4]))