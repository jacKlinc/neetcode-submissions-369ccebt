class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # probably a pointer
        # calcualting the each val is the r - l + 1
        diff = [] # store diff here
        for i in range(len(temperatures)):
            current = temperatures[i]
            #for j in range(1, len(temperatures) - 1):
            j = i + 1
            while j < len(temperatures):
                print(current, i, j, temperatures[j])
                # current val is bigger or equal to the next one so skip iteration
                if current >= temperatures[j]:
                    j += 1    
                    continue
                # append val and exit while
                diff.append(j - i)
                break
            # this means no value has been found     
            if j == len(temperatures):
                diff.append(0)       
        return diff