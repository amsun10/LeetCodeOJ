# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum = nums[0]
        temp_sum = nums[0]
        for index, i in enumerate(nums[1:]):
            temp_sum += i
            if temp_sum < i:
                if max_sum < i:
                    max_sum = i
                temp_sum = i
            else:
                if temp_sum > max_sum:
                    max_sum = temp_sum
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([-2, -1]))
    print(solution.maxSubArray([-1, -2]))

    print(solution.maxSubArray([8, -19, 5, -4, 20]))
