__author__ = 'xizhang'
"https://leetcode.com/problems/move-zeroes/"

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        j = 0
        for i in range(length):
            if nums[j] == 0:
                nums.append(0)
                nums.pop(j)
            else:
                j += 1


if __name__ == '__main__':
    solu = Solution()
    solu.moveZeroes([0, 0, 1])
    solu.moveZeroes([1,0,3,12,0])
