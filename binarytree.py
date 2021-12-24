class LinkesBinaryTree(BinaryTree):

    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"
        
        def __init__ (self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node


    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")

        if p._container is not self:
            raise ValueError("p must be proper position type")

        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")

        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None


    def __init__(self):

        self._root = None
        self._size = 0

        def __len__(self):
            return self._size

        def root(self):
            return self._make_position(self._root)

    
