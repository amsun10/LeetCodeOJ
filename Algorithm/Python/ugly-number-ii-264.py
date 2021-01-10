# https://leetcode.com/problems/ugly-number-ii/
class Solution:
    a = [1]

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return self.a[-1]
        p2 = 0
        p3 = 0
        p5 = 0

        for i in range(1, n):
            min_value = min(self.a[p2] * 2, self.a[p3] * 3, self.a[p5] * 5)
            self.a.append(min_value)
            while self.a[p2] * 2 <= min_value:
                p2 += 1

            while self.a[p3] * 3 <= min_value:
                p3 += 1

            while self.a[p5] * 5 <= min_value:
                p5 += 1

        return self.a[-1]




if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(1))
    print(solution.nthUglyNumber(2))
    print(solution.nthUglyNumber(3))
    print(solution.nthUglyNumber(4))
    print(solution.nthUglyNumber(5))
    print(solution.nthUglyNumber(6))
    print(solution.nthUglyNumber(7))
    print(solution.nthUglyNumber(8))
    print(solution.nthUglyNumber(9))
    print(solution.nthUglyNumber(10))
    print(solution.nthUglyNumber(11))
    print(solution.nthUglyNumber(12))
    print(solution.nthUglyNumber(13))
