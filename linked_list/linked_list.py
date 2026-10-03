class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def to_list(self):
        return list(self)    
        
class LinkedList:
    def __init__(self):
        self.head = None

    # Requirement 1
    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def to_list(self):
        """Helper that makes tests easy to write."""
        result, cur = [], self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # Req 3: add anywhere
    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self._size += 1

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._size += 1

    def insert(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if index == 0:
            self.insert_at_head(data)
            return
        prev = self._node_at(index - 1)
        node = Node(data)
        node.next = prev.next
        prev.next = node
        self._size += 1

    # Req 6: access by index
    def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur

    def get(self, index):
        return self._node_at(index).data

    def __getitem__(self, index):
        return self.get(index)

    # Req 4: mutable
    def __setitem__(self, index, data):
        self._node_at(index).data = data

    # Req 7: length
    def __len__(self):
        return self._size

    # Req 8: remove
    def remove_first(self):
        return self.remove_at(0)

    def remove_last(self):
        return self.remove_at(self._size - 1)

    def remove_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        if index == 0:
            removed = self.head
            self.head = removed.next
        else:
            prev = self._node_at(index - 1)
            removed = prev.next
            prev.next = removed.next
        self._size -= 1
        return removed.data

    # Req 9: search
    def search(self, data):
        for i, value in enumerate(self):
            if value == data:
                return i
        return -1

    def __contains__(self, data):
        return self.search(data) != -1

    # Req 10: clear
    def clear(self):
        self.head = None
        self._size = 0

    # Req 11: iterable
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __str__(self):
        return " -> ".join(repr(x) for x in self) or "(empty)"