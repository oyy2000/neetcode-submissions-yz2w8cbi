# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the mid to last nodes
        second = slow.next
        slow.next = None

        prev, cur = None, second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        second = prev

        # merge prev and head
        l1 , l2 = head, second
        while l2:
           n1, n2 = l1.next, l2.next
           l1.next = l2
           l2.next = n1
           l1, l2 = n1, n2         

        return 
