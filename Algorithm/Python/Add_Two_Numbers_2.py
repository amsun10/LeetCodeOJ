# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def calculate(self, l):
        i, j = 10, 0
        result = 0
        while l is not None:
            result += l.val * (i**j)
            l = l.next
            j += 1

        return result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result_l1 = self.calculate(l1)
        result_l2 = self.calculate(l2)

        result_l1_l2 = result_l1 + result_l2
        # result_l1_l2 = 807

        num = result_l1_l2 % 10
        root_node = ListNode(num)
        head_node = root_node
        result_l1_l2 = int(result_l1_l2 / 10)

        while result_l1_l2:
            num = result_l1_l2 % 10
            head_node.next = ListNode(num)
            head_node = head_node.next
            result_l1_l2 = int(result_l1_l2 / 10)

        return root_node


if __name__ == '__main__':
    solution = Solution()
    solution.addTwoNumbers(807,807)