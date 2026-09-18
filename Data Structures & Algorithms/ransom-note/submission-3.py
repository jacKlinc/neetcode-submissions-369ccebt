class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom, mag = Counter(ransomNote), Counter(magazine)

        for c in ransom:
            if mag[c] < ransom[c]:
                return False

        return True
