# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_value = None
        self.stack = []

    def push(self, x: int) -> None:
        if self.min_value is not None:
            if x < self.min_value:
                self.min_value = x
        else:
            self.min_value = x

        self.stack.insert(0, [x, self.min_value])

    def pop(self) -> None:
        self.stack.pop(0)
        if not self.stack:
            self.min_value = None
        else:
            self.min_value = self.stack[0][1]

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()