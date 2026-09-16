class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # map number of occurences to characters
        counter = Counter(arr)

        for s in arr:
            if counter[s] == 1:
                k -= 1
                if k == 0:
                    return s

        return ""
