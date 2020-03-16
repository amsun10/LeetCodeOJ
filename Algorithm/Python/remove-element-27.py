# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums, val: int) -> int:
        array_len = 0
        while array_len < len(nums):
            if nums[array_len] == val:
                nums.pop(array_len)
            else:
                array_len += 1

        return array_len
