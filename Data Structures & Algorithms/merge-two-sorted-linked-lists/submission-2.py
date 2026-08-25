# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            # curr -> p1
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            # curr -> p2
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        
        # if one list is longer than the other
        if p1:
            while p1:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
        
        if p2:
            while p2:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        
        return dummy.next





        