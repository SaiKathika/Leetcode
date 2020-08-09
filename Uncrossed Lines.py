#dynamic programming
def maxUncrossedLines(A, B) -> int:
    dp = [[0] * (len(B) + 1) for i in range(len(A) + 1)]        #it will create len(A)+1 x len(B)+1 Matrix with 0 values
    #dp = [print([0] * (len(B) + 1)) for i in range(len(A) + 1)]
    #print(dp)
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if(A[i - 1] == B[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(A)][len(B)]

print(maxUncrossedLines([1,4,2], [1,2,4]))