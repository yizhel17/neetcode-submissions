class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        
        #key-value mapping: key -> node
        self.cache = {}
        
        #Dummy nodes
        self.left = Node(0, 0) #LRU side
        self.right = Node(0, 0) #MRU side

        self.left.next = self.right
        self.right.prev = self.left


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        #It's used
        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        #Case 1: If the key exists in the cache
        if key in self.cache:
            node = self.cache[key]

            #update the value of the node (A node object)
            node.val = value

            #Remove the node from the linked list
            self.remove(node)

            #Insert the node to the right extreme of the linked list(Most recent used)
            self.insert(node)

        
        #Case 2: If the key doesn't exist
        else:
            #create a new node object
            node = Node(key, value)

            self.cache[key] = node

            self.insert(node)

        if len(self.cache) > self.capa:
            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]

        
    def remove(self, node):
        pre_node = node.prev
        nxt_node = node.next

        pre_node.next = nxt_node
        nxt_node.prev = pre_node
    

    def insert(self, node):
        pre_rightmost_node = self.right.prev

        node.prev = pre_rightmost_node
        pre_rightmost_node.next = node

        node.next = self.right
        self.right.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)