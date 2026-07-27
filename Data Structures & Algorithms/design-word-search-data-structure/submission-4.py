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
        def dfs(ix, node):
            curr = node
            for i in range(ix, len(word)):
                c = word[i]
                # do dfs
                if c == ".":
                    # wildcards must explore all of the node's children 
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.end

        return dfs(0, self.root)
