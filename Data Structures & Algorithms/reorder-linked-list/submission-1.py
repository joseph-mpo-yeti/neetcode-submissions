# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return
        
        # Find middle node
        last = slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
    
        # Reverse the second half
        prev, curr = None, slow.next
        slow.next = None # disconnect halves
        while curr:
            tmp = curr.next
            curr.next, prev = prev, curr
            curr = tmp
        
        # connect first half with reverse half alternating nodes
        first = head
        second = prev
        while first and second:
            tmp_f = first.next
            tmp_s = second.next
            first.next = second
            if tmp_f:
                second.next = tmp_f
            first = tmp_f
            second = tmp_s
