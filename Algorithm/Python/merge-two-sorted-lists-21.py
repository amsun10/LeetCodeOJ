# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_node_new = ListNode()
        head = list_node_new

        if not l1:
            return l2

        if not l2:
            return l1

        while l1 and l2:
            if l1.val <= l2.val:
                list_node_new.val = l1.val
                l1 = l1.next
            else:
                list_node_new.val = l2.val
                l2 = l2.next

            if l1 and l2:
                list_node_new.next = ListNode()
                list_node_new = list_node_new.next

        if not l1:
            list_node_new.next = l2
        else:
            list_node_new.next = l1

        return head