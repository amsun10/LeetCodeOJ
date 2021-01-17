# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        c = None
        while head:
            temp = head.next
            head.next = c
            c = head
            head = temp
        return c


if __name__ == '__main__':
    a = [2, 3]
    b = a
    a.append(4)
    print(a, b)