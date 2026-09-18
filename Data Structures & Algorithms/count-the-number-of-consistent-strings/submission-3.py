class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        arr = [False] * 26
        for c in allowed:
            arr[ord(c) - ord("a")] = True

        res = len(words)
        for w in words:
            for c in w:
                if not arr[(ord(c) - ord("a"))]:
                    res -= 1
                    break

        return res
