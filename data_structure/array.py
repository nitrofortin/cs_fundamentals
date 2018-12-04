class Array:
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