'''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices):
            buy = prices[0]
        max_ = 0
        for i in range(1, len(prices)):
            if prices[i] - buy < 0:
                buy = prices[i]
            if prices[i] - buy > max_:
                max_ = prices[i] - buy
        return max_
            
