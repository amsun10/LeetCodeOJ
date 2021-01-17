# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        address_list = []
        address_list.append(id(head))
        while head.next is not None:
            if id(head.next) in address_list:
                return True
            else:
                address_list.append(id(head.next))
            head = head.next
        return False


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = head
        fast = head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
