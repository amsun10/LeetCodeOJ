__author__ = 'amsun'
"https://leetcode.com/problems/majority-element/"

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appears = {}
        len_num = len(nums)

        if len_num == 1:
            return nums[0]

        for index, num in enumerate(nums):
            appears[num] = appears.get(num, 0) + 1

        for key, value in appears.items():
            if value > int(len_num / 2):
                return key

if __name__ == '__main__':
    solu = Solution()
    print solu.majorityElement([3, 2, 3])