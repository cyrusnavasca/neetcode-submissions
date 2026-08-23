# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of linked list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        # removing node
        idx, target_idx = 0, length - n
        dummy = prev = ListNode(-1, next=head)
        curr = head
        while idx < target_idx: # finding node to remove
            prev = curr
            curr = curr.next
            idx += 1
        prev.next = curr.next

        return dummy.next
            
        