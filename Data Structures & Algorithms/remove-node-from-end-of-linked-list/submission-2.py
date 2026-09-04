# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize slow/fast pointers and prev
        prev = dummy = ListNode(-1)
        dummy.next = head
        slow = fast = head

        # count how far fast is
        count = 0

        # move fast pointer (n - 1) times
        while count < (n-1):
            fast = fast.next
            count += 1
        
        # simultaneously move both until fast is at the end of the list
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # remove slow node
        prev.next = slow.next

        return dummy.next

        

