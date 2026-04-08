# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(0)
        

        while list1 and list2:
                           
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if not list1:
            dummy.next = list2
        if not list2:
            dummy.next = list1 
        return node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        for i in range(1, len(lists)):
           lists[i] = self.mergeTwoLists(lists[i], lists[i-1])

        return lists[len(lists) - 1]
        