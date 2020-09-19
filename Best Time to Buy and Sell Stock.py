#using DP
def maxProfit(prices):
    res, dp = 0, 0
    lst = []
    for i in range(0, len(prices)-1):   #here we are not considering last index bcoz
        q = prices[i+1] - prices[i]     #here we are doing i+1 so we took lst idx in loop then we get idx out of range
        dp = max(dp + q, q)
        lst.append(dp)
        res = max(res, dp)
    return lst, res

print(maxProfit([7,1,5,3,6,4]))
'''
#without dp
def maxProfit(self, prices: List[int]) -> int:
    minprice = 9999999999
    maxprofit = 0
    for i in range(len(prices)): 
        if (prices[i] < minprice):
            minprice = prices[i]
        elif (prices[i] - minprice > maxprofit):
            maxprofit = prices[i] - minprice
    
    return maxprofit
'''