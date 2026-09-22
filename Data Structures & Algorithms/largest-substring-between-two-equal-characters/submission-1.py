class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # could do a counter
        # return -1 if none of the counts are more than 1
        # loop over the string and do a lookup
        distance = {}
        res = -1
        for i, c in enumerate(s):
            if c in distance:
                res = max(res, i - distance[c] - 1)
            else:
                distance[c] = i
        return res
