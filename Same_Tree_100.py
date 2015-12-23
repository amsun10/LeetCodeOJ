__author__ = 'amsun'
"https://leetcode.com/problems/same-tree/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p and q:
            if p.val == q.val:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if not p and not q:
                return True
            else:
                return False

