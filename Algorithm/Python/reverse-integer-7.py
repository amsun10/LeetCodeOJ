# https://leetcode.com/problems/reverse-integer/

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        s = "{}".format(x)[::-1]
        if s[-1] == '-':
            result = int(s[:-1]) * -1
        else:
            result = int(s)

        if result < - 2**31 or result > 2**31 - 1:
            result = 0

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-1230))
    print(solution.reverse(1534236469))

