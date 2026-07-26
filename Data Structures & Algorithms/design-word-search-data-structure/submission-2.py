class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                c = word[i]
                # run dfs
                if c == ".":
                    # . could match any of the characters
                    # Looping over ALL children to find matches
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                if c not in curr.children:
                    return False
                curr = curr.children[c]

            return curr.end

        return dfs(0, self.root)
