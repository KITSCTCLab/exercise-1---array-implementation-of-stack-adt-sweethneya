import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.top=-1
        self.size = size

    def is_empty(self):
        return self.top>-1

    def is_full(self):
        return len(self.items)==self.top

    def push(self, data):
        if not self.is_full():
            self.top+=1
            self.items.append(data)

    def pop(self):
        if self.is_empty():
            self.top-=1
            del self.items[-1]
            
    def status(self):
        for i in self.items:
            print(i)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
