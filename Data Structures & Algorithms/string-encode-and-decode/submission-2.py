class Solution:
    def encode(self, strs: List[str]) -> str:
        self.delimeter = "\t"
        # the problem here is the delimeter
        res = ""
        for s in strs:
            res += f"{self.delimeter}{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        for i, c in enumerate(s):
            # we have a new word
            if c == self.delimeter:
                new_word = ""
                j = i + 1
                while j < len(s) and s[j] != self.delimeter:
                    new_word += s[j]
                    j += 1
                res.append(new_word)

        return res
