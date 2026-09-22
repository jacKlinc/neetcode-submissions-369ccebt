class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        for i, c in enumerate(s):
            if c not in count:
                count[c] = i
            else:
                count[c] = n

        res = n
        for c in count:
            res = min(res, count[c])

        return -1 if res == n else res