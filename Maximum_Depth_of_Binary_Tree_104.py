__author__ = 'xizhang'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            length = 1

            if root.left:
                left_length = self.maxDepth(root.left) + 1
            else:
                left_length = 0

            if root.right:
                right_length = self.maxDepth(root.right) + 1
            else:
                right_length = 0

            length += max(left_length, right_length)
        else:
            length = 0

        return length



