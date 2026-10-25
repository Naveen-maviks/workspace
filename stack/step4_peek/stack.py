class Stack:
    """A simple stack: Last In, First Out (LIFO)."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to the top of the stack."""
        pass  # TODO: paste your push line from step 1

    def is_empty(self):
        """Return True if the stack has no items."""
        pass  # TODO: paste your is_empty line from step 2

    def pop(self):
        """Remove and return the top item. Raise IndexError if empty."""
        pass  # TODO: your pop code from step 3

    def peek(self):
        """Return the top item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]