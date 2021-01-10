# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True

        if num == 0:
            return False

        while num not in [2, 3, 5]:
            for i in [2, 3, 5]:
                if num % i == 0:
                    num = num / i
                    if num in [2, 3, 5]:
                        return True
                    else:
                        break
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(0))
    print(solution.isUgly(2))
    print(solution.isUgly(6))
    print(solution.isUgly(8))
    print(solution.isUgly(14))