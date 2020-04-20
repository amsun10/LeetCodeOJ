# https://leetcode.com/problems/factorial-trailing-zeroes/
# http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        x = 5
        while n >= x:
            count += int(n / x)
            x = x * 5
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(30))
