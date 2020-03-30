# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: []) -> TreeNode:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        nums_len = len(nums)
        middle = int(nums_len / 2)
        tree_node = TreeNode(nums[middle])
        tree_node.left = self.sortedArrayToBST(nums[:middle-1])
        tree_node.right = self.sortedArrayToBST(nums[middle+1:])
        return tree_node


