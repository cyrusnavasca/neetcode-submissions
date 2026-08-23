# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        idx = 0
        while idx < n: # get right node to be n from the start
            right = right.next
            idx += 1
        
        prev = dummy = ListNode(-1, next=head)
        while right: # get left node to correct position
            prev = prev.next
            left = left.next
            right = right.next

        prev.next = left.next

        return dummy.next
        


        




