class Solution:
    def maxDifference(self, s: str) -> int:
        # could store the freq in hash key
        # find the biggest odd and even
        count = Counter(s)
        odd_max, even_min = 0, len(s)

        for cnt in count.values():
            if cnt & 1:
                odd_max = max(odd_max, cnt)
            else:
                even_min = min(even_min, cnt)

        return odd_max - even_min
