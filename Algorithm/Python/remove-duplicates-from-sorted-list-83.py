# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur_head = head
        while cur_head is not None:
            if cur_head.next:
                temp_next = cur_head.next
                if cur_head.val == temp_next.val:
                    cur_head.next = temp_next.next
                else:
                    cur_head = cur_head.next
            else:
                break

        return head



