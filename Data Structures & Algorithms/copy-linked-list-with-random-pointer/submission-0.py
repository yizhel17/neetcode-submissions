"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # The main difficulty: Since a random pointer of a single node 
        # may point to an existed seen node, which may not be even copied yet, 
        # let alone to point something to them. 

        # So the solution to that would be to first create a hashmap 
        # where all nodes in the linked list have their own copy in.
        CopyNode = {None: None}
        # The neetcode calls it "Two Passes" algorithm.


        # First, we iterate through the entire linked list for mapping old nodes 
        # with copy of themselves.
        cur = head
        while cur:
            copy = Node(cur.val)
            CopyNode[cur] = copy
            cur = cur.next
        
        # Second, we distribute the pointers ("next" and "random") of the copies
        cur = head
        while cur:
            copy = CopyNode[cur]
            copy.next = CopyNode[cur.next] #Edge case: when cur.next is Null ? 
            copy.random = CopyNode[cur.random]
            cur = cur.next
        
        return CopyNode[head]
