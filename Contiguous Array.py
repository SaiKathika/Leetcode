def findMaxLength(nums) -> int:
        d = {}
        curr = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==1:
                curr += 1
            else:
                curr -= 1
            
            if curr==0:
                ans = max(ans, i+1)
                print(ans)
            
            if curr in d:
                ans = max(ans, i-d[curr])
                print('at d:', ans)
            else:
                d[curr] = i
        
        return ans

print(findMaxLength([0,1,0]))