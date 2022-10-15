class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        minprice= sys.maxsize
        maxpro=0
        for i in range(len(prices)):
            minprice= min(prices[i],minprice)
            maxpro= max(maxpro, prices[i]- minprice)
        return maxpro
