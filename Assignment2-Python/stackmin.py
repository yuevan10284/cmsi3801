#3.2 Stack Min (p.98)
'''Stack Min: How would you design a stack which, in addition to p u s h and pop, has a function m i n
which returns the minimum eiement? Push, p o p and m i n should ail operate in 0 ( 1 ) time'''

class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else: 
            self.min_stack.append(self.min_stack[-1])
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

#TestCase
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Returns -3
minStack.pop()
print(minStack.top())     # Returns 0
print(minStack.getMin())  # Returns -2