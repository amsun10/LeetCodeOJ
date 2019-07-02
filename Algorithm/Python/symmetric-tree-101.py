# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    https://leetcode.com/problems/symmetric-tree/
    """

    def isSymmetricNode(self, left_node, right_node):
        if left_node is None or right_node is None:
            if left_node == right_node:
                return True
            return False
        else:
            if left_node.val == right_node.val:
                return self.isSymmetricNode(left_node.left, right_node.right) and \
                       self.isSymmetricNode(left_node.right, right_node.left)
            else:
                return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True
        else:
            return self.isSymmetricNode(root.left, root.right)





