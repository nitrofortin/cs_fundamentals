class Array(object):
    def __init__(self, array_size, placeholder=None):
        self._array = [placeholder]*array_size

    def __getitem__(self, idx):
        return self._array[idx]

class ArrayList(list):
    def __init__(self):
        self._array = [None]
        self._array_size = 1
        self._array_iter = 0

    def append(self, value):
        if self._array_iter > len(self._array) - 1:
            self._array = self._array + [None]*self._array_size
            self._array_size = len(self._array)

        self._array[self._array_iter] = value
        self._array_iter += 1 


class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if len(self._stack)>0:
            return self._stack.pop()
        return None

    def peek(self):
        if len(self._stack)>0:
            return self._stack[-1]
        return None
        
    def empty(self):
        return bool(self._stack)

class Queue(object):
    def __init__(self):
        self._queue = []
        self._queue_size = 0

    def enqueue(self, value):
        self._queue_size += 1
        self._queue.append(value)

    def dequeue(self):
        if len(self._queue)>0:
            self._queue_size -= 1
            return self._queue.pop(0)
        return None

    def peek(self):
        if len(self._queue)>0:
            return self._queue[0]
        return None

    def size(self):
        return self._queue_size

    def empty(self):
        return bool(self._queue)

class Dequeue(object):
    def __init__(self):
        self._dequeue = []

    def enqueue_bottom(self, value):
        self._dequeue.append(value)

    def enqueue_top(self, value):
        self._dequeue = [value] + self._dequeue

    def dequeue_top(self):
        if len(self._dequeue)>0:
            return self._dequeue.pop()
        return None

    def dequeue_top(self):
        if len(self._dequeue)>0:
            return self._dequeue.pop(0)
        return None

    def peek_bottom(self):
        if len(self._dequeue)>0:
            return self._dequeue[-1]
        return None

    def peek_top(self):
        if len(self._dequeue)>0:
            return self._dequeue[0]
        return None

    def size(self):
        return len(self._dequeue)

    def empty(self):
        return bool(self._dequeue)
