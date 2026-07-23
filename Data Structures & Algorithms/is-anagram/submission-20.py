class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_s = set(s)
        for ss in unique_s:
            if t.count(ss) != s.count(ss):
                return False

        return len(s) == len(t)