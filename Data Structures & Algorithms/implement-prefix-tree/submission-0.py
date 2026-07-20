class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            # if it does not exist
            if curr.children[index] is None:
                curr.children[index] = TrieNode()

            curr = curr.children[index]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            # if is's not there: fail
            if curr.children[index] is None:
                return False
            # it's there: set the pointer to that
            curr = curr.children[index]

        return curr.is_end_of_word

    def startsWith(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord("a")
            # if is's not there: fail
            if curr.children[index] is None:
                return False
            # it's there: set the pointer to that
            curr = curr.children[index]

        return True
