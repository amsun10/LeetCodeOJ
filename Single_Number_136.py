__author__ = 'amsun'
"https://leetcode.com/problems/single-number/"

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = []
        if len(nums) == 1:
            return nums[0]
        else:
            while len(nums) > 1 and nums[0] in nums[1:]:
                nums.pop(0)
            return nums[0]

        return nums[0]
if __name__ == '__main__':
    solu = Solution()
    print solu.singleNumber([4, 3, 5, 6, 7, 5, 4, 7, 6])
    print solu.singleNumber([1, 0, 1])