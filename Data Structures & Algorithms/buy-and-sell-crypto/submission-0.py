class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_after = [0] * n
        res = 0

        for j in range(n -2, -1, -1):
            max_after[j] = max(max_after[j+1], prices[j+1])
        
        for i in range(n-1):
            res = max(res, max_after[i] - prices[i])

        return res