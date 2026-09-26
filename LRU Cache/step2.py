class Node:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def _add_to_tail(self, node):
        target = self.tail.prev
        
        target.next = node
        node.prev = target
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        target = self.cache[key]
        self._remove(target)
        self._add_to_tail(target)
        return target.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        new = Node(key, value)
        self.cache[key] = new
        self._add_to_tail(new)
        if len(self.cache) > self.capacity:
            target = self.head.next
            self._remove(target)
            del self.cache[target.key]
        
