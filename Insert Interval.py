#https://leetcode.com/problems/insert-interval/discuss/844494/Python-O(n)-solution-explained
def insert(intervals, newInterval):
    res, i = [], -1
    for i, (x, y) in enumerate(intervals):
        if y < newInterval[0]:
            res.append([x, y])
        elif newInterval[1] < x:
            i -= 1
            break
        else:
            newInterval[0] = min(newInterval[0], x)
            newInterval[1] = max(newInterval[1], y)
                
    return res + [newInterval] + intervals[i+1:]

print(insert([[1,3],[6,9]], [2,5]))