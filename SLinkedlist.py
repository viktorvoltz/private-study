class Linkedstack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):

        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):

        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._head._element