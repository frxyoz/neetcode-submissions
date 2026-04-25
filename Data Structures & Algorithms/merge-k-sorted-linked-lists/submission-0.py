class Solution:    
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            l1 = list1
            l2 = list2
            dummy = node = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            dummy.next = l1 or l2
            return node.next


        if len(lists) == 0:
            return None
        while len(lists) > 1:
            lists[1] = mergeTwoLists(lists[0], lists[1])
            lists.pop(0)
        return lists[0]