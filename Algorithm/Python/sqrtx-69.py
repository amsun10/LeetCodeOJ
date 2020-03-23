# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [1, 0]:
            return x

        if x == 2:
            return 1

        sum = int(x/2) + 1

        for i in range(sum + 1):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(591420545))



