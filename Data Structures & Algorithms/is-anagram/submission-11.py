class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_unique = set(s)
        if s_unique != set(t):
            return False

        for ss in s_unique:
            if t.count(ss) != s.count(ss):
                return False
        
        return True