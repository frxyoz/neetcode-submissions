# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        dummy = ListNode()
        dummy.next = head
        prevGroup = dummy
        curr = dummy.next

        i = 1
        while True:
            while i < k:
                if not curr.next:
                    return dummy.next
                curr = curr.next
                i += 1
            nextGroup = curr.next
            curr.next = None
            prevGroup.next = reverse(prevGroup.next)
            for i in range(k):
                prevGroup = prevGroup.next
            prevGroup.next = nextGroup
            curr = prevGroup
            i = 0
        return

        
                

            