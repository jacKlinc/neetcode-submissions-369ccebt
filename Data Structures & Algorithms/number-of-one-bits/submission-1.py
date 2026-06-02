class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for s in bin(n)[2:]:
            if int(s) ^ 1 == 0:
                res += 1
        
        return res