class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon = b, a, l, o, n
        counter = Counter(text)
        balloon = Counter("balloon")

        res = len(text)
        for c in balloon:
            res = min(res, counter[c] // balloon[c])
        return res
