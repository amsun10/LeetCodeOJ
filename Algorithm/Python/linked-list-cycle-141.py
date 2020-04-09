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
