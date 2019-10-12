__author__ = 'amsun'
"https://leetcode.com/problems/contains-duplicate/"
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
