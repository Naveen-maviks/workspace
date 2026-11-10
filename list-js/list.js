class List {
  constructor() {
    this._items = [];
  }

  // ===== Req 1: Support multiple data types =====
  add(value) {
    this._items.push(value);
  }

  toArray() {
    return [...this._items];
  }

  // ===== Req 3: Add anywhere (front, end, in between) =====
  _checkIndex(index, max) {
    if (!Number.isInteger(index) || index < 0 || index > max) {
      throw new RangeError("index out of range");
    }
  }

  addFirst(value) {
    this._items.unshift(value);
  }

  addAt(index, value) {
    this._checkIndex(index, this._items.length);
    this._items.splice(index, 0, value);
  }

  // ===== Req 4: Mutable =====
  set(index, value) {
    this._checkIndex(index, this._items.length - 1);
    this._items[index] = value;
  }
}

module.exports = { List };
