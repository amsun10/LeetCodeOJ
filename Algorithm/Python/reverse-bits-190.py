class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0
        while i <= 31:
            result += (n & 0x0001) << (31 - i)
            n = n >> 1
            i -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    i = 0b1101
    a = solution.reverseBits(i)
    print(a, 'b')
