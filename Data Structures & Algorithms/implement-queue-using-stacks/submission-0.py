class MyQueue:

    def __init__(self):
        self.s = []
        

    def push(self, x: int) -> None:
        self.s.insert(0,x)
        

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        if not self.s:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()