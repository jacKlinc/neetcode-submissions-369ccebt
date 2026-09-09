class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in cur.children:
                cur.children[(c1, c2)] = TrieNode()
            cur = cur.children[(c1, c2)]
            cur.count += 1

    def count(self, word):
        cur = self.root
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in cur.children:
                return 0
            cur = cur.children[(c1, c2)]
        return cur.count


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        root = Trie()
        cnt = 0

        for w in reversed(words):
            cnt += root.count(w)
            root.add(w)
        return cnt
