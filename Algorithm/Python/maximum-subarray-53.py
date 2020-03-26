# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list) -> int:
        result = nums[0]
        temp_sum = nums[0]
        start_index = 0
        for index, i in enumerate(nums[1:]):
            temp_sum = result + i
            if temp_sum >= result:
                if temp_sum < i:
                    result = i
                else:
                    result = temp_sum






        return max_sum
        pass


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
