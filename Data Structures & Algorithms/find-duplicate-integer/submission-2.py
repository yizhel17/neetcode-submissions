class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #看成一个带环的链表, 龟兔赛跑(Floyd Algo)

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 1. 把一个指针拉回起点
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
