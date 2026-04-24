class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # insert right before tail (most recent)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])

        node = Node(key, value)
        self.hm[key] = node
        self.insert(node)

        if len(self.hm) > self.cap:
            # remove LRU (head.next)
            lru = self.head.next
            self.remove(lru)
            del self.hm[lru.key]