# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: [], m: int, nums2: [], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) != m:
            nums1.pop(-1)

        if not nums2:
            return

        if not nums1:
            nums1.extend(nums2)
            return

        index_nums2 = 0
        index_nums1 = 0
        while True:
            if nums2[index_nums2] < nums1[index_nums1]:
                nums1.insert(index_nums1, nums2[index_nums2])
                index_nums2 += 1
            else:
                index_nums1 += 1
                if index_nums1 == len(nums1):
                    nums1.extend(nums2[index_nums2:])
                    break

            if index_nums2 == n:
                break





        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    #solution.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
    solution.merge([2,0], 1, [1], 1)
