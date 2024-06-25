class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        maxProfit = 0
        while l < r and l < len(prices) and r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1
        print('r', prices[r-1])
        print('l', prices[l])
        
        return maxProfit