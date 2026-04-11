class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting results in a O(n.log(n))

        # Max heap allows for a max k=2
        # Pop things off the heap k times. Each pop is O(n)

        # Linear time can be achieved with Bucket Sort
        d = {}
        freq = [[] for i in range(len(nums) + 1)]

        # If all values were indentical, the max size would be it's length
        for num in nums:
            d[num] = 1 + d.get(num, 0)

        for n, c in d.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res