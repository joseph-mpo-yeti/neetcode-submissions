# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # def s(self, node):
    #     if not node:
    #         return "X"
    #     elif node.next:
    #         return f"{node.val} -> {self.s(node.next)}"
    #     else:
    #         return f"{node.val} -> X"

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # print(self.s(head))
        front = head
        for _ in range(n):
            front = front.next

        prev, back = None, head
        while front:
            prev, back, front = back, back.next, front.next

        if prev and back:
            prev.next = back.next
            return head

        return head.next