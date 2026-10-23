class Node:
    def __init__(self,key,val):
        self.key =key
        self.val=val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.nodes = {} # (key, node)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        

    def insert(self,node):
        # to mru
        # if self.mru.prev:
        #     cur_mru = self.mru.prev
        #     cur_mru.next = node
        
        #     node.prev = cur_mru
        # else:
        #     self.lru.next = node
        prev = self.mru.prev
        prev.next = node
        self.mru.prev = node
        node.next = self.mru
        node.prev = prev
      
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        # find key
        node = self.nodes[key]
        # remove key node
        self.remove(node)
        # insert key node to mru
        self.insert(node)

        return node.val
        


        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            # update existing key
                # remove key node
            node = self.nodes[key]
            self.remove(node)
         # insert key node with NEW value
        newNode = Node(key,value)
        self.insert(newNode)
        self.nodes[key] = newNode


        # if above capacity
        # remove node from lru
        if len(self.nodes) > self.k:
            lru = self.lru.next
            self.remove(lru)
            del self.nodes[lru.key]
        
