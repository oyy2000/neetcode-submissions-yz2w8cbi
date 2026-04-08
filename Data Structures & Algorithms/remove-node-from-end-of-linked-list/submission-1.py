# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        n1, n2 = dummy, dummy
        for i in range(n):
            n2 = n2.next

        while n2 and n2.next:
            n1 = n1.next
            n2 = n2.next
        if n1.next: 
            n1.next = n1.next.next 
        return dummy.next
