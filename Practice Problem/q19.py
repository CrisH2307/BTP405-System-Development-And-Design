class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not (len(self.items) == 0): return self.items.pop()
    
    def peek(self):
        if not (len(self.items) == 0): return self.items[-1]

    def length(self):
        return (len(self.items))

stack = Stack()

stack.push("Fuck")
stack.push("My")
stack.push("Mom")

for each in range(stack.length()):
    print(stack.pop())

for each in range(stack.length()):
    print(stack.peek())

