class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                
        profit = 0

        for day in range(len(prices) - 1):
            if prices[day] < prices[day + 1]:
                profit += prices[day + 1] - prices[day]
        return(profit)