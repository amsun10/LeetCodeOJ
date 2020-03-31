# https://leetcode.com/problems/balanced-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root:
            if abs(self.tree_height(root.right) - self.tree_height(root.left)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)

        return True

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

            height += max(left_height, right_height)

        return height