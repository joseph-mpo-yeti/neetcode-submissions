# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        final, c1, c2 = dummy, list1, list2

        while c1 and c2:        
            if c1.val <= c2.val:
                final.next = c1
                c1 = c1.next
            else:
                final.next = c2
                c2 = c2.next

            final = final.next
        
        final.next = c1 or c2

        return dummy.next