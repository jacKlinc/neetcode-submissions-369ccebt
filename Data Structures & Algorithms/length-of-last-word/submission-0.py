class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # loop backwards until we hit a space
        j = 0
        backwards = s[::-1]
        found = False
        for i in range(len(s)):
            print(backwards[i])
            if backwards[i] != " ":
                found = True
            if not found:
                continue
            if found and backwards[i] == " ":
                break
            j += 1

        return j
