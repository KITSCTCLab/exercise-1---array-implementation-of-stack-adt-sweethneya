import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return self.top <= -1

    def is_full(self):
        if(self.isfull():
            print("Stack is full....")
        else:
            self.top +=1
            self.stack[self.top]=int(input("Enter the data: ")
            print(self.stack)

    def push(self, data):
        if not self.is_full():
            self.top += 1
            self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            x=self.stack.pop()
            self.top -= 1
            return x

    def status(self):
        if(self.isempty()):
           print("Stack is empty")
        else:
           print(self.stack[self.top])

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
