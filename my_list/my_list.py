class MyList:
    """A simple ordered list. Positions start at 0."""

    def __init__(self):
        self._items = []

    def append(self, item):
        """Add item at the end of the list."""
        self._items.append(item)
    def size(self):
        """Return the number of items in the list."""
        return len(self._items) 

    def is_empty(self):
        """Return True if the list has no items, otherwise False."""
        return self.size() == 0

    def get(self, index):
        """Return the item at index. Raise IndexError if out of range."""
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range")
        return self._items[index]

    def insert(self, index, item):
        
        if index < 0 or index > self.size():
            raise IndexError("Index out of range")
        self._items.insert(index, item)

    def remove_at(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("index out of range")
        return self._items.pop(index)

    def contains(self, item):
        """Return True if item is in the list."""
        return item in self._items

    def index_of(self, item):
        """Return the first position of item in the list. Raise ValueError if not found."""
        if not self.contains(item):
            raise ValueError("item not found")
        return self._items.index(item)