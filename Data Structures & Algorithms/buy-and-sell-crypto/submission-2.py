class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxprofit = 0
        while R < len(prices):
            if prices[L] <= prices[R]:
                if maxprofit < prices[R] - prices[L]:
                    maxprofit = prices[R] - prices[L]
                R += 1
            else:
                L = R
                R = L + 1
        return maxprofit