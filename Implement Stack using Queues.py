class MyStack:

    def __init__(self):
        self.vals = []

    def push(self, x: int) -> None:
        self.vals.append(x)

    def pop(self) -> int:
        return self.vals.pop(-1)

    def top(self) -> int:
        return self.vals[-1]

    def empty(self) -> bool:
        return len(self.vals) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()