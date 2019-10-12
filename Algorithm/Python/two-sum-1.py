# https://leetcode.com/problems/two-sum/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, i in enumerate(nums):
            j = target - i
            try:
                index_j = nums.index(j)
                if index_j != index:
                    return [index, index_j]
            except ValueError:
                pass


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([-1, -2, -3, -4, -5], -8))