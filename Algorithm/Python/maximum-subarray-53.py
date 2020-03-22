# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum = nums[0]

        for i in nums[1:]:
            if max_sum + i < i:
                max_sum = i
            else:
                if i >= 0:
                    max_sum = max_sum + i
                else:
                    while


        return max_sum
        pass


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
