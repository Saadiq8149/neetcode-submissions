class Node:
    def __init__(self, key, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.filled = 0

        self.hashmap = {}
        self.head = None
        self.tail = None 

    def makeRecentlyUsed(self, key: int):
        val = self.hashmap[key]

        if val != self.tail:
            if val == self.head:
                val.next.prev = None
                self.head = val.next

                val.next = None
                val.prev = self.tail
                self.tail.next = val
                self.tail = val            
            else:
                val.prev.next = val.next
                val.next.prev = val.prev

                val.next = None
                val.prev = self.tail
                self.tail.next = val
                self.tail = val             


    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.makeRecentlyUsed(key)
            return self.hashmap[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.makeRecentlyUsed(key)
            self.hashmap[key].val = value
        else:
            if self.filled >= self.capacity:
                lru = self.head

                del self.hashmap[lru.key]

                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None

                self.filled -= 1

            new = Node(key, value)            
            new.prev = self.tail

            self.hashmap[key] = new         

            if not self.tail:
                self.head = new
                self.tail = new
            else:
                self.tail.next = new
                self.tail = new   
            self.filled += 1         

