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

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if len(self._stack)>0:
            return self._stack.pop(0)
        return None

    def peek(self):
        if len(self._stack)>0:
            return self._stack[0]
        return None

    def size(self):
        return len(self._queue)

    def empty(self):
        return bool(self._queue)