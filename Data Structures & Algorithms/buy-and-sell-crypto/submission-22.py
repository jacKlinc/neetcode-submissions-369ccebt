class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                max_prof = max(max_prof, prof)
            elif prices[l] > prices[r]:
                l = r
            r += 1
        
        return max_prof
            