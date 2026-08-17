class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make frequency map
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for n in count.keys():
            # (frequency, number)
            heapq.heappush(heap, (count[n], n))
            # Pop if heap size exceeds k
            if len(heap) > k:
                heapq.heappop(heap)

        # heap now has k most frequent elements
        res = []
        for _ in range(k):
            # pop each to return the result
            res.append(heapq.heappop(heap)[1])

        return res
