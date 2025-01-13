# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueUsingTwoStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        print(self.stack2[-1])

import sys
input = sys.stdin.read

data = input().splitlines()
queue = QueueUsingTwoStack()

for line in data[1:]:
    query = line.split()
    if query[0] == '1':
        queue.enqueue(int(query[1]))
    elif query[0] == '2':
        queue.dequeue()
    elif query[0] == '3':
        queue.peek()
