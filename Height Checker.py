def heightChecker(heights):
    sortedlst = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != sortedlst[i]:
            count += 1
    return count
print(heightChecker([5,1,2,3,4]))