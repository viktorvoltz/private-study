class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):

        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError('Queue is Empty')
        return self._data[self._front]

    def add_first(self, e):
        self._front = (self._front - 1) % len(self._data)
        self._size += 1
        self._data[self._front] = e

    def delete_last(self):
        if self.is_empty():
            raise IndexError('Queue is Empty')
        last = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last]
        self._data[last] = None
        self._size = -1
        return answer
        

    def delete_first(self):

        if self.is_empty():
            raise IndexError('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)% len(self._data)
        self._size -= 1
        return answer

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size)% len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self.data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]

            walk = (1 + walk) % len(old)

        self._front = 0


q = ArrayQueue()
q.add_last(5)
q.add_first(3)
q.add_first(7)
print(q.first())
print(len(q))

