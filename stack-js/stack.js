class Stack {
  constructor() {
    this._items = [];
  }

  // ===== Req 1: Push (any data type, duplicates allowed) =====
  push(value) {
    this._items.push(value);
  }

  // Helper for tests: items from bottom to top
  toArray() {
    return [...this._items];
  }

  // ===== Req 2: Pop (remove and return the top item) =====
  pop() {
    if (this._items.length === 0) {
      throw new Error("stack is empty");
    }
    return this._items.pop();
  }

  // ===== Req 3: Peek (read the top item without removing it) =====
  peek() {
    if (this._items.length === 0) {
      throw new Error("stack is empty");
    }
    return this._items[this._items.length - 1];
  }

  // ===== Req 4: Size (number of items in the stack) =====
  get size() {
    return this._items.length;
  }
}

module.exports = { Stack };
