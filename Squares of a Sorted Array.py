def sortedSquares(A):
    lst = [i * i for i in A]
    lst.sort()
    return lst

print(sortedSquares([-4,-1,0,3,10]))