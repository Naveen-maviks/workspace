const { List } = require("./list");

const make = (...items) => {
  const list = new List();
  items.forEach((i) => list.add(i));
  return list;
};

describe("Req 3: add anywhere", () => {
  test("add at the front", () => {
    const list = make(2, 3);
    list.addFirst(1);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test("add at the front of an empty list", () => {
    const list = new List();
    list.addFirst(1);
    expect(list.toArray()).toEqual([1]);
  });

  test("add at the end", () => {
    const list = make(1, 2);
    list.add(3);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test("add in between", () => {
    const list = make(1, 3);
    list.addAt(1, 2);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test("addAt works at the start and the end", () => {
    const list = make(2);
    list.addAt(0, 1);
    list.addAt(2, 3);
    expect(list.toArray()).toEqual([1, 2, 3]);
  });

  test("invalid index throws and leaves the list unchanged", () => {
    const list = make(1);
    expect(() => list.addAt(5, 9)).toThrow(RangeError);
    expect(() => list.addAt(-1, 9)).toThrow(RangeError);
    expect(list.toArray()).toEqual([1]);
  });
});
