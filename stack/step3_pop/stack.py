class Stack:
    """A simple stack: Last In, First Out (LIFO)."""

    def __init__(self):
        self._items = []

    def pop(self):
        if self._items:
            return self._items.pop()
        else:
            raise IndexError("pop from empty stack")
