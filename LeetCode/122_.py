class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in [0,1]:
            return 0

        profit = 0
        for d in range(1, len(prices)):
            if prices[d-1] < prices[d]:
                profit += prices[d] - prices[d-1]
        return profit      
