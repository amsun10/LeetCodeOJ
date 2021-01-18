# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2

        if t2 is None:
            return t1

        t1.val += t2.val

        if t1.left is None:
            t1.left = t2.left
        else:
            t1.left = self.mergeTrees(t1.left, t2.left)

        if t1.right is None:
            t1.right = t2.right
        else:
            t2.right = self.mergeTrees(t2.right, t2.right)

        return t1
