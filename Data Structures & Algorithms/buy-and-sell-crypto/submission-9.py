class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0

        while r < len(prices):
            print(prices[l], prices[r])
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                max_prof = max(max_prof, prof)
            else:
                l = r
            r += 1

        return max_prof