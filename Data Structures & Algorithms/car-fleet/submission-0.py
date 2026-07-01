class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #统一成 时间 来比较

        #先倒序, 按距终点的位置 从近到远 排序, 因为题目规定不能超车
        cars = sorted(zip(position, speed), reverse = True)

        stack = []

        for p, s in cars:
            t = (target - p) / s

            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #后车用时短于前车, 会与前车形成车队
                stack.pop()

        return len(stack)
