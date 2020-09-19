#https://leetcode.com/problems/partition-labels/discuss/828031/Python-Greedy-O(n)-solution-explained

def partitionLabels(S):
    end = {c: i for i, c in enumerate(S)}
    curr, res = 0, [0]
    print('end', end)
    while curr < len(S):
        last = end[S[curr]]
        print('last', last)
        while curr <= last:
            symb = S[curr]
            last = max(last, end[symb])
            curr += 1
        res.append(curr)

    return [res[i] - res[i-1] for i in range(1, len(res))]

print(partitionLabels("ababcbacadefegdehijhklij"))
'''
#best one
def partitionLabels(self, S: str) -> List[int]:
    last = {s: i for i, s in enumerate(S)}
    j,anchor = 0,0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
            
    return ans
'''