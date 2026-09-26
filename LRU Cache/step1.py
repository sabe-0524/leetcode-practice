class Node:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        target = self.cache[key]
        if target == self.tail:
            return target.val
        if target == self.head:
            self.head = target.next
        if target.prev:
            target.prev.next = target.next
        if target.next:
            target.next.prev = target.prev
        target.next = None
        target.prev = self.tail
        self.tail.next = target
        self.tail = target
        return target.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        if self.count < self.capacity:
            self.count += 1
        else:
            del self.cache[self.head.key]
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        
        new = Node(key, value, None, self.tail)
        if self.tail:
            self.tail.next = new
        self.cache[key] = new
        self.tail = new
        if self.count == 1:
            self.head = new
