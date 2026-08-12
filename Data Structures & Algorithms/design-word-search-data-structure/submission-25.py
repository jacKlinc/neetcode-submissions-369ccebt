class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(ix, node):
            cur = node
            for i in range(ix, len(word)):
                if (c := word[i]) == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.end

        return dfs(0, self.root)
