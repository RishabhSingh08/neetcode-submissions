class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] - prices[j] <= minProfit:
                    minProfit = prices[i] - prices[j]
        return abs(minProfit)
