__author__ = 'amsun'
"https://leetcode.com/problems/reverse-linked-list/"

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        L1 = ListNode(0)

        while head:
            L1.next, head.next, head = head, L1.next, head.next
            # head.next = L1.next
            # head = head.next

        return L1.next

if __name__ == '__main__':
    a = 3
    b = 4
    a, b = b, a
    print a, b