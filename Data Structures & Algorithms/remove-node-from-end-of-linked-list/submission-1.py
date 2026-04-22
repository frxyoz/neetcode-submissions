# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while n-1:
            curr = curr.next
            n = n - 1
        dummy = ListNode(0, head)
        new = dummy
        while curr.next:
            new = new.next
            curr = curr.next
        new.next = new.next.next
        return dummy.next
        
