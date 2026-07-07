class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0

        while r < len(prices):
            print(l, r, prices[l], prices[r])
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                max_prof = max(max_prof, prof)
            elif prices[l] > prices[r]:
                l = r
            r += 1
        
        return max_prof