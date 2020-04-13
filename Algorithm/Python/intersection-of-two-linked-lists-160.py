# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        address_map = {}
        while headA:
            address_map[id(headA)] = 1
            headA = headA.next

        while headB:
            if address_map.get(id(headB)):
                return headB
            headB = headB.next