class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_stock = 0
        min_stock = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_stock:
                min_stock = prices[i]
            else:
                max_stock += prices[i] - min_stock
                min_stock = prices[i]
        return max_stock