class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        min_num = sys.maxsize
        for i in range(len(prices)):
            if prices[i]< min_num:
                min_num = prices[i]
            else:
                max_num = max(max_num,prices[i] - min_num)
        return max_num