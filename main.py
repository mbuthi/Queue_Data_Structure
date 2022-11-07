from collections import deque

MAX_LENGTH = 10
class Queue:
    def __init__(self) -> None:  
        self.queue = deque()              
    def enqueue(self, element):
        return self.queue.appendleft(element)
    def dequeue(self):
        return self.queue.pop()
    def peek(self):
        return len(self.queue)
    def isFull(self):
        return MAX_LENGTH == len(self.queue)
    def isEmpty(self):
        return len(self.queue) == 0