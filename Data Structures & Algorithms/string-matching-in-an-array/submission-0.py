class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.cnt = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        for i in range(len(word)):
            cur = self.root
            for j in range(i, len(word)):
                c = word[j]
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                cur.cnt += 1

    def find(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            # cur = node.children[idx]
        return cur.cnt > 1


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        res = []
        for word in words:
            if trie.find(word):
                res.append(word)

        return res
