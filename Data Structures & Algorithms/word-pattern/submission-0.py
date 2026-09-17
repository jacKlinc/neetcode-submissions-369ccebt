class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # seems like another counter problem
        # order is important here
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        char_word, word_char = {}, {}

        for c, w in zip(pattern, words):
            if (c in char_word and char_word[c] != w) or (w in word_char and word_char[w] != c):
                return False
            char_word[c], word_char[w] = w, c

        return True
