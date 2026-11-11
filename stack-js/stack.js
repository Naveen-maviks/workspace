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
}

module.exports = { Stack };
