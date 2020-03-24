# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        count_2 = int(n / 2)
        is_odd = n % 2

        result = 1  # default all 1
        i = 1
        while i <= count_2:
            count_1 = (count_2 - i) * 2 + is_odd
            result += self.C(count_1 + i, i)
            i += 1
        return result

    def C(self, n, i) -> int:
        return int(self.factorial(n)/(self.factorial(i) * self.factorial(n-i)))

    def factorial(self, n) -> int:
        if n == 0:
            return 1

        result = n
        for i in range(1, n, 1):
            result *= i

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.factorial(4))
    # print(solution.A(4, 2))
    # print(solution.climbStairs(2))
    # print(solution.climbStairs(3))
    # print(solution.climbStairs(4))
   # print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(5))
    print(solution.climbStairs(6))
    print(solution.climbStairs(12))






