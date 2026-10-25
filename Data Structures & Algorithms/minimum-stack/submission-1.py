class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # 实时记录当前对应栈的最小值,这样就不需要遍历整个栈去找当前的最小值, 时间复杂度是o(1)
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1]) #一一对应

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()