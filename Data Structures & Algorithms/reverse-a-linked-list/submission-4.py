# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None -> 0 -> 1 -> 2 -> 3 -> None
        prev = None
        curr = head
        while curr:
            advance_to = curr.next
            curr.next = prev
            prev = curr
            curr = advance_to

        return prev
        