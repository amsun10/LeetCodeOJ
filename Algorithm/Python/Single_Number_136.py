__author__ = 'amsun'
"https://leetcode.com/problems/single-number/"

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        i = nums[0]
        for index, value in enumerate(nums[1:]):
            i = int(self.xor(i,value), 16)
        return i

    def xor(self, a, b):
        return hex(a ^ b)

if __name__ == '__main__':
    solu = Solution()
    print solu.singleNumber([2,2,1])