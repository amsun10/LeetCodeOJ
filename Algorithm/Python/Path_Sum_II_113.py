__author__ = 'amsun'
"https://leetcode.com/problems/path-sum-ii/"
import copy


class Solution(object):
    def __init__(self):
        self.sum_list = []

    def find_sum_list(self, sum_list, node, target):
        sum_list = copy.deepcopy(sum_list)

        if node.left is None and node.right is None:
            if sum(sum_list) + node.val == target:
                sum_list.append(node.val)
                self.sum_list.append(sum_list)
        else:
            sum_list.append(node.val)
            if node.left is not None:
                self.find_sum_list(sum_list, node.left, target)

            if node.right is not None:
                self.find_sum_list(sum_list, node.right, target)

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        self.find_sum_list([], root, target)

        return self.sum_list