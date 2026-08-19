class Solution:
    def reverseBits(self, n: int) -> int:
        # there are 32 bits in each int
        # find the max set bit. For 21 that is bit 4 of 31
        # left shift until we reach 31?
        index = 0
        for i in range(32):
            bit = (n >> i) & 1
            index += bit << (31 - i)

        return index
