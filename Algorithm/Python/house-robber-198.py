# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: []) -> int:
        a = 0
        b = 0
        for index, i in enumerate(nums):
            if index % 2 == 0:
                a = max(a + i, b)
            else:
                b = max(b + i, a)

        return max(a, b)


if __name__ == '__main__':
    solution = Solution()

    # print(solution.rob([1, 2, 1, 1]))  # 18
    # print(solution.rob([2, 1, 1, 10000, 1]))  # 18
    print(solution.rob([8, 2, 8, 9, 2]))  # 18
   # print(solution.rob([2, 2, 4, 3]))  # 6
    #print(solution.rob([2, 2, 4, 3, 2, 5]))  # 11
    # print(solution.rob([1, 7, 9, 4]))
    # print(solution.rob([2, 4, 1]))
    # print(solution.rob([2, 3, 2]))
    # print(solution.rob([8, 9, 7, 1]))
    # print(solution.rob([8, 15, 7, 20]))
    # print(solution.rob([15, 8, 7, 20]))
    # print(solution.rob([15, 8, 9, 7, 20]))
    # print(solution.rob([2, 3, 4, 2]))
    # print(solution.rob([2, 4, 3, 2]))
    # print(solution.rob([1, 2, 3, 1]))
    # print(solution.rob([2, 7, 9, 3, 1]))
