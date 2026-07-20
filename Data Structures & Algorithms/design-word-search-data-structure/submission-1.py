class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            # if it does not exist
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    # use DFS to traverse all existing characters
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                # check for wildcard in previous pos
                # not found
                if c not in curr.children:
                    return False

                curr = curr.children[c]
            return curr.is_end_of_word

        return dfs(0, self.root)
