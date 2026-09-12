class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        # Loop over each email and check if it is already in the set
        for e in emails:
            # . is a wildcard
            # + means omit until @
            i = 0
            email = ""
            while i < len(e):
                if e[i] != ".":
                    email += e[i]
                if e[i] == "+":
                    j = i+1
                    while j < len(e):
                        if e[j] == "@":
                            print(e[j+1 : len(e)])
                            email += e[j+1 : len(e)]
                            break
                        j += 1
                    break
                if e[i] == "@":
                    # print(e[i+1 : len(e)])
                    email += e[i+1 : len(e)]
                    break
                i += 1
            if email not in unique:
                unique.add(email)
        print(unique)

        return len(unique)
