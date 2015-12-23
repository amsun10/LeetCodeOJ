__author__ = 'amsun'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        if root.left and not root.right:
            root.right = TreeNode(root.left.val)
            root.right.left = root.left.left
            root.right.right = root.left.right
            root.left = None

        elif root.right and not root.left:
            root.left = TreeNode(root.right.val)
            root.left.left = root.right.left
            root.left.right = root.right.right
            root.right = None

        elif root.right and root.left:
            temp_val = root.left.val
            root.left.val = root.right.val
            root.right.val = temp_val

            temp_node_left = root.left.left
            temp_node_right = root.left.right
            root.left.left = root.right.left
            root.left.right = root.right.right
            root.right.left = temp_node_left
            root.right.right = temp_node_right

        else:
            return root

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root
