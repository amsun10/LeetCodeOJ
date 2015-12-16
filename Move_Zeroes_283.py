__author__ = 'xizhang'
"https://leetcode.com/problems/move-zeroes/"

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        loop_count = 0
        length = len(nums)
        while True:
            if nums[index] == 0:
                nums.append(0)
                nums.pop(index)
            else:
                index += 1
            loop_count += 1
            if loop_count == length:
                break
        print nums


if __name__ == '__main__':
    solu = Solution()
    solu.moveZeroes([0, 0, 1])
    solu.moveZeroes([1,0,3,12,0])
