# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        dum = head

        while dum:
            leng += 1
            dum = dum.next
        real = leng - n

        # --- 核心大招：召唤哨兵假人守住起点 ---
        fake_head = ListNode(0)
        fake_head.next = head
        # 让你的移动推土机停在假人这里起跑
        pre = fake_head

        for _ in range(real):
            pre = pre.next
        # 此时 pre 稳稳地停在了【被删除节点的前一个节点】身上！

        pre.next = pre.next.next

        return fake_head.next

        