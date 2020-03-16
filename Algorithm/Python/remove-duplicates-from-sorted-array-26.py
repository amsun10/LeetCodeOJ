class Solution:
    def removeDuplicates(self, nums=[]) -> int:
        unique_array_len = 1
        while unique_array_len < len(nums):
            if nums[unique_array_len - 1] == nums[unique_array_len]:
                nums.pop(unique_array_len - 1)
            else:
                unique_array_len += 1

        return unique_array_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4]))















