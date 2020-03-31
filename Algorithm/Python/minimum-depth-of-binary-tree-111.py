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
            min_depth = 1
            if root.left and root.right:
               min_depth += min(self.tree_height(root.left), self.tree_height(root.right))
            elif root.left:
                min_depth += self.tree_height(root.left)
            else:
                min_depth += self.tree_height(root.right)

        return min_depth

    def tree_height(self, node: TreeNode):
        height = 0

        if node:
            height += 1
            left_height = 0
            right_height = 0
            if node.left:
                left_height = self.tree_height(node.left)

            if node.right:
                right_height = self.tree_height(node.right)


            height += min(left_height, right_height)

        return height

