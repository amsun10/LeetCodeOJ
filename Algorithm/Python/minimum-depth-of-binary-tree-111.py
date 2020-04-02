# https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_depth = 0

        if root:
            min_depth += 1
        else:
            return 0

        if root.left is None:
            return min_depth + self.minDepth(root.right)

        if root.right is None:
            return min_depth + self.minDepth(root.left)

        min_depth += min(self.minDepth(root.left), self.minDepth(root.right))

        return min_depth

