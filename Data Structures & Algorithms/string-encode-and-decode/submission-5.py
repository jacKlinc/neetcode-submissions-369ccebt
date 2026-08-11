class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"\t{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            if s[i] == "\t":
                word = ""
                j = i + 1
                while j < len(s) and s[j] != "\t":
                    word += s[j]
                    j += 1
            
                res.append(word)

        return res