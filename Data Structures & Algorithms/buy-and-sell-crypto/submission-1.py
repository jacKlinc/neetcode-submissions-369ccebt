class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this is a common problem that cane be solve with the double pointer
        # A left pointer is assigned to the buy at the 0th element
        # A right pointer is assigned to the sell at 1st element
        # this will have a time complexity of O(n) while the brute force will have O(n²)
        l = 0
        r = 1
        max_prof = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                max_prof = max(prof, max_prof)
            else:
                l = r
            r += 1
        return max_prof

