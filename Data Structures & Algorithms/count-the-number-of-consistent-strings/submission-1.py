class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        unique_s = set(allowed)
        for w in words:
            cnt += 1
            for c in w:
                if c not in unique_s:
                    cnt -= 1
                    break

        return cnt
