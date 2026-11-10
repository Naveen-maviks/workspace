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
}

module.exports = { List };
