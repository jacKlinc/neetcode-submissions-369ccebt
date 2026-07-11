class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ss in set(s):
            if t.count(ss) != s.count(ss):
                return False

        return len(s) == len(t)
        