class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            # add a Trie if it does not exist
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # reset the pointer to child
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            # add a Trie if it does not exist
            if c not in curr.children:
                return False
            # reset the pointer to child
            curr = curr.children[c]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            # add a Trie if it does not exist
            if c not in curr.children:
                return False
            # reset the pointer to child
            curr = curr.children[c]

        return True
