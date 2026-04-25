import heapq

class Solution:    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        heapq.heapify(heap)
    
        for index, node in enumerate(lists):
            heapq.heappush(heap, (node.val, index, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, index, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, index, node))
            

        return dummy.next