class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        assert capacity > 0
        self.cap = capacity
        self.map = {}  # key -> Node

        # Doubly linked list to maintain order of usage
        self.head = Node()  # MRU side -> left most when cache is printed
        self.tail = Node()  # LRU side -> right most when cache is printed
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        nodes = []
        current = self.head.next
        while current != self.tail:
            nodes.append(f"{current.key}:{current.val}")
            current = current.next
        return "LRUCache{" + ", ".join(nodes) + "}"

    # DLL helpers 
    def _add_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: Node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_front(self, node: Node):
        self._remove(node)
        self._add_to_front(node)

    def _evict_from_back(self) -> Node:
        # real last node before tail
        lru = self.tail.prev
        self._remove(lru)
        return lru

    # ---- public API ----
    def get(self, key: int):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._move_to_front(node)
            return

        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        if len(self.map) > self.cap:
            lru = self._evict_from_back()
            del self.map[lru.key]

def main():
    # Example usage
    # head -> {2=2, 1=1} <- tail
    cache = LRUCache(2)
    cache.put(1, 1)  # cache is {1=1}
    print(cache)
    cache.put(2, 2)  # cache is {2=2, 1=1}
    print(cache)
    cache.get(1)  # changes the order, cache is {1=1, 2=2}
    print(cache)
    cache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
    print(cache)  
    cache.get(2)  # returns -1 (not found)

if __name__ == "__main__":
    main()