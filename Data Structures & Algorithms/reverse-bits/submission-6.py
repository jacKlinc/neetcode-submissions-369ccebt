class Solution:
    def reverseBits(self, n: int) -> int:
        index = 0
        # 32 bits for an int
        for i in range(32):
            # extract the ith bit of n
            bit = (n >> i) & 1
            print(bit, index)
            # shift by 31 to reverse
            index += bit << (31 - i)

        return index
