class List {
  constructor() {
    this._items = [];
  }

  add(value) {
    this._items.push(value);
  }

  toArray() {
    return [...this._items];
  }
}

module.exports = { List };