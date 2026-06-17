class Solution:
    """def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # probably a pointer
        # calcualting the each val is the r - l + 1
        diff = [] # store diff here
        for i in range(len(temperatures)):
            current = temperatures[i]
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
        return diff"""
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic Decreasing Stack
        # use a stack to remember the previous val
        # if the successive val is less, apppend to the stack
        # upon finding a bigger val, pop the smaller ones
        stack = [] # pair: [temp, index]
        diff = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                diff[stack_i] = i - stack_i
            
            stack.append([t, i])
        
        return diff

