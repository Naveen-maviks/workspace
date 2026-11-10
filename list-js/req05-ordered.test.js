const { List } = require("./list");

const make = (...items) => {
  const list = new List();
  items.forEach((i) => list.add(i));
  return list;
};

describe("Req 5: ordered sequence", () => {
  test("keeps insertion order and does not sort", () => {
    expect(make(3, 1, 2).toArray()).toEqual([3, 1, 2]);
  });

  test("adding at the end does not change the existing order", () => {
    const list = make(3, 1, 2);
    list.add(0);
    expect(list.toArray()).toEqual([3, 1, 2, 0]);
  });

  test("adding at the front keeps the rest in order", () => {
    const list = make(3, 1, 2);
    list.addFirst(9);
    expect(list.toArray()).toEqual([9, 3, 1, 2]);
  });

  test("adding in between keeps the rest in order", () => {
    const list = make(3, 1, 2);
    list.addAt(1, 7);
    expect(list.toArray()).toEqual([3, 7, 1, 2]);
  });

  test("mixed types stay in the order they were added", () => {
    expect(make("b", 2, "a", 1).toArray()).toEqual(["b", 2, "a", 1]);
  });
});
