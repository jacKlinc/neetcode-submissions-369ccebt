class Solution:

    def encode(self, strs: List[str]) -> str:
        # Delimiters are complicated because the delimiter character might appear anyway
        # Storing word length as an array could work but the solution requires statelessness
        # Combining the two: prefixing each word with the word length and delimiter works
        res = ""
        for s in strs:
            res += f"{len(s)},{s}"
        return res


    def decode(self, s: str) -> List[str]:
        # 0-9: 48-57
        # A-Z: 65-90
        # a-z: 97-122

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ",":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res


        #words = []
        #for i, ss in enumerate(s):
         #   uni_char = ord(ss)
          #  if uni_char in [48, 57] and s[i+1] == ",":
           #     word = s[i + 2:int(uni_char) + 2]
            #    words.append(word)
        #return words