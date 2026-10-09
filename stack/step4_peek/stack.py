class Stack:
    """A simple stack: Last In, First Out (LIFO)."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to the top of the stack."""
        pass  # TODO: your push line from step 1

    def is_empty(self):
        """Return True if the stack has no items."""
        pass  # TODO: return a comparison on len(self._items)

    def pop(self):
        """Remove and return the top item. Raise IndexError if empty."""
        pass  # TODO: check is_empty, raise IndexError, else remove and return the last item

    def peek(self):
        """Return the top item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
