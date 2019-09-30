# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.


class Solution(object):
    def findMedianSortedArrays(self, nums1=[], nums2=[]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums1_len < nums2_len:
            nums1, nums2 = nums2, nums1

        middle = (nums1_len + nums2_len - 1) % 2
        middle_value = (nums1_len + nums2_len - 1) % 2

        if middle == 0:
            middle_min = middle_max = int((nums1_len + nums2_len - 1) / 2)
        else:
            middle_min = int((nums1_len + nums2_len - 1) / 2 - 0.5)
            middle_max = int((nums1_len + nums2_len - 1) / 2 + 0.5)

        nums = nums2 + nums1
        nums.sort()

        return (nums[middle_max] + nums[middle_min]) / 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))




