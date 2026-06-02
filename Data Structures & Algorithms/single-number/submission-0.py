class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for n in nums:
            if n in res:
                res[n] += 1 
                continue
            
            res.update({n: 1})
        
        return min(res, key=res.get)