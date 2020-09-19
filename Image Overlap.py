from collections import Counter
def largestOverlap(A, B):
    A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
    B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
    count = Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
    return max(count.values() or [0])

print(largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]))