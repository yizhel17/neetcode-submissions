# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        left = 0
        right = len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break
            
            nodes[right].next = nodes[left]
            right -= 1
        
        nodes[left].next = None
        