class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """if t == s:
            return t
        if t not in s:
            return """""
        
        # O(n) where is number of characters in s and O(m) where is the unique chars in both s and t
        count_t, window = {}, {}
        # Initialise
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)        

            if c in count_t and window[c] == count_t[c]:
                # update have count
                have += 1
            # keep shrinking from the left
            while have == need:
                # update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                # pop from the left
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1 

        l, r = res

        if res_len != float("infinity"):
            return s[l:r + 1]
      
        return ""