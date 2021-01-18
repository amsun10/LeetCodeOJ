# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root

        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        if left_ancestor and right_ancestor:
            return root

        if left_ancestor:
            return left_ancestor

        if right_ancestor:
            return right_ancestor
