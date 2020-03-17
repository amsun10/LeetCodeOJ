# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        index = 0
        while nums[index] <= target:
            if nums[index] == target:
                return index

            if index == len(nums) - 1:
                index += 1
                break
            else:
                index += 1
        return index


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 2))
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
