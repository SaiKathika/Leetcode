#Best Answer
'''
        dp = [1] + [0] * (amount);    
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
'''
#Explanation
#https://leetcode.com/problems/coin-change-2/discuss/676134/Python-3-simple-DP-solution-with-explanation
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount_plus_1 = amount + 1
        sol = [0] * amount_plus_1
        sol[0] = 1
        for coin in coins:
            for j in range(coin, amount_plus_1):
                sol[j] += sol[j - coin]
        return sol[-1]