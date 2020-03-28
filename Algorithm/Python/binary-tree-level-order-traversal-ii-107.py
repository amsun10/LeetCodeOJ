# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = {}

    def levelOrderBottom(self, root):
        self.result = {}
        self.search(root, 0)
        result_array = []
        index = 0
        while self.result.get(index):
            result_array.insert(0, self.result.get(index))
            index += 1
        return result_array

    def search(self, tree_node, index:int):
        if tree_node:
            if not self.result.get(index):
                self.result[index] = []
            self.result[index].append(tree_node.val)

            if tree_node.left:
                self.search(tree_node.left, index+1)

            if tree_node.right:
                self.search(tree_node.right, index+1)
