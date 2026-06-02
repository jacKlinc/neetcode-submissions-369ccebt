class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for s in bin(n):
            if s == "1":
                res += 1
        
        return res