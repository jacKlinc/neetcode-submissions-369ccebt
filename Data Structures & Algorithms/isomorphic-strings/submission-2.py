class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # for something to be Isomorphic, the char count needs to match
        # Not only that, also position and count
        # Input: s = "egg", t = "add"
        # 0 is "a" in alphabet
        # {4: [0], 6: [1, 2]}
        if len(s) != len(t):
            return False

        def hash(s, t):
            res = {}
            for i in range(len(s)):
                if s[i] in res and res[s[i]] != t[i]:
                    return False
                res[s[i]] = t[i]
            return True

        return hash(s, t) and hash(t, s)
