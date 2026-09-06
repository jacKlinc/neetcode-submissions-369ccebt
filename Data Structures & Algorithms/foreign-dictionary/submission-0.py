class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # lexicographically: alphabetical
        # but: "10" < "2" because the first charcater is less

        # could make an adj list where each neighbouring string is a connection
        # we're comparing the differing charcaters

        # "hrn","hrf": diff = "n". "n" is before "f"
        # "enn","rfnn": diff = "e", "r". "e" is before "r"

        adj_l = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # checking matching prefixes
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_l[w1[j]].add(w2[j])
                    break

        visiting, visited = set(), set()
        stack = []

        def dfs(node):
            if node in visiting:
                return True
            if node in visited:
                return False

            visiting.add(node)
            for neighbour in adj_l[node]:
                if dfs(neighbour):
                    return True

            visiting.remove(node)
            visited.add(node)

            stack.append(node)


        for c in adj_l:
            if dfs(c):
                return ""

        return "".join(stack[::-1])
