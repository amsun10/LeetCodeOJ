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

        i = 0
        j = 1
        while len(nums) > 1:
            if nums[i] == nums[j]:
                nums.pop(j)
                nums.pop(i)
                if j >= len(nums) - 1:
                    j = len(nums) - 1
                    i += 1

                if i == 0:
                    j += 1
            else:
                if j >= len(nums) - 1:
                    j = len(nums) - 1
                    i += 1

                if i == 0:
                    j += 1

        return nums[0]
if __name__ == '__main__':
    solu = Solution()
    print solu.singleNumber([4,3,5,6,7,5,4,7,6])
    print solu.singleNumber([1,0,1])