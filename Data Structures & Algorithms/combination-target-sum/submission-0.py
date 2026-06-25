class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # hash map storing difference?
        # return hash map where key is zero
        # append list of sum items
        
        # backtracking: recursively try different solutions
        # 1. Choose initial solution
        # 2. Try all extensions that solution
        # 3. Return if valid
        # 4. Backtrack to others in case it does not
        # 5. Repeat 2-4 until we get one

        # Time complexity for decision tree: O(2^t) where t is the target

        res = []

        def dfs(i, current: List, total: int):
            if total == target:
                # Use a copy to prevent modifying the original
                res.append(current.copy())
                return
            # pointer out of bounds or 
            if i >= len(nums) or total > target:
                return

            current.append(nums[i])
            # added to combinations
            dfs(i, current, total + nums[i]) # this is branch one
            # remove last one
            current.pop()
            dfs(i + 1, current, total) # this is branch two

        dfs(0, [], 0)
        return res      
