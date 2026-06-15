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
        if not head and head.next:
            return
        
        #寻找中点并切断成两部分

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow刚好停在终点位置
        sec_prt_head = slow.next #单独拿出后半部分的车头
        slow.next = None #切断两半部分的连接

        #反转后半部分

        pre = None
        cur = sec_prt_head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        l1 = head
        l2 = pre

        #开始合并两部分

        while l1 and l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l1 = nxt1

            l2.next = l1
            l2 = nxt2

