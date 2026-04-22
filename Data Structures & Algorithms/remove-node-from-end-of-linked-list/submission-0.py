# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        inc = length - n
        dummy = ListNode(0, head)
        curr = dummy
        while inc:
            curr = curr.next
            inc -= 1
        curr.next = curr.next.next
        return dummy.next
        
