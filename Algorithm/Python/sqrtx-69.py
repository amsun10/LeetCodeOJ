# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        lo, hi = 0, x
        while hi - lo > 1:
            mid = (hi + lo) // 2

            if mid * mid > x:
                hi = int(mid)
            else:
                lo = int(mid)

        return (hi + lo) // 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(591420545))



